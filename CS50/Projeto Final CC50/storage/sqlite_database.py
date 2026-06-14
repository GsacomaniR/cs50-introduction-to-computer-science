"""
Gerencia persistência usando SQLite para alta performance
"""
import sqlite3
import json
from typing import List, Dict, Optional
from datetime import datetime
import os

class SQLiteDatabase:
    def __init__(self, filename="storage/tasks.db"):
        self.filename = filename
        self._ensure_directory_exists()
        self._create_tables()
    
    def _ensure_directory_exists(self):
        """Garante que o diretório existe"""
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
    
    def _get_connection(self):
        """Cria e retorna conexão com o banco"""
        conn = sqlite3.connect(self.filename)
        conn.row_factory = sqlite3.Row  # Permite acesso por nome de coluna
        return conn
    
    def _create_tables(self):
        """Cria as tabelas necessárias"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Tabela principal de tarefas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                priority TEXT CHECK(priority IN ('alta', 'media', 'baixa')),
                due_date TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                review_count INTEGER DEFAULT 0,
                last_reviewed TEXT,
                next_review TEXT
            )
        ''')
        
        # Índices para buscas rápidas
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_completed ON tasks(completed)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_priority ON tasks(priority)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_due_date ON tasks(due_date)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_next_review ON tasks(next_review)')
        
        # Tabela de backup/estatísticas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stats (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_task(self, task: Dict) -> int:
        """Salva uma única tarefa e retorna o ID"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO tasks (title, priority, due_date, completed, created_at, 
                             review_count, last_reviewed, next_review)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            task['title'],
            task['priority'],
            task['due_date'],
            1 if task['completed'] else 0,
            task['created_at'],
            task.get('review_count', 0),
            task.get('last_reviewed'),
            task.get('next_review')
        ))
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return task_id
    
    def load_all_tasks(self) -> List[Dict]:
        """Carrega todas as tarefas"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tasks ORDER BY id')
        rows = cursor.fetchall()
        
        tasks = []
        for row in rows:
            tasks.append({
                'id': row['id'],
                'title': row['title'],
                'priority': row['priority'],
                'due_date': row['due_date'],
                'completed': bool(row['completed']),
                'created_at': row['created_at'],
                'review_count': row['review_count'],
                'last_reviewed': row['last_reviewed'],
                'next_review': row['next_review']
            })
        
        conn.close()
        return tasks
    
    def update_task(self, task_id: int, task_data: Dict) -> bool:
        """Atualiza uma tarefa existente"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tasks 
            SET title = ?, priority = ?, due_date = ?, completed = ?,
                review_count = ?, last_reviewed = ?, next_review = ?
            WHERE id = ?
        ''', (
            task_data['title'],
            task_data['priority'],
            task_data['due_date'],
            1 if task_data['completed'] else 0,
            task_data.get('review_count', 0),
            task_data.get('last_reviewed'),
            task_data.get('next_review'),
            task_id
        ))
        
        affected = cursor.rowcount
        conn.commit()
        conn.close()
        return affected > 0
    
    def delete_task(self, task_id: int) -> bool:
        """Remove uma tarefa pelo ID"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        affected = cursor.rowcount
        conn.commit()
        conn.close()
        return affected > 0
    
    def search_tasks(self, keyword: str) -> List[Dict]:
        """Busca tarefas por palavra-chave (usando LIKE com índice)"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Usando LIKE com escape para busca eficiente
        cursor.execute('''
            SELECT * FROM tasks 
            WHERE title LIKE ? 
            ORDER BY 
                CASE priority 
                    WHEN 'alta' THEN 1 
                    WHEN 'media' THEN 2 
                    WHEN 'baixa' THEN 3 
                END,
                due_date
        ''', (f'%{keyword}%',))
        
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append({
                'id': row['id'],
                'title': row['title'],
                'priority': row['priority'],
                'due_date': row['due_date'],
                'completed': bool(row['completed']),
                'created_at': row['created_at'],
                'review_count': row['review_count'],
                'last_reviewed': row['last_reviewed'],
                'next_review': row['next_review']
            })
        
        conn.close()
        return tasks
    
    def get_pending_tasks(self) -> List[Dict]:
        """Retorna apenas tarefas pendentes (mais eficiente)"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM tasks 
            WHERE completed = 0 
            ORDER BY 
                CASE priority 
                    WHEN 'alta' THEN 1 
                    WHEN 'media' THEN 2 
                    WHEN 'baixa' THEN 3 
                END,
                due_date
        ''')
        
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append({
                'id': row['id'],
                'title': row['title'],
                'priority': row['priority'],
                'due_date': row['due_date'],
                'completed': bool(row['completed']),
                'created_at': row['created_at'],
                'review_count': row['review_count'],
                'last_reviewed': row['last_reviewed'],
                'next_review': row['next_review']
            })
        
        conn.close()
        return tasks
    
    def get_due_for_review(self) -> List[Dict]:
        """Retorna tarefas para revisão hoje (usando índice)"""
        today = datetime.now().strftime("%Y-%m-%d")
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM tasks 
            WHERE next_review <= ? AND completed = 0
            ORDER BY next_review
        ''', (today,))
        
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append({
                'id': row['id'],
                'title': row['title'],
                'priority': row['priority'],
                'due_date': row['due_date'],
                'completed': bool(row['completed']),
                'created_at': row['created_at'],
                'review_count': row['review_count'],
                'last_reviewed': row['last_reviewed'],
                'next_review': row['next_review']
            })
        
        conn.close()
        return tasks
    
    def get_stats(self) -> Dict:
        """Retorna estatísticas usando queries agregadas"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Total de tarefas
        cursor.execute('SELECT COUNT(*) as total FROM tasks')
        total = cursor.fetchone()['total']
        
        # Tarefas concluídas
        cursor.execute('SELECT COUNT(*) as completed FROM tasks WHERE completed = 1')
        completed = cursor.fetchone()['completed']
        
        # Tarefas por prioridade
        cursor.execute('''
            SELECT priority, COUNT(*) as count 
            FROM tasks 
            GROUP BY priority
        ''')
        priorities = {row['priority']: row['count'] for row in cursor.fetchall()}
        
        # Tarefas para revisar hoje
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute('''
            SELECT COUNT(*) as due FROM tasks 
            WHERE next_review <= ? AND completed = 0
        ''', (today,))
        due_today = cursor.fetchone()['due']
        
        conn.close()
        
        return {
            'total_tasks': total,
            'completed_tasks': completed,
            'completion_rate': (completed / total * 100) if total > 0 else 0,
            'priorities': priorities,
            'due_today': due_today
        }
    
    def backup(self) -> bool:
        """Cria backup do banco de dados SQLite"""
        backup_name = f"{self.filename}.backup"
        try:
            import shutil
            shutil.copy2(self.filename, backup_name)
            print(f"Backup criado: {backup_name}")
            return True
        except Exception as e:
            print(f"Erro no backup: {e}")
            return False
    
    def migrate_from_json(self, json_filename="storage/tasks.json"):
        """Migra dados do JSON antigo para o SQLite"""
        import json
        import os
        
        if not os.path.exists(json_filename):
            print("Arquivo JSON não encontrado. Nada a migrar.")
            return
        
        try:
            with open(json_filename, 'r', encoding='utf-8') as f:
                old_tasks = json.load(f)
            
            print(f"Migrando {len(old_tasks)} tarefas do JSON para SQLite...")
            
            for task in old_tasks:
                # Remove o campo 'id' pois o SQLite vai gerar automaticamente
                if 'id' in task:
                    del task['id']
                self.save_task(task)
            
            print("Migração concluída com sucesso!")
            
            # Opcional: renomear o JSON antigo como backup
            os.rename(json_filename, f"{json_filename}.migrated")
            print(f"Arquivo JSON renomeado para {json_filename}.migrated")
            
        except Exception as e:
            print(f"Erro na migração: {e}")