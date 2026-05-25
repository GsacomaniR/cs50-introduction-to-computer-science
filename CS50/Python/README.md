```markdown
# CC50 - Introdução à Ciência da Computação (Harvard/CS50)

Este repositório contém as soluções dos problemas da semana 6 do curso CC50 (versão em português do CS50), implementadas em Python.

## Problemas Implementados

### 1. Readability (`readability.py`)
Calcula o nível de legibilidade de um texto usando o índice de Coleman-Liau.

**Funcionalidades:**
- Conta letras, palavras e frases no texto
- Calcula o índice de legibilidade
- Retorna o nível escolar americano correspondente

**Como usar:**
```bash
python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

### 2. Mario (`mario.py`)
Constrói uma pirâmide de blocos (#) similar ao jogo Super Mario Bros.

**Funcionalidades:**
- Solicita uma altura entre 1 e 8
- Imprime uma pirâmide alinhada à direita

**Como usar:**
```bash
python mario.py
Height: 5
    #
   ##
  ###
 ####
#####
```

### 3. Mario 2 (`mario2.py`)
Constrói duas pirâmides lado a lado (versão mais avançada).

**Funcionalidades:**
- Altura entre 1 e 8
- Duas pirâmides com espaço entre elas

**Como usar:**
```bash
python mario2.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

### 4. Hello (`hello.py`)
Programa simples de saudação.

**Como usar:**
```bash
python hello.py
What is your name? Maria
hello, Maria
```

### 5. Credit (`credit.py`)
Valida números de cartão de crédito usando o algoritmo de Luhn.

**Funcionalidades:**
- Valida números de cartão (AMEX, MASTERCARD, VISA)
- Implementa o algoritmo de Luhn
- Identifica a bandeira do cartão

**Como usar:**
```bash
python credit.py
Number: 4003600000000014
VISA
```

### 6. Cash (`cash.py`)
Calcula o número mínimo de moedas para dar o troco.

**Funcionalidades:**
- Usa moedas de 25¢, 10¢, 5¢ e 1¢
- Algoritmo guloso (greedy)
- Trata valores com ponto flutuante

**Como usar:**
```bash
python cash.py
Change owed: 0.41
4
```

### 7. DNA (`dna.py`)
Identifica a qual pessoa pertence uma sequência de DNA baseada em STRs (Short Tandem Repeats).

**Funcionalidades:**
- Lê banco de dados CSV com perfis de DNA
- Analisa sequência de DNA
- Encontra correspondência usando STRs

**Como usar:**
```bash
python dna.py databases/small.csv sequences/1.txt
Bob
```

### 8. Lab 6 - Tournament (`lab6/tournament.py`)
Simula torneios esportivos baseados no sistema de rating da FIFA.

**Funcionalidades:**
- Lê dados de times de um arquivo CSV
- Simula múltiplos torneios
- Calcula probabilidades de vitória

**Como usar:**
```bash
python tournament.py teams.csv
```

## 🛠️ Pré-requisitos

- Python 3.6 ou superior
- Biblioteca CS50 (`pip install cs50`)

##  Estrutura do Projeto

```
cc50-python/
├── readability.py
├── mario.py
├── mario2.py
├── hello.py
├── credit.py
├── cash.py
├── dna.py
├── lab6/
│   └── tournament.py
├── databases/          # Arquivos CSV para DNA
├── sequences/          # Sequências de DNA
└── README.md
```

## Conceitos Aprendidos

- **Variáveis e tipos de dados**
- **Estruturas de controle** (if, else, while, for)
- **Funções e modularização**
- **Manipulação de strings**
- **Listas e dicionários**
- **Algoritmos** (Luhn, guloso, busca)
- **Manipulação de arquivos CSV**
- **Simulações e aleatoriedade**

## 📝 Notas Importantes

- Todos os programas foram desenvolvidos seguindo as especificações do CS50
- O código prioriza clareza e legibilidade
- As soluções passam em todos os testes do CS50 (check50)
- Os programas tratam entradas inválidas adequadamente

## 📄 Licença

Este projeto é apenas para fins educacionais, como parte do curso CC50.

## Autor

Gustavo Sacomani Rafael - Estudante do curso CC50

---

Se este repositório te ajudou, considere dar uma estrela!
```
