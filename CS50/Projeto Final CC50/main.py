"""
StudyFlow - CLI Study Organizer com UX melhorado
"""
from core.task_manager import TaskManager
from core.scheduler import SpacedRepetitionScheduler
from core.report import ReportGenerator
from storage.sqlite_database import SQLiteDatabase
from api.client import StudyFlowAPIClient
from datetime import datetime
from colorama import init, Fore, Back, Style, just_fix_windows_console
import os

# Inicializar Colorama para Windows
init(autoreset=True)
just_fix_windows_console()

class StudyFlowApp:
    def __init__(self):
        self.db = SQLiteDatabase()
        self.task_manager = TaskManager()
        self.scheduler = SpacedRepetitionScheduler(self.task_manager)
        self.report_gen = ReportGenerator(self.task_manager)
        self.api_client = StudyFlowAPIClient()
        self.load_data()
    
    def clear_screen(self):
        """Limpa a tela"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, text):
        """Imprime cabeçalho estilizado"""
        print(f"\n{Back.CYAN}{Fore.BLACK}{'='*60}{Style.RESET_ALL}")
        print(f"{Back.CYAN}{Fore.BLACK}{text.center(60)}{Style.RESET_ALL}")
        print(f"{Back.CYAN}{Fore.BLACK}{'='*60}{Style.RESET_ALL}")
    
    def print_success(self, text):
        """Imprime mensagem de sucesso"""
        print(f"{Fore.GREEN}✅ {text}{Style.RESET_ALL}")
    
    def print_error(self, text):
        """Imprime mensagem de erro"""
        print(f"{Fore.RED}❌ {text}{Style.RESET_ALL}")
    
    def print_warning(self, text):
        """Imprime mensagem de aviso"""
        print(f"{Fore.YELLOW}⚠️  {text}{Style.RESET_ALL}")
    
    def print_info(self, text):
        """Imprime mensagem informativa"""
        print(f"{Fore.CYAN}ℹ️  {text}{Style.RESET_ALL}")
    
    def load_data(self):
        """Carrega dados do SQLite"""
        tasks = self.db.load_all_tasks()
        self.task_manager.tasks = tasks
    
    def save_data(self):
        """Salva dados no SQLite"""
        for task in self.task_manager.tasks:
            self.db.update_task(task['id'], task)
    
    def display_menu(self):
        """Exibe menu principal estilizado"""
        self.clear_screen()
        
        # Logo
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}")
        print("  ╔══════════════════════════════════════════════════════╗")
        print("  ║                                                      ║")
        print("  ║     📚  S T U D Y F L O W  🧠                        ║")
        print("  ║     Seu organizador de estudos com ciência           ║")
        print("  ║                                                      ║")
        print("  ╚══════════════════════════════════════════════════════╝")
        print(f"{Style.RESET_ALL}")
        
        # Estatísticas rápidas
        stats = self.db.get_stats()
        pending_count = len([t for t in self.task_manager.tasks if not t['completed']])
        due_count = stats['due_today']
        
        print(f"\n{Fore.CYAN}📊 Resumo:{Style.RESET_ALL}")
        print(f"   • Tarefas pendentes: {Fore.YELLOW}{pending_count}{Style.RESET_ALL}")
        print(f"   • Taxa de conclusão: {Fore.GREEN}{stats['completion_rate']:.1f}%{Style.RESET_ALL}")
        if due_count > 0:
            print(f"   • {Fore.RED}⚠️  {due_count} tarefa(s) precisam de revisão hoje!{Style.RESET_ALL}")
        
        # Menu
        print(f"\n{Fore.CYAN}{Style.BRIGHT}════════════════════════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{Style.BRIGHT}                         M E N U{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}════════════════════════════════════════════════════════{Style.RESET_ALL}")
        
        menu_items = [
            ("1", "➕ Adicionar tarefa", Fore.GREEN),
            ("2", "📋 Listar tarefas", Fore.CYAN),
            ("3", "✅ Completar tarefa", Fore.GREEN),
            ("4", "🗑️  Remover tarefa", Fore.RED),
            ("5", "🔍 Buscar tarefas", Fore.BLUE),
            ("6", "🧠 Revisão espaçada", Fore.MAGENTA),
            ("7", "📊 Relatório semanal", Fore.YELLOW),
            ("8", "💡 Dicas de produtividade", Fore.CYAN),
            ("9", "💾 Backup manual", Fore.WHITE),
            ("10", "🌐 Sincronizar com API", Fore.BLUE),
            ("0", "🚪 Sair", Fore.RED),
        ]
        
        for num, text, color in menu_items:
            print(f"   {color}{num}{Style.RESET_ALL}  {text}")
        
        print(f"{Fore.CYAN}{Style.BRIGHT}════════════════════════════════════════════════════════{Style.RESET_ALL}")
    
    def add_task_ui(self):
        """Interface para adicionar tarefa com UX melhorado"""
        self.clear_screen()
        self.print_header("➕ ADICIONAR NOVA TAREFA")
        
        print(f"\n{Fore.CYAN}Digite os dados da tarefa:{Style.RESET_ALL}")
        
        title = input(f"{Fore.WHITE}📝 Título: {Style.RESET_ALL}").strip()
        if not title:
            self.print_error("Título não pode estar vazio!")
            input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.YELLOW}Prioridades disponíveis:{Style.RESET_ALL}")
        print(f"  {Fore.RED}🔴 alta{Style.RESET_ALL} - Urgente e importante")
        print(f"  {Fore.YELLOW}🟡 média{Style.RESET_ALL} - Importante mas não urgente")
        print(f"  {Fore.GREEN}🟢 baixa{Style.RESET_ALL} - Pode esperar")
        
        priority = input(f"{Fore.WHITE}🎯 Prioridade (padrão: média): {Style.RESET_ALL}").strip().lower()
        if priority not in ['alta', 'média', 'baixa', 'media', '']:
            self.print_warning("Prioridade inválida! Usando 'média'")
            priority = 'media'
        elif priority == 'média':
            priority = 'media'
        elif priority == '':
            priority = 'media'
        
        due_date = input(f"{Fore.WHITE}📅 Data limite (AAAA-MM-DD ou Enter para hoje): {Style.RESET_ALL}").strip()
        if not due_date:
            due_date = datetime.now().strftime("%Y-%m-%d")
        
        # Criar tarefa
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
        
        task_id = self.db.save_task(temp_task)
        temp_task["id"] = task_id
        self.task_manager.tasks.append(temp_task)
        
        self.print_success(f"Tarefa '{title}' adicionada com ID: {task_id}")
        input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
    
    def list_tasks_ui(self):
        """Lista tarefas com cores e formatação"""
        self.clear_screen()
        self.print_header("📋 MINHAS TAREFAS")
        
        tasks = self.task_manager.tasks
        if not tasks:
            self.print_warning("Nenhuma tarefa encontrada!")
            input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
            return
        
        pending = [t for t in tasks if not t["completed"]]
        completed = [t for t in tasks if t["completed"]]
        
        # Tarefas Pendentes
        if pending:
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}⏳ TAREFAS PENDENTES ({len(pending)}){Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*55}{Style.RESET_ALL}")
            
            for task in pending:
                # Cor da prioridade
                if task["priority"] == "alta":
                    priority_color = Fore.RED
                    priority_icon = "🔴"
                elif task["priority"] == "media":
                    priority_color = Fore.YELLOW
                    priority_icon = "🟡"
                else:
                    priority_color = Fore.GREEN
                    priority_icon = "🟢"
                
                print(f"\n{Fore.CYAN}[{task['id']}]{Style.RESET_ALL} {priority_color}{priority_icon} {task['title']}{Style.RESET_ALL}")
                print(f"   {Fore.WHITE}📅 Vence: {task['due_date']}{Style.RESET_ALL}")
                
                # Verificar se está atrasada
                if task['due_date'] < datetime.now().strftime("%Y-%m-%d"):
                    print(f"   {Fore.RED}⚠️  ATRASADA!{Style.RESET_ALL}")
                
                if task.get("next_review"):
                    print(f"   {Fore.MAGENTA}🧠 Próxima revisão: {task['next_review']}{Style.RESET_ALL}")
        
        # Tarefas Concluídas
        if completed:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ TAREFAS CONCLUÍDAS ({len(completed)}){Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*55}{Style.RESET_ALL}")
            
            for task in completed:
                print(f"\n{Fore.GREEN}✓ [{task['id']}] {task['title']}{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
    
    def complete_task_ui(self):
        """Marca tarefa como concluída com UX melhorado"""
        self.clear_screen()
        self.print_header("✅ COMPLETAR TAREFA")
        
        try:
            # Mostrar tarefas pendentes
            pending = [t for t in self.task_manager.tasks if not t['completed']]
            if not pending:
                self.print_warning("Não há tarefas pendentes para completar!")
                input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
                return
            
            print(f"\n{Fore.YELLOW}Tarefas pendentes:{Style.RESET_ALL}")
            for task in pending:
                print(f"  {Fore.CYAN}[{task['id']}]{Style.RESET_ALL} {task['title']}")
            
            task_id = int(input(f"\n{Fore.WHITE}ID da tarefa concluída: {Style.RESET_ALL}"))
            task = self.task_manager.get_task_by_id(task_id)
            
            if not task:
                self.print_error("Tarefa não encontrada!")
                input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
                return
            
            task["completed"] = True
            if self.db.update_task(task_id, task):
                self.print_success(f"Parabéns! Você completou '{task['title']}'! 🎉")
                
                # Perguntar sobre revisão
                answer = input(f"\n{Fore.CYAN}Agendar revisão espaçada? (s/n): {Style.RESET_ALL}").lower()
                if answer == 's':
                    self.scheduler.schedule_review(task_id)
                    self.db.update_task(task_id, task)
                    self.print_success("Revisão agendada com sucesso!")
            else:
                self.print_error("Erro ao atualizar tarefa!")
                
        except ValueError:
            self.print_error("ID inválido!")
        
        input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
    
    def spaced_repetition_ui(self):
        """Interface de revisão espaçada com UX melhorado"""
        self.clear_screen()
        self.print_header("🧠 REVISÃO ESPAÇADA")
        
        stats = self.db.get_stats()
        
        print(f"\n{Fore.CYAN}📈 Estatísticas do sistema:{Style.RESET_ALL}")
        print(f"   • Total de tarefas: {Fore.WHITE}{stats['total_tasks']}{Style.RESET_ALL}")
        print(f"   • Concluídas: {Fore.GREEN}{stats['completed_tasks']}{Style.RESET_ALL}")
        print(f"   • Taxa de conclusão: {Fore.YELLOW}{stats['completion_rate']:.1f}%{Style.RESET_ALL}")
        print(f"   • Para revisar hoje: {Fore.RED if stats['due_today'] > 0 else Fore.GREEN}{stats['due_today']}{Style.RESET_ALL}")
        
        due_tasks = self.db.get_due_for_review()
        if due_tasks:
            print(f"\n{Fore.RED}{Style.BRIGHT}⚠️  Tarefas que precisam de revisão HOJE:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*50}{Style.RESET_ALL}")
            
            for task in due_tasks:
                last = task.get('last_reviewed') or 'nunca'
                print(f"\n{Fore.YELLOW}📌 {task['title']}{Style.RESET_ALL}")
                print(f"   Última revisão: {last}")
            
            answer = input(f"\n{Fore.CYAN}Deseja revisar agora? (s/n): {Style.RESET_ALL}").lower()
            if answer == 's':
                for task in due_tasks:
                    print(f"\n{Fore.MAGENTA}Revisando: {task['title']}{Style.RESET_ALL}")
                    input(f"{Fore.CYAN}Pressione Enter quando terminar a revisão...{Style.RESET_ALL}")
                    self.scheduler.schedule_review(task['id'])
                    self.db.update_task(task['id'], task)
                    self.print_success(f"Revisão de '{task['title']}' concluída!")
                
                self.print_success("Todas as revisões concluídas!")
        else:
            print(f"\n{Fore.GREEN}🎉 Nenhuma tarefa para revisar hoje! Continue assim!{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
    
    # ... (outros métodos mantidos semelhantes com cores)
    
    def run(self):
        """Loop principal do aplicativo"""
        self.clear_screen()
        print(f"{Fore.MAGENTA}{Style.BRIGHT}")
        print("  ╔══════════════════════════════════════════════════════════╗")
        print("  ║                                                          ║")
        print("  ║     🌟 BEM-VINDO AO STUDYFLOW 2.0! 🌟                    ║")
        print("  ║     Sua jornada de estudos com inteligência e estilo     ║")
        print("  ║                                                          ║")
        print("  ╚══════════════════════════════════════════════════════════╝")
        print(f"{Style.RESET_ALL}")
        
        if self.api_client.check_health():
            self.print_success("API detectada! Sincronização disponível (opção 10)")
        else:
            self.print_warning("API não detectada. Execute 'python api/server.py' para sincronização")
        
        input(f"\n{Fore.CYAN}Pressione Enter para começar...{Style.RESET_ALL}")
        
        while True:
            self.display_menu()
            choice = input(f"\n{Fore.YELLOW}🎯 Escolha uma opção: {Style.RESET_ALL}").strip()
            
            if choice == '1':
                self.add_task_ui()
            elif choice == '2':
                self.list_tasks_ui()
            elif choice == '3':
                self.complete_task_ui()
            elif choice == '4':
                self.delete_task_ui()
            elif choice == '5':
                self.search_tasks_ui()
            elif choice == '6':
                self.spaced_repetition_ui()
            elif choice == '7':
                self.weekly_report_ui()
            elif choice == '8':
                self.productivity_tips_ui()
            elif choice == '9':
                self.backup_ui()
            elif choice == '10':
                self.sync_with_api()
            elif choice == '0':
                self.clear_screen()
                print(f"\n{Fore.GREEN}{Style.BRIGHT}")
                print("  ╔══════════════════════════════════════════════════════════╗")
                print("  ║                                                          ║")
                print("  ║     👋 ATÉ LOGO! Continue estudando com consistência!    ║")
                print("  ║                                                          ║")
                print("  ║     📚 Estude hoje, colha os frutos amanhã! 🧠           ║")
                print("  ║                                                          ║")
                print("  ╚══════════════════════════════════════════════════════════╝")
                print(f"{Style.RESET_ALL}")
                break
            else:
                self.print_error("Opção inválida!")
                input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")

if __name__ == "__main__":
    app = StudyFlowApp()
    app.run()