"""
Sistema de revisão espaçada baseado no método Ebbinghaus
"""
from datetime import datetime, timedelta
from typing import List, Dict

class SpacedRepetitionScheduler:
    def __init__(self, task_manager):
        self.task_manager = task_manager
    
    def schedule_review(self, task_id: int) -> Dict:
        """Programa proxima revisao"""
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            return None
        
        intervals = [1, 3, 7, 14, 30]
        review_count = task.get("review_count", 0)
        
        if review_count >= len(intervals):
            next_interval = intervals[-1]
        else:
            next_interval = intervals[review_count]
        
        next_review = datetime.now() + timedelta(days=next_interval)
        task["next_review"] = next_review.strftime("%Y-%m-%d")
        task["review_count"] = review_count + 1
        task["last_reviewed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return task
    
    def get_tasks_due_for_review(self) -> List[Dict]:
        """Retorna tarefas que precisam ser revisadas hoje"""
        today = datetime.now().strftime("%Y-%m-%d")
        due_tasks = []
        
        for task in self.task_manager.tasks:
            if task.get("next_review") and task["next_review"] <= today:
                if not task["completed"]:
                    due_tasks.append(task)
        return due_tasks
    
    def get_review_stats(self) -> Dict:
        """Estatisticas do sistema de revisao"""
        total = len(self.task_manager.tasks)
        with_review = sum(1 for t in self.task_manager.tasks if t.get("review_count", 0) > 0)
        due_today = len(self.get_tasks_due_for_review())
        
        return {
            "total_tasks": total,
            "tasks_with_review": with_review,
            "due_today": due_today,
            "completion_rate": self._calculate_completion_rate()
        }
    
    def _calculate_completion_rate(self) -> float:
        """Calcula taxa de conclusao"""
        if not self.task_manager.tasks:
            return 0.0
        completed = sum(1 for t in self.task_manager.tasks if t["completed"])
        return (completed / len(self.task_manager.tasks)) * 100