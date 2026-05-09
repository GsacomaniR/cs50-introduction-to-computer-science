# Algoritmos - CS50

Este diretório contém implementações e análises práticas dos principais algoritmos de **ordenação** (sorting) e **votação** (election methods) estudados no curso CS50 de Introdução à Ciência da Computação de Harvard.

## Conteúdo

- **`sort1`, `sort2`, `sort3`** – três programas de ordenação (identidade oculta) analisados pelo comportamento temporal.
- **`plurality`** – sistema de votação simples (pluralidade / "o mais votado").
- **`runoff`** – sistema de votação por eliminação em turnos (runoff / "segundo turno").
- **`tideman`** – sistema de votação por pares ordenados (método de Tideman / "locked pairs").

---

## Análise dos Algoritmos de Ordenação

Foram realizados testes com três algoritmos de ordenação diferentes, medindo o tempo de execução (em segundos) para listas de 5.000, 10.000 e 50.000 elementos em três estados de ordenação inicial: aleatório, ordem reversa e já ordenado.

### Tabela comparativa (50.000 elementos)

| Algoritmo         | Aleatório | Reverso | Ordenado | Complexidade |
|------------------|-----------|---------|----------|---------------|
| **sort1**        | 6,064s    | 4,504s  | 0,985s   | O(n²) com melhor caso O(n) |
| **sort2**        | 0,945s    | 0,958s  | 0,849s   | O(n log n)                |
| **sort3**        | 2,811s    | 2,905s  | 2,784s   | O(n²) independente       |

---

### sort1 → **Bubble Sort** (com otimização de parada antecipada)

**Comportamento observado:**  
- Melhor caso (dados ordenados): 0,038s → 0,985s (fator ~25×) → sugere **O(n)**.  
- Pior caso (dados aleatórios): 0,052s → 6,064s (fator ~116×) → sugere **O(n²)**.  

**Evidência:**  
A grande variação conforme a ordenação inicial é a marca registrada do *bubble sort*. A versão utilizada provavelmente interrompe o algoritmo quando nenhuma troca é feita.

---

### sort2 → **Merge Sort**

**Comportamento observado:**  
- Tempos praticamente idênticos para os três tipos de entrada:  
  - Aleatório: 0,945s  
  - Reverso: 0,958s  
  - Ordenado: 0,849s  
- Crescimento de ~45× para 10× mais elementos → compatível com **O(n log n)**.

**Evidência:**  
O algoritmo sempre divide os dados e depois os intercala (merge), independentemente da ordem inicial — característica fundamental do *merge sort*.

---

### sort3 → **Selection Sort**

**Comportamento observado:**  
- Tempos muito próximos entre as três entradas:  
  - Aleatório: 2,811s  
  - Reverso: 2,905s  
  - Ordenado: 2,784s  
- Fator de crescimento ~60–70× para 10× mais elementos → **O(n²)**.

**Evidência:**  
O *selection sort* sempre percorre todo o vetor para encontrar o menor elemento. Ele **não se beneficia** de listas parcialmente ordenadas, ao contrário do *bubble sort*.

---

## Implementações de Sistemas de Votação

### 1. Pluralidade (`plurality`)

**Funcionamento:**  
- Cada eleitor vota em **um único candidato**.  
- Vence quem tiver **mais votos** (não necessariamente a maioria).  
- Pode haver **empates múltiplos** (todos os que atingirem a maior votação são declarados vencedores).

**Destaques do código:**  
- Função `vote()`: busca linear pelo nome do candidato e incrementa os votos.  
- Função `print_winner()`: primeiro encontra o `max_votes`, depois imprime todos os candidatos com essa votação.

---

### 2. Turno Único com Eliminação (`runoff`)

**Funcionamento:**  
- Cada eleitor fornece uma **lista de preferências** (rank) de todos os candidatos.  
- Enquanto não houver vencedor:  
  - Contam-se os votos **do candidato preferido ainda não eliminado** de cada eleitor.  
  - Se alguém tiver `> 50%` dos votos → vence.  
  - Caso contrário, **elimina-se o(s) candidato(s) com menor votação**.  
  - Em caso de empate geral, todos os não eliminados vencem.

**Destaques do código:**  
- `tabulate()`: para cada eleitor, encontra o primeiro candidato não eliminado na sua ordem de preferência e adiciona um voto.  
- `find_min()` / `eliminate()` / `is_tie()`: gerenciam a eliminação de candidatos com menor votação.  
- `print_winner()`: verifica se alguém ultrapassou metade dos votos (`voter_count / 2`).

---

### 3. Método de Tideman (`tideman`)

**Funcionamento (passos principais):**  
1. Cada eleitor ordena todos os candidatos por preferência.  
2. Constrói-se uma matriz `preferences[i][j]` = quantos eleitores preferem `i` sobre `j`.  
3. Criam-se `pairs` (pares) para todos os casos onde `i` é preferido sobre `j`.  
4. Ordenam-se os pares por **força da vitória** (diferença `preferences[winner][loser] - preferences[loser][winner]`).  
5. Aplicam-se os pares em ordem decrescente, **somente se não criarem um ciclo** no grafo de preferências.  
6. O vencedor é o candidato que não possui nenhuma aresta **entrante** no grafo final (fonte do grafo).

**Destaques do código:**  
- `add_pairs()`: adiciona apenas pares com vitória não empatada.  
- `sort_pairs()`: ordenação por força de vitória (bubble sort no código – poderia ser melhorada).  
- `creates_cycle()`: função recursiva que verifica se travar o par `(winner, loser)` criaria um ciclo no grafo.  
- `print_winner()`: imprime o(s) candidato(s) que não são perdedores de nenhuma aresta travada.

---

## Como compilar e executar

Todos os exemplos foram feitos no ambiente do CS50 (ou com a biblioteca `cs50.h` instalada).

### Compilação (exemplo para `plurality`):
```bash
gcc -o plurality plurality.c -lcs50
