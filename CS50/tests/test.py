"""
Testes unitários para o TaskManager
"""
import unittest
import sys
import os

# Adicionar diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Configuração antes de cada teste"""
        self.manager = TaskManager()
    
    def test_add_task(self):
        """Testa adição de tarefa"""
        task = self.manager.add_task("Estudar Python")
        self.assertEqual(task["title"], "Estudar Python")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.tasks), 1)
    
    def test_complete_task(self):
        """Testa conclusão de tarefa"""
        task = self.manager.add_task("Fazer exercícios")
        result = self.manager.complete_task(1)
        self.assertTrue(result)
        self.assertTrue(self.manager.tasks[0]["completed"])
    
    def test_delete_task(self):
        """Testa remoção de tarefa"""
        self.manager.add_task("Tarefa 1")
        self.manager.add_task("Tarefa 2")
        result = self.manager.delete_task(1)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["title"], "Tarefa 2")
    
    def test_search_tasks(self):
        """Testa busca de tarefas"""
        self.manager.add_task("Estudar Algoritmos")
        self.manager.add_task("Praticar Python")
        results = self.manager.search_tasks("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Praticar Python")

if __name__ == "__main__":
    unittest.main()
