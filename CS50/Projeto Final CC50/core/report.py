"""
Geração de relatórios e estatísticas de produtividade
"""
from datetime import datetime, timedelta
from collections import Counter
from typing import Dict, List

class ReportGenerator:
    def __init__(self, task_manager):
        self.task_manager = task_manager
    
    def weekly_report(self) -> str:
        """Gera relatorio da semana"""
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        
        # Filtrar tarefas da ultima semana
        recent_tasks = []
        for task in self.task_manager.tasks:
            try:
                created = datetime.strptime(task["created_at"], "%Y-%m-%d %H:%M:%S")
                if created >= week_ago:
                    recent_tasks.append(task)
            except:
                # Se der erro na data, ignora a tarefa
                pass
        
        total = len(recent_tasks)
        completed = sum(1 for t in recent_tasks if t["completed"])
        
        # Prioridades mais comuns
        priorities = [t["priority"] for t in recent_tasks]
        priority_counts = Counter(priorities)
        
        avg_daily = total/7 if total > 0 else 0
        
        report = f"""
{'='*50}
RELATORIO SEMANAL DE ESTUDOS
{'='*50}

VISAO GERAL:
• Tarefas criadas: {total}
• Tarefas concluidas: {completed}
• Taxa de conclusao: {(completed/total*100) if total > 0 else 0:.1f}%

POR PRIORIDADE:
• Alta: {priority_counts.get('alta', 0)}
• Media: {priority_counts.get('media', 0)}
• Baixa: {priority_counts.get('baixa', 0)}

PRODUTIVIDADE:
• Media diaria: {avg_daily:.1f} tarefas/dia
{'='*50}
"""
        return report
    
    def productivity_tips(self) -> List[str]:
        """Sugestoes baseadas no comportamento"""
        tips = []
        pending = len(self.task_manager.get_pending_tasks())
        
        if pending > 10:
            tips.append("Muitas tarefas pendentes! Tente dividir em subtarefas menores.")
        
        # Verificar tarefas de alta prioridade atrasadas
        high_priority_overdue = 0
        for task in self.task_manager.get_pending_tasks():
            try:
                if task["priority"] == "alta" and task["due_date"] < datetime.now().strftime("%Y-%m-%d"):
                    high_priority_overdue += 1
            except:
                pass
        
        if high_priority_overdue > 0:
            tips.append(f"Voce tem {high_priority_overdue} tarefa(s) de alta prioridade atrasada(s)!")
        
        if not tips:
            tips.append("Otimo trabalho! Mantenha o ritmo consistente.")
        
        return tips