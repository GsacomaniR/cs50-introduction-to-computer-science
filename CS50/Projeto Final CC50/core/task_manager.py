"""
Modulo responsavel pelas operacoes CRUD das tarefas
"""
from datetime import datetime
from typing import List, Dict, Optional

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title: str, priority: str = "media", due_date: str = None) -> Dict:
        """Adiciona uma nova tarefa"""
        if due_date is None:
            due_date = datetime.now().strftime("%Y-%m-%d")
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "review_count": 0,
            "last_reviewed": None
        }
        self.tasks.append(task)
        return task
    
    def get_pending_tasks(self) -> List[Dict]:
        """Retorna apenas tarefas nao concluidas"""
        return [t for t in self.tasks if not t["completed"]]
    
    def complete_task(self, task_id: int) -> bool:
        """Marca tarefa como concluida"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Remove uma tarefa"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks.pop(i)
                # Reorganizar IDs
                for j, t in enumerate(self.tasks, 1):
                    t["id"] = j
                return True
        return False
    
    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Busca tarefa pelo ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def search_tasks(self, keyword: str) -> List[Dict]:
        """Busca tarefas por palavra-chave"""
        keyword = keyword.lower()
        return [t for t in self.tasks if keyword in t["title"].lower()]