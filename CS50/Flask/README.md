```markdown
# CC50 - Projetos Flask: Birthday Tracker & Finance Manager

Este repositório contém dois projetos desenvolvidos como parte do curso CC50 (a versão em português do CS50 de Harvard), focando em aplicações web com Flask, bancos de dados SQL e autenticação de usuários.

## 📁 Estrutura do Projeto

```
cc50-flask-projects/
├── birthdays/            # Gerenciador de aniversários
│   ├── app.py            # Aplicação principal
│   ├── birthdays.db      # Banco de dados SQLite
│   ├── static/           # Arquivos estáticos (CSS)
│   └── templates/        # Templates HTML
└── finance/              # Gerenciador de carteira de ações
    ├── app.py            # Aplicação principal
    ├── finance.db        # Banco de dados SQLite
    ├── helpers.py        # Funções auxiliares
    ├── requirements.txt  # Dependências do projeto
    ├── static/           # Arquivos estáticos (CSS, imagens)
    └── templates/        # Templates HTML
```

## Birthday Tracker

### Sobre o Projeto
Uma aplicação web para gerenciar aniversários de contatos. Permite adicionar, editar e remover aniversários, exibindo-os em uma tabela organizada por mês e dia.

### Funcionalidades
- **Adicionar aniversários** - Nome, mês e dia
- **Listar aniversários** - Tabela ordenada por data
- **Editar aniversários** - Formulário dinâmico inline
- **Excluir aniversários** - Com confirmação
- **Responsividade** - Layout adaptável para mobile

### Tecnologias Utilizadas
- **Backend:** Flask (Python)
- **Banco de Dados:** SQLite com CS50 Library
- **Frontend:** HTML5, CSS3 (design personalizado)
- **JavaScript:** Interações dinâmicas (edição inline)

### Estrutura do Banco de Dados
```sql
CREATE TABLE birthdays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
);

### Personalização CSS
O projeto possui um design moderno com:
- Cores inspiradas no Google Blue (#1a73e8)
- Cards com sombras suaves
- Botões com hover effects
- Tabela responsiva com zebra striping
- Formulário de edição que aparece dinamicamente

---

## Finance Manager (C$50 Finance)

### Sobre o Projeto
Uma aplicação completa para gerenciar uma carteira de investimentos simulada. Usuários podem comprar e vender ações, visualizar seu portfólio e histórico de transações.

### Funcionalidades
- **Sistema de Autenticação** - Registro e login seguros
- **Cotações em Tempo Real** - API financeira integrada
- **Comprar/Vender Ações** - Validação de saldo e quantidades
- **Portfólio Dinâmico** - Mostra posições atuais e valor total
- **Histórico Completo** - Todas as transações com timestamps
- **Adicionar Saldo** - Recarga da conta simulada
- **Formatação Monetária** - Valores em USD (ex: $1,234.56)

### Tecnologias Utilizadas
- **Backend:** Flask, Flask-Session
- **Banco de Dados:** SQLite com CS50 Library
- **Segurança:** Werkzeug (password hashing)
- **Frontend:** Bootstrap 5.3, CSS customizado
- **API Externa:** finance.cs50.io (cotações)
- **Validação:** HTML5 e server-side

### Estrutura do Banco de Dados
```sql
-- Tabela de usuários
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC DEFAULT 10000.00
);

-- Tabela de transações
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    transaction_type TEXT CHECK(transaction_type IN ('buy', 'sell')),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

### Demonstração de Uso

#### 1. Registro e Login
- Crie uma conta com username e senha
- Senhas são armazenadas com hash seguro
- Login automático após registro

#### 2. Consultar Cotação (/quote)
- Digite o símbolo da ação (ex: AAPL, GOOGL, TSLA)
- Visualize nome da empresa e preço atual

#### 3. Comprar Ações (/buy)
- Informe símbolo e quantidade de ações
- Sistema verifica saldo disponível
- Atualiza portfólio e registra transação

#### 4. Gerenciar Portfólio (/)
- Visualize todas as suas posições
- Preços atualizados em tempo real
- Calcular valor total (ações + saldo)

#### 5. Vender Ações (/sell)
- Selecione ação do seu portfólio
- Informe quantidade (não pode exceder possuída)
- Saldo é creditado automaticamente

### Segurança Implementada
- **@login_required decorator** - Rotas protegidas
- **Session-based authentication** - Usando Flask-Session
- **Password hashing** - Werkzeug generate/check password hash
- **SQL Injection prevention** - CS50 Library com placeholders
- **Input validation** - Server-side para todos os formulários
- **Cache control headers** - Evita cache de páginas autenticadas

### Funções Auxiliares (helpers.py)

#### `apology(message, code)`
Retorna mensagem de erro com meme personalizado

#### `login_required(f)`
Decorator para proteger rotas que exigem autenticação

#### `lookup(symbol)`
Consulta API externa para obter cotação atual da ação

#### `usd(value)`
Formata valores numéricos como moeda USD

### Estilização com Bootstrap
O projeto utiliza Bootstrap 5.3 com:
- Navbar responsiva
- Sistema de grid flexível
- Componentes estilizados (cards, forms, tables)
- Alertas para flash messages
- Validação de formulários via HTML5
- Tema customizado com cores do CS50

### API de Cotações
- **Endpoint:** `https://finance.cs50.io/quote?symbol={symbol}`
- **Resposta:** JSON com companyName, latestPrice, etc.
- **Tratamento de erros:** Try/except para falhas de rede/dados

## Conceitos Aprendidos (CC50)

### Flask & Web Development
- Rotas com métodos GET/POST
- Templates com Jinja2 (herança, condicionais, loops)
- Manipulação de formulários
- Sessions e cookies
- Flash messages
- Decorators personalizados

### Banco de Dados SQL
- SQLite com CS50 Library
- Consultas parametrizadas (segurança)
- Relacionamentos (transações -> usuários)
- SUM, GROUP BY, HAVING
- Agregações para portfólio

### Segurança Web
- Password hashing (bcrypt algorithm)
- Session management
- Input sanitization
- XSS prevention (Jinja2 auto-escaping)

### Frontend & UI/UX
- Responsive design (Media Queries)
- CSS Flexbox/Grid
- JavaScript interativo (edição inline)
- Bootstrap components
- Formulários acessíveis
- Feedback visual (hover, active states)

### Integração com API
- Requisições HTTP externas
- Tratamento de JSON
- Error handling (timeout, parse errors)
  
### Finance Manager
```
cs50
Flask
Flask-Session
pytz
requests
```

## Licença

Este projeto é parte do curso CC50 (CS50's Introduction to Computer Science) e é disponibilizado apenas para fins educacionais.

## 👨‍💻 Autor

Gustavo Sacomani Rafael
Desenvolvido como parte do currículo do **CC50** - versão em português do curso CS50 de Harvard.

---

**Nota:** Estes projetos foram desenvolvidos para aprendizado dos conceitos fundamentais de desenvolvimento web full-stack com Python/Flask, banco de dados SQL e boas práticas de segurança.
```
