# CS50 – Aula de Arrays

Este repositório contém os exercícios desenvolvidos durante a aula de Arrays do curso CS50 (Introduction to Computer Science – Harvard).

# Conceitos Aprendidos

Durante esta aula, foram abordados os seguintes conceitos:

- O que são arrays (vetores) em C

- Manipulação de strings

- Uso da biblioteca ctype.h

- Conversão de caracteres

- Operações com índices

-  Criptografia básica

- Contagem e análise de texto

---

# Arquivos do Projeto
> caesar.c

- Implementação da Cifra de César, um método clássico de criptografia que desloca letras do alfabeto por um número fixo de posições.

- Conceitos utilizados:

- Arrays de caracteres (strings)

- Conversão ASCII

- Operador módulo (%)

- Função isdigit()

- Validação de argumentos da linha de comando

> readability.c
Programa que calcula o nível de leitura de um texto utilizando a fórmula Coleman-Liau Index.

Conceitos utilizados:

- Contagem de letras, palavras e frases

- Uso de isalpha() e isspace()

- Cálculo matemático com floats

- Manipulação de strings

> scrabble.c

Simula a pontuação do jogo Scrabble, atribuindo pontos às letras digitadas pelos jogadores.

Conceitos utilizados:

- Array para armazenar pontuação das letras

- Percorrer strings com for

- Uso de toupper()

Comparação de pontuações

> substitution.c

Implementação de uma cifra por substituição, onde cada letra do alfabeto é mapeada para outra letra.

Conceitos utilizados:

- Arrays para representar o alfabeto

- Validação de chave de substituição

- Uso de strlen()

- Manipulação de caracteres maiúsculos e minúsculos

---

# Como Compilar

Para compilar os arquivos, utilize:

> make nome_do_programa

Exemplo:

> make caesar
> ./caesar 3

---

# Objetivo da Aula

O principal objetivo desta aula foi compreender como arrays funcionam na linguagem C e como eles são fundamentais para:

- Trabalhar com texto

- Criar sistemas de criptografia simples

- Analisar dados

Manipular sequências de caracteres

# Aprendizado

Essa aula reforça a importância dos arrays como estrutura fundamental na programação, sendo base para estruturas mais avançadas como:

- Matrizes

- Strings

- Estruturas de dados

- Algoritmos de busca e ordenação
