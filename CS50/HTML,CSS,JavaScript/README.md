```markdown
# Projetos CC50 - Homepage & Trivia

Este repositório contém dois projetos interativos desenvolvidos para o curso **CC50 (Introdução à Ciência da Computação)**. Ambos os projetos demonstram habilidades fundamentais em desenvolvimento web utilizando **HTML5**, **CSS3**, **JavaScript** e o framework **Bootstrap 4**.

- **TechInnovate Homepage**: Um site institucional moderno e responsivo para uma empresa de tecnologia.
- **Quiz Trivia**: Um jogo de perguntas e respostas interativo com múltipla escolha e respostas livres.

---

## Estrutura do Projeto

```
/
├── homepage/                   # Projeto Homepage (TechInnovate)
│   ├── index.html              # Página principal
│   ├── services.html           # Página de serviços
│   ├── portfolio.html          # Página de portfólio com carrossel
│   ├── contact.html            # Página de contato com formulário
│   ├── styles.css              # Estilos personalizados
│   └── script.js               # Comportamentos interativos
│
└── trivia/                     # Projeto Trivia (Quiz Interativo)
    ├── index.html              # Página única do quiz
    └── styles.css              # Estilos específicos do quiz (inline no HTML)
```

---

## Projeto 1: TechInnovate Homepage

### Descrição
Site institucional completo para uma empresa fictícia de inovação tecnológica. O projeto explora layout responsivo, componentes Bootstrap e interatividade com JavaScript puro.

### Páginas e Funcionalidades

| Página       | Funcionalidades                                                                 |
|--------------|---------------------------------------------------------------------------------|
| **Home**     | - Hero section com botão de boas-vindas (alert)<br>- Cards de serviços<br>- Contadores animados (Projetos, Clientes, etc.) |
| **Services** | - Cards descritivos com botões que exibem alerts<br>- Accordion (FAQ) com Bootstrap |
| **Portfolio**| - Carrossel (Carousel) com cases de sucesso<br>- Cards clicáveis com alert informativo |
| **Contact**  | - Formulário com validação e feedback visual<br>- Botão "Clear" para limpar campos<br>- Modal com direções (Bootstrap Modal)<br>- Saudação dinâmica baseada no horário |

### Tecnologias Utilizadas
- **HTML5** semântico
- **CSS3** (Flexbox, Grid, Animações, Media Queries)
- **JavaScript** (Eventos, manipulação do DOM, temporizadores)
- **Bootstrap 4** (Navbar, Cards, Carousel, Modal, Accordion, Grid)

### Destaques Técnicos
- Contadores animados ao carregar a página (setInterval)
- Validação de formulário com feedback visual
- Uso de data-attributes para identificar serviços
- Modal ativado via JavaScript (`$('#mapModal').modal('show')`)
- Design responsivo com mobile-first

---

## Projeto 2: Trivia Quiz

### Descrição
Quiz interativo de conhecimentos gerais com dois tipos de perguntas: múltipla escolha e resposta livre. O projeto inclui perguntas principais e um bloco extra expansível.

### Funcionalidades

#### Parte 1 - Múltipla Escolha
- Pergunta: "Qual é a capital do Brasil?"
- Opções: Rio de Janeiro, São Paulo, **Brasília**, Salvador
- **Comportamento**: Ao clicar, a opção escolhida fica verde (correta) ou vermelha (incorreta). A opção correta é destacada automaticamente em caso de erro. Os botões são desabilitados após a resposta.

#### Parte 2 - Resposta Livre
- Pergunta: "Qual é o maior planeta do Sistema Solar?"
- Campo de texto com botão "Confirmar Resposta"
- **Validação**: Case insensitive, ignora acentos e espaços extras (aceita "Júpiter", "jupiter", "júpiter")
- Feedback visual: campo com borda verde (acerto) ou vermelha (erro), além de mensagem explicativa.

#### Desafio Extra (Expansível)
- Duas perguntas adicionais dentro de um elemento `<details>`:
  1. **Múltipla escolha**: "Qual é o animal mais rápido do mundo?" (Falcão-peregrino)
  2. **Resposta livre**: "Processo pelo qual as plantas produzem alimento usando luz solar?" (Fotossíntese)

### Tecnologias Utilizadas
- **HTML5** com semântica moderna
- **CSS3** (Gradientes, Animações, Flexbox, Transições)
- **JavaScript** (Manipulação de DOM, eventos, normalização de strings, desabilitação de botões)

### Destaques Técnicos
- Função `normalizeAnswer()` para remover acentos e padronizar respostas
- Controle de estado (`isMcQuestionAnswered`) para impedir múltiplas respostas
- Animações CSS de fade-in nos feedbacks
- Atalho de teclado (Enter) para submeter respostas livres
- Função `resetQuiz()` disponível no console para reiniciar o quiz

---

## CSS Customizado - Destaques

### Homepage (styles.css)
- **Seletores variados**: tag (`body`), classe (`.feature-card`), ID (`#welcomeBtn`)
- **Efeitos**: hover com transformação (escala, sombra), transições suaves
- **Animações**: `fadeIn` para feedback do formulário
- **Gradiente linear** no hero section e nos cards do portfólio

### Trivia (estilos inline no HTML)
- Layout centralizado com gradiente de fundo (`linear-gradient`)
- Botões com efeito `transform: translateX()` ao passar o mouse
- Cores dinâmicas nos inputs corretos/incorretos (verde/vermelho)
- Animações keyframes (`fadeInUp`) para feedbacks

---

## Testes e Validação

- Navegadores suportados: Chrome, Firefox, Edge, Safari (últimas 2 versões)
- Design responsivo testado em resoluções 360px, 768px e 1920px
- Formulários validam campos obrigatórios
- Quiz trata respostas vazias e entradas inesperadas

---

## Conceitos Aplicados do CC50

| Conceito                | Aplicação nos projetos                                   |
|-------------------------|----------------------------------------------------------|
| HTML semântico          | Uso de `nav`, `section`, `footer`, `details`            |
| CSS Flexbox/Grid        | Layouts responsivos (cards, formulários, contadores)    |
| JavaScript DOM          | Manipulação de classes, estilos e conteúdo              |
| Eventos                 | `click`, `submit`, `keypress`                           |
| Temporizadores          | `setInterval` para contadores animados                  |
| Bootstrap 4             | Componentes prontos (navbar, carousel, modal, accordion)|
| Validação de formulários| Verificação de campos vazios e feedback visual           |
| Expressões regulares    | Normalização de strings no quiz (remoção de acentos)    |

---

## 👤 Autor

Gustavo Sacomani Rafael
Projeto desenvolvido como parte do curso **CC50 (Harvard/CS50 adaptado)** – uma introdução à Ciência da Computação.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo para estudos e aprimorar seu portfólio.

---
