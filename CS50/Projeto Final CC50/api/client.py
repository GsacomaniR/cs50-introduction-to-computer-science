"""
Cliente para consumir a API do StudyFlow
"""
import requests
from typing import List, Dict, Optional

class StudyFlowAPIClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.timeout = 10
    
    def _request(self, method, endpoint, data=None):
        """Faz requisição HTTP para a API"""
        url = f"{self.base_url}{endpoint}"
        headers = {'Content-Type': 'application/json'}
        
        try:
            if method == 'GET':
                response = requests.get(url, timeout=self.timeout)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=self.timeout)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=self.timeout)
            elif method == 'DELETE':
                response = requests.delete(url, timeout=self.timeout)
            else:
                return {'success': False, 'error': f'Método {method} não suportado'}
            
            if response.status_code in [200, 201]:
                return response.json()
            else:
                return {'success': False, 'error': f'HTTP {response.status_code}'}
                
        except requests.exceptions.ConnectionError:
            return {'success': False, 'error': 'API não está rodando. Execute api/server.py primeiro'}
        except requests.exceptions.Timeout:
            return {'success': False, 'error': 'Timeout na requisição'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def check_health(self):
        """Verifica se API está online"""
        result = self._request('GET', '/api/health')
        return result.get('status') == 'ok'
    
    def get_tasks(self, completed=None, priority=None):
        """Lista tarefas"""
        params = []
        if completed is not None:
            params.append(f"completed={completed}")
        if priority:
            params.append(f"priority={priority}")
        
        endpoint = "/api/tasks"
        if params:
            endpoint += "?" + "&".join(params)
        
        return self._request('GET', endpoint)
    
    def get_task(self, task_id):
        """Busca tarefa específica"""
        return self._request('GET', f"/api/tasks/{task_id}")
    
    def create_task(self, title, priority, due_date):
        """Cria nova tarefa"""
        data = {
            'title': title,
            'priority': priority,
            'due_date': due_date
        }
        return self._request('POST', "/api/tasks", data)
    
    def update_task(self, task_id, **kwargs):
        """Atualiza tarefa"""
        return self._request('PUT', f"/api/tasks/{task_id}", kwargs)
    
    def delete_task(self, task_id):
        """Remove tarefa"""
        return self._request('DELETE', f"/api/tasks/{task_id}")
    
    def get_stats(self):
        """Obtém estatísticas"""
        return self._request('GET', "/api/stats")
    
    def sync_tasks(self, tasks):
        """Sincroniza múltiplas tarefas"""
        data = {'tasks': tasks}
        return self._request('POST', "/api/sync", data)
