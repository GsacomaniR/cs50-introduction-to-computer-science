"""
StudyFlow - Versão Web
"""
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.task_manager import TaskManager
from core.scheduler import SpacedRepetitionScheduler
from core.report import ReportGenerator
from storage.sqlite_database import SQLiteDatabase

app = Flask(__name__)
app.secret_key = 'studyflow-secret-key-2024'
CORS(app)

# Inicializar componentes
db = SQLiteDatabase()
task_manager = TaskManager()
scheduler = SpacedRepetitionScheduler(task_manager)
report_gen = ReportGenerator(task_manager)

def load_data():
    tasks = db.load_all_tasks()
    task_manager.tasks = tasks

load_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def list_tasks():
    pending = [t for t in task_manager.tasks if not t['completed']]
    completed = [t for t in task_manager.tasks if t['completed']]
    hoje = datetime.now().strftime("%Y-%m-%d")
    return render_template('tasks.html', pending=pending, completed=completed, now=hoje)

@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        priority = request.form.get('priority', 'media')
        due_date = request.form.get('due_date')
        
        if not title:
            flash('Título é obrigatório!', 'error')
            return redirect(url_for('add_task'))
        
        if not due_date:
            due_date = datetime.now().strftime("%Y-%m-%d")
        
        temp_task = {
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "review_count": 0,
            "last_reviewed": None,
            "next_review": None
        }
        
        task_id = db.save_task(temp_task)
        temp_task["id"] = task_id
        task_manager.tasks.append(temp_task)
        
        flash(f'Tarefa "{title}" adicionada!', 'success')
        return redirect(url_for('list_tasks'))
    
    return render_template('add_task.html')

@app.route('/task/complete/<int:task_id>')
def complete_task(task_id):
    task = task_manager.get_task_by_id(task_id)
    if task:
        task['completed'] = True
        db.update_task(task_id, task)
        flash('Tarefa concluída! 🎉', 'success')
    return redirect(url_for('list_tasks'))

@app.route('/task/delete/<int:task_id>')
def delete_task(task_id):
    task = task_manager.get_task_by_id(task_id)
    if task:
        db.delete_task(task_id)
        task_manager.tasks = [t for t in task_manager.tasks if t['id'] != task_id]
        flash('Tarefa removida!', 'success')
    return redirect(url_for('list_tasks'))

@app.route('/task/review/<int:task_id>')
def schedule_review(task_id):
    task = task_manager.get_task_by_id(task_id)
    if task:
        scheduler.schedule_review(task_id)
        db.update_task(task_id, task)
        flash('Revisão agendada!', 'success')
    return redirect(url_for('list_tasks'))

@app.route('/stats')
def stats():
    stats_data = db.get_stats()
    due_tasks = db.get_due_for_review()
    tips = report_gen.productivity_tips()
    return render_template('stats.html', stats=stats_data, due_tasks=due_tasks, tips=tips)

@app.route('/review')
def review():
    stats = db.get_stats()
    due_tasks = db.get_due_for_review()
    tasks_with_review = len([t for t in task_manager.tasks if t.get('review_count', 0) > 0])
    stats['tasks_with_review'] = tasks_with_review
    
    today = datetime.now().strftime("%Y-%m-%d")
    upcoming_reviews = [t for t in task_manager.tasks 
                        if t.get('next_review') and t['next_review'] > today and not t['completed']]
    upcoming_reviews.sort(key=lambda x: x['next_review'])
    upcoming_reviews = upcoming_reviews[:5]
    
    return render_template('review.html', stats=stats, due_tasks=due_tasks, upcoming_reviews=upcoming_reviews)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = db.search_tasks(query) if query else []
    return render_template('search.html', query=query, results=results)

@app.route('/api/web/dashboard-stats')
def dashboard_stats():
    stats = db.get_stats()
    pending_count = len([t for t in task_manager.tasks if not t['completed']])
    today = datetime.now().strftime("%Y-%m-%d")
    completed_today = len([t for t in task_manager.tasks 
                          if t['completed'] and t.get('created_at', '').startswith(today)])
    return jsonify({
        'pending': pending_count,
        'completed_today': completed_today,
        'due_review': stats['due_today']
    })

if __name__ == '__main__':
    print("="*50)
    print("🌐 StudyFlow - Versão Web")
    print("="*50)
    print("🚀 Servidor: http://localhost:5001")
    print("="*50)
    app.run(debug=True, host='localhost', port=5001)