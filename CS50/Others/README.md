# Exercícios Extras – CC50 (CS50)

Este repositório contém exercícios **extras e de prática** desenvolvidos durante meus estudos no **CC50**, a versão em português do curso **CS50 – Introduction to Computer Science**, oferecido pela Harvard.

O objetivo destes exercícios é reforçar conceitos fundamentais da linguagem **C**, como:
- Uso de argumentos de linha de comando
- Manipulação de strings
- Controle de fluxo
- Funções
- Depuração de código
- Boas práticas de programação

---

## Estrutura dos Arquivos

Cada arquivo `.c` representa um exercício independente:

- **hello.c** – Programa simples para imprimir mensagens na tela  
- **hi.c** – Variação de saudação para prática de saída padrão  
- **argv.c** – Uso de argumentos da linha de comando (`argc` e `argv`)  
- **string.c** – Manipulação básica de strings  
- **uppercase.c** – Conversão de caracteres para letras maiúsculas  
- **scores.c** – Trabalho com arrays e cálculo de valores  
- **exit.c** – Uso do código de saída do programa (`return` / `exit`)  
- **buggy0.c / buggy1.c** – Exercícios focados em depuração (debugging)

> Alguns arquivos podem conter erros intencionais, usados para treinar identificação e correção de bugs.

---

## Como Compilar e Executar

Use o `clang` ou `gcc` para compilar os arquivos. Exemplo:

```bash
clang hello.c -o hello
./hello
