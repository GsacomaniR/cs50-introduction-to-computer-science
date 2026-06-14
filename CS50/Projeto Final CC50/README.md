```markdown
# StudyFlow - Sistema Inteligente de Organização de Estudos

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)
![SQLite](https://img.shields.io/badge/sqlite-3-blue.svg)
![License](https://img.shields.io/badge/license-MIT-red.svg)

> Um sistema completo de gerenciamento de estudos com algoritmo de **revisão espaçada** baseado no método científico de Hermann Ebbinghaus.

## Sobre o Projeto

StudyFlow é uma aplicação full-stack desenvolvida como projeto final do curso **CS50 - Introduction to Computer Science** de Harvard. O sistema resolve um problema real enfrentado por estudantes: a dificuldade de lembrar o que foi estudado ao longo do tempo.

**O problema:** Após 24 horas, esquecemos cerca de 50% do que estudamos.

**A solução:** A revisão espaçada - algoritmo que agenda revisões em intervalos crescentes (1, 3, 7, 14, 30 dias) para fixar o conteúdo na memória de longo prazo.

## Funcionalidades

### Gestão de Tarefas
- Criar, ler, atualizar e deletar tarefas
- Definir prioridade (Alta/Média/Baixa)
- Estabelecer datas limites
- Busca por palavras-chave

### Revisão Espaçada
- Agendamento automático de revisões
- Alertas de tarefas pendentes
- Próximas revisões programadas
- Baseado no método científico de Ebbinghaus

### Dashboard e Estatísticas
- Taxa de conclusão de tarefas
- Distribuição por prioridade
- Tarefas concluídas no dia
- Revisões pendentes

### Interfaces
- **Web App** (Recomendado) - Interface moderna com design Glassmorphism
- **CLI** - Terminal colorido com experiência interativa
- **API REST** - Endpoints para integração com outros sistemas

## Arquitetura do Projeto

```
studyflow/
├── core/
│   ├── task_manager.py
│   ├── scheduler.py
│   └── report.py
├── storage/
|   ├── task.db
│   └── sqlite_database.py
├── api/
│   ├── server.py
│   └── client.py
├── web/
│   ├── app.py
|   ├── static
|   |   ├── script.js
|   |   └── styles.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── tasks.html
│       ├── add_task.html
│       ├── review.html
│       ├── stats.html
│       └── search.html
├── tests/
│   └── test_tasks.py
├── main.py
├── .gitignore
└── requirements.txt
```

## Como Executar

### Pré-requisitos
- Python 3.13 ou superior

### Executando as Interfaces

#### Web App (Recomendado para uso diário)
```bash
python web/app.py
```
Acesse no navegador: `http://localhost:5001`

**Páginas disponíveis:**
- `/` - Dashboard principal
- `/tasks` - Lista de tarefas
- `/task/add` - Criar nova tarefa
- `/review` - Sistema de revisão espaçada
- `/stats` - Estatísticas de produtividade
- `/search` - Busca de tarefas

#### CLI (Para usuários de terminal)
```bash
python main.py
```

#### API REST (Para desenvolvedores)
```bash
python api/server.py
```

## Como funciona a Revisão Espaçada?

O algoritmo agenda revisões nos seguintes intervalos:

| Revisão | Intervalo |            Objetivo             |
|---------|-----------|---------------------------------|
|   1ª    |   1 dia   | Impedir o esquecimento inicial  |
|   2ª    |  3 dias   |       Reforçar a memória        |
|   3ª    |  7 dias   |    Consolidar o aprendizado     |
|   4ª    |  14 dias  | Fixar na memória de médio prazo |
|   5ª    |  30 dias  | Tornar o conhecimento duradouro |

**Resultado:** Estudos mostram que este método pode aumentar a retenção de informações em até **70%** comparado ao estudo tradicional.

## Tecnologias Utilizadas

|     Camada     |  Tecnologia  |             Finalidade             |
|----------------|--------------|------------------------------------|
|    Backend     | Python 3.13  |    Lógica principal do sistema     |
| Framework Web  |    Flask     |        Aplicação web e API         |
| Banco de Dados |    SQLite    |       Persistência de dados        |
| Interface CLI  |   Colorama   |       Cores e UX no terminal       |
|    Frontend    |  HTML5/CSS3  | Interface visual com Glassmorphism |
|  Estilização   | Font Awesome |          Ícones modernos           |

## Design e UX

- **Glassmorphism:** Fundos transparentes com efeito blur
- **Animações:** Transições suaves e feedback visual
- **Responsivo:** Adapta-se a diferentes tamanhos de tela
- **Acessibilidade:** Alto contraste para melhor legibilidade

## Licença

Este projeto está sob a licença MIT.

## Autor

**Gustavo Sacomani Rafel**
- GitHub: [@GsacomaniR](https://github.com/GsacomaniR)
- LinkedIn: [Gustavo Sacomani Rafael](https://www.linkedin.com/in/gustavo-sacomani-rafael-6941823b8/)

## Agradecimentos

- **CS50 Harvard** - Pelo curso e inspiração
- **Hermann Ebbinghaus** - Pela pesquisa sobre memória e esquecimento
- **Comunidade Open Source** - Pelas bibliotecas e ferramentas

## Suporte

Caso encontre algum problema ou tenha sugestões:
- Abra uma issue no GitHub
- Envie um email para g.sacomani.r@gmail.com

---

**Se este projeto te ajudou, considere dar uma estrela no GitHub!**
```