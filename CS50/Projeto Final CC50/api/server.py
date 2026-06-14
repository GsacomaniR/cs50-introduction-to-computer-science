"""
API RESTful para sincronização de tarefas
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Permite requisições do seu app CLI

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'storage', 'tasks.db')

def get_db():
    """Conecta ao banco de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ============= ROTAS DA API =============

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Lista todas as tarefas"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Parâmetros de filtro opcionais
    completed = request.args.get('completed')
    priority = request.args.get('priority')
    
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []
    
    if completed is not None:
        query += " AND completed = ?"
        params.append(1 if completed.lower() == 'true' else 0)
    
    if priority:
        query += " AND priority = ?"
        params.append(priority)
    
    query += " ORDER BY CASE priority WHEN 'alta' THEN 1 WHEN 'media' THEN 2 WHEN 'baixa' THEN 3 END, due_date"
    
    cursor.execute(query, params)
    tasks = [dict(row) for row in cursor.fetchall()]
    
    # Converter booleanos
    for task in tasks:
        task['completed'] = bool(task['completed'])
    
    conn.close()
    return jsonify({
        'success': True,
        'count': len(tasks),
        'tasks': tasks
    })

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Busca uma tarefa específica"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    
    if task:
        task_dict = dict(task)
        task_dict['completed'] = bool(task_dict['completed'])
        return jsonify({'success': True, 'task': task_dict})
    else:
        return jsonify({'success': False, 'error': 'Tarefa não encontrada'}), 404

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Cria uma nova tarefa"""
    data = request.json
    
    required_fields = ['title', 'priority', 'due_date']
    for field in required_fields:
        if field not in data:
            return jsonify({'success': False, 'error': f'Campo {field} é obrigatório'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO tasks (title, priority, due_date, completed, created_at, review_count)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['title'],
        data['priority'],
        data['due_date'],
        0,  # completed = False
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        0
    ))
    
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'task_id': task_id,
        'message': 'Tarefa criada com sucesso'
    }), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente"""
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    
    # Construir query dinâmica
    updates = []
    params = []
    
    updatable_fields = ['title', 'priority', 'due_date', 'completed', 
                        'review_count', 'last_reviewed', 'next_review']
    
    for field in updatable_fields:
        if field in data:
            updates.append(f"{field} = ?")
            if field == 'completed':
                params.append(1 if data[field] else 0)
            else:
                params.append(data[field])
    
    if not updates:
        return jsonify({'success': False, 'error': 'Nenhum campo para atualizar'}), 400
    
    params.append(task_id)
    query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query, params)
    
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    
    if affected > 0:
        return jsonify({'success': True, 'message': 'Tarefa atualizada'})
    else:
        return jsonify({'success': False, 'error': 'Tarefa não encontrada'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Remove uma tarefa"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    affected = cursor.rowcount
    conn.commit()
    conn.close()
    
    if affected > 0:
        return jsonify({'success': True, 'message': 'Tarefa removida'})
    else:
        return jsonify({'success': False, 'error': 'Tarefa não encontrada'}), 404

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Estatísticas via API"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as total FROM tasks")
    total = cursor.fetchone()['total']
    
    cursor.execute("SELECT COUNT(*) as completed FROM tasks WHERE completed = 1")
    completed = cursor.fetchone()['completed']
    
    cursor.execute('''
        SELECT priority, COUNT(*) as count 
        FROM tasks 
        GROUP BY priority
    ''')
    priorities = {row['priority']: row['count'] for row in cursor.fetchall()}
    
    cursor.execute('''
        SELECT COUNT(*) as due FROM tasks 
        WHERE next_review <= date('now') AND completed = 0
    ''')
    due_today = cursor.fetchone()['due']
    
    conn.close()
    
    return jsonify({
        'success': True,
        'stats': {
            'total_tasks': total,
            'completed_tasks': completed,
            'completion_rate': (completed / total * 100) if total > 0 else 0,
            'priorities': priorities,
            'due_today': due_today
        }
    })

@app.route('/api/sync', methods=['POST'])
def sync_tasks():
    """Sincroniza múltiplas tarefas de uma vez"""
    data = request.json
    tasks_to_sync = data.get('tasks', [])
    
    conn = get_db()
    cursor = conn.cursor()
    
    results = {
        'created': 0,
        'updated': 0,
        'errors': []
    }
    
    for task in tasks_to_sync:
        try:
            # Verificar se existe
            cursor.execute("SELECT id FROM tasks WHERE id = ?", (task.get('id'),))
            exists = cursor.fetchone()
            
            if exists:
                # Atualizar
                updates = []
                params = []
                for field in ['title', 'priority', 'due_date', 'completed', 'review_count']:
                    if field in task:
                        updates.append(f"{field} = ?")
                        if field == 'completed':
                            params.append(1 if task[field] else 0)
                        else:
                            params.append(task[field])
                
                if updates:
                    params.append(task['id'])
                    cursor.execute(f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?", params)
                    results['updated'] += 1
            else:
                # Criar
                cursor.execute('''
                    INSERT INTO tasks (id, title, priority, due_date, completed, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    task.get('id'),
                    task['title'],
                    task['priority'],
                    task['due_date'],
                    1 if task.get('completed', False) else 0,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ))
                results['created'] += 1
                
        except Exception as e:
            results['errors'].append(str(e))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'results': results
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Verifica se a API está online"""
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("="*50)
    print("🌐 StudyFlow API Server")
    print("="*50)
    print(f"📁 Banco de dados: {DATABASE_PATH}")
    print(f"🚀 Servidor rodando em: http://localhost:5000")
    print(f"📋 Endpoints disponíveis:")
    print(f"   GET    /api/health          - Status da API")
    print(f"   GET    /api/tasks           - Listar tarefas")
    print(f"   GET    /api/tasks/<id>      - Buscar tarefa")
    print(f"   POST   /api/tasks           - Criar tarefa")
    print(f"   PUT    /api/tasks/<id>      - Atualizar tarefa")
    print(f"   DELETE /api/tasks/<id>      - Remover tarefa")
    print(f"   GET    /api/stats           - Estatísticas")
    print(f"   POST   /api/sync            - Sincronização em lote")
    print("="*50)
    print("\n⚠️  Pressione Ctrl+C para parar o servidor\n")
    
    app.run(debug=True, host='localhost', port=5000)