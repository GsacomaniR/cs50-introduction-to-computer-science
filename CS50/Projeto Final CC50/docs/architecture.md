# Arquitetura do StudyFlow

## Decisões de Design

### 1. Separação em Camadas
- **Core**: Lógica de negócio pura (sem dependências externas)
- **Storage**: Persistência de dados (fácil trocar para banco de dados)
- **UI**: Interface do usuário (fácil trocar para web)

### 2. Por que JSON?
- Simples para MVP
- Sem dependências externas
- Fácil debugar (arquivo legível)

### 3. Algoritmo de Revisão Espaçada
Baseado em pesquisas de Hermann Ebbinghaus:
- Intervalos dobrados a cada revisão
- Máximo de 30 dias entre revisões
- Prioriza tarefas recém-aprendidas

### 4. Tratamento de Erros
- Try/except em operações de arquivo
- Validação de entrada do usuário
- Mensagens amigáveis em vez de crashes

## Fluxo de Dados
Usuário → main.py → TaskManager → Database → tasks.json
↓
Scheduler (revisões)
↓
Report (estatísticas)
