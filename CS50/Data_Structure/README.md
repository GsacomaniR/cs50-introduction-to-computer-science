```markdown
# Data Structures - CC.50

Este repositório contém duas implementações fundamentais de estruturas de dados desenvolvidas durante o curso **CC.50 (CS50's Introduction to Computer Science)**. Os projetos exploram conceitos de **hash tables**, **listas ligadas**, **algoritmos de hashing** e **árvores genealógicas recursivas**.

---

## Projetos

### 1. Speller - Verificador Ortográfico

Um corretor ortográfico eficiente que carrega um dicionário em memória usando uma **tabela hash otimizada** e verifica palavras em um texto.

#### Características Técnicas

| Componente | Detalhe |
|------------|---------|
| **Estrutura** | Tabela hash com 100.000 buckets |
| **Hash Function** | djb2 (Dan Bernstein) com case-insensitive |
| **Tratamento de colisões** | Encadeamento separado (listas ligadas) |
| **Carga máxima** | ~143.091 palavras (fator de carga ~1.43) |
| **Complexidade** | O(1) médio para busca e inserção |

#### Funcionalidades

```c
// Verifica se palavra está no dicionário (case-insensitive)
bool check(const char *word);

// Hash function otimizada (djb2)
unsigned int hash(const char *word);

// Carrega dicionário do arquivo para memória
bool load(const char *dictionary);

// Retorna número total de palavras carregadas
unsigned int size(void);

// Libera toda a memória alocada
bool unload(void);
```

#### Estrutura da Tabela Hash

```
┌─────────────────────────────────────┐
│  Buckets (N = 100.000)              │
├─────┬───────────────────────────────┤
│ [0] │ → [apple] → [application] → NULL │
│ [1] │ → NULL                        │
│ [2] │ → [banana] → NULL             │
│ ... │  ...                          │
│[99999]│ → [zebra] → NULL            │
└─────┴───────────────────────────────┘
```

---

### 2. Inheritance - Simulação Genética

Um simulador de herança genética que modela a transmissão de **alelos do tipo sanguíneo** (A, B, O) através de gerações familiares usando **estruturas recursivas**.

#### Estrutura de Dados

```c
typedef struct person
{
    struct person *parents[2];  // Ponteiros para os pais
    char alleles[2];            // Alelos do tipo sanguíneo
} person;
```

#### Lógica Genética

- **Geração base (G0)** : Alelos são escolhidos aleatoriamente
- **Gerações seguintes** : Cada filho herda **um alelo aleatório de cada pai**
- **Possíveis tipos sanguíneos**: AA, AO, OA, BB, BO, OB, OO, AB, BA

#### Árvore Familiar

```
Child (Generation 0): blood type AO
    Parent (Generation 1): blood type AB
        Grandparent (Generation 2): blood type AO
            Great-Grandparent (Generation 3): blood type BB
            Great-Grandparent (Generation 3): blood type OO
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OO
```

---

## 📁 Estrutura do Repositório

```
data-structure-cc50/
├── speller/
│   ├── dictionary.c      # Implementação da tabela hash
│   ├── dictionary.h      # Interface e definições
│   └── speller.c         # Programa principal (não incluso)
├── inheritance/
│   └── inheritance.c     # Simulação genética recursiva
└── README.md             # Documentação
```

---

## Compilação e Execução

### Speller

```bash
cd speller
make speller
./speller texts/lalaland.txt
```

### Inheritance

```bash
cd inheritance
make inheritance
./inheritance
```

---

## 🔬 Análise de Complexidade

### Speller - Hash Table

| Operação | Melhor Caso | Pior Caso | Médio |
|----------|-------------|-----------|-------|
| `hash()` | O(1) | O(L) | O(L/2)* |
| `check()` | O(1) | O(n) | O(1) |
| `load()` | O(n) | O(n²) | O(n) |
| `unload()` | O(n) | O(n) | O(n) |

*L = comprimento médio da palavra*

### Inheritance - Árvore Genealógica

| Operação | Complexidade |
|----------|--------------|
| `create_family()` | O(2^G)* |
| `free_family()` | O(2^G) |
| `print_family()` | O(2^G) |

*G = número de gerações*

---

## 💡 Otimizações Implementadas

### Speller
-  **Hash function djb2**: Baixa taxa de colisão e boa distribuição
-  **Case-insensitive hashing**: Converte para lowercase durante o hash
-  **Inserção no início da lista**: O(1) para inserção
-  **Buckets otimizados**: N = 100.000 para melhor performance

### Inheritance
-  **Recursão eficiente**: Liberação de memória post-order
-  **Alocação dinâmica**: Cada pessoa ocupa exatamente o necessário

---

## Testes e Validação

### Speller - Dicionários Testados
- `dictionaries/small` (1.438 palavras)
- `dictionaries/large` (143.091 palavras)

### Valgrind (Verificação de memória)
```bash
valgrind ./speller texts/cat.txt
# Output esperado: "All heap blocks were freed -- no leaks are possible"
```

---

## Métricas de Performance (Speller)

| Dicionário | Tempo de Load | Memory Usage |
|------------|---------------|--------------|
| Small (1.438 palavras) | ~0.001s | ~0.1 MB |
| Large (143.091 palavras) | ~0.042s | ~9.4 MB |

---

## Aprendizados

1. **Hash Tables**: Trade-off entre memória e velocidade
2. **Encadeamento**: Como tratar colisões eficientemente
3. **Recursão em estruturas**: Árvores e listas ligadas
4. **Gerenciamento de memória**: `malloc`, `free` e prevenção de vazamentos
5. **Algoritmos genéticos**: Simulação simplificada de herança mendeliana

---

## Licença

Este projeto é parte do curso CC.50 e está disponível para fins educacionais.

---

## Autor

Desenvolvido como parte do currículo **CC.50 - Introdução à Ciência da Computação**

*"Data structures are the backbone of efficient algorithms."*
```
Gustavo Sacomani Rafael
