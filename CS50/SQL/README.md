```markdown
# SQL do CC50 - Exercícios Comentados

Este repositório contém soluções comentadas para os exercícios de SQL do curso **CC50 (Harvard CS50 adaptado)**. Os projetos abordam desde consultas básicas até investigações criminais complexas utilizando múltiplas tabelas e junções.

## 📂 Estrutura do Projeto

```
/
├── log.sql              # Investigação do caso "O Roubo na Fiftyville"
├── movies/              # Queries sobre banco de dados de filmes (1-13.sql)
└── songs/               # Queries sobre banco de dados de músicas (1-8.sql)
```

---

##  Caso: O Roubo na CS50 (Fiftyville)

Uma investigação completa usando SQL para encontrar o ladrão, o cúmplice e a cidade de fuga.

### Metodologia aplicada no `log.sql`

| Passo | Ação | Resultado |
|-------|------|------------|
| 1 | Buscar relatório do crime (28/07/2023, Fiftyville) | Roubo às 10:15am na bakery, 3 testemunhas |
| 2 | Analisar entrevistas das testemunhas | Ruth (carro), Eugene (caixa eletrônico), Raymond (voo) |
| 3 | Verificar saídas da bakery (10:15-10:25) | 8 placas de carro suspeitas |
| 4 | Verificar saques no caixa da Leggett Street | Várias contas bancárias |
| 5 | Identificar voo mais cedo em 29/07 | ID 36 às 8:20 para Nova York |
| 6 | Cruzar todos os dados (pessoas + carro + saque + voo) | **Bruce** (placa 94KL13X) |
| 7 | Verificar chamadas curtas (< 60s) no dia do crime | Bruce ligou para (375) 555-8161 |
| 8 | Identificar receptor da chamada | **Robin** (cúmplice) |
| 9 | Confirmar destino do voo | **Nova York** (cidade de fuga) |  

### Conclusão do Caso

- **Ladrão:** Bruce
- **Cúmplice:** Robin  
- **Cidade de fuga:** Nova York

---

## Banco de Dados `movies` (13 consultas)

Exemplos de consultas com junções (`JOIN`), subconsultas e ordenação.

| Query | Descrição |
|-------|------------|
| `1.sql` | Títulos de filmes de 2008 |
| `2.sql` | Ano de nascimento de Emma Stone |
| `3.sql` | Filmes de 2018 em diante (ordem alfabética) |
| `4.sql` | Quantos filmes têm nota 10.0 |
| `5.sql` | Filmes da saga Harry Potter em ordem cronológica |
| `6.sql` | Média das notas dos filmes de 2012 |
| `7.sql` | Notas dos filmes de 2010 (decrescente por nota) |
| `8.sql` | Atores do filme "Toy Story" |
| `9.sql` | Atores de 2004 ordenados por ano de nascimento |
| `10.sql` | Diretores com filmes nota ≥ 9.0 |
| `11.sql` | Top 5 filmes de Chadwick Boseman por nota |
| `12.sql` | Filmes com Johnny Depp e Helena Bonham Carter |
| `13.sql` | Atores que trabalharam com Kevin Bacon (exceto ele) |

---

## Banco de Dados `songs` (8 consultas)

Consultas sobre músicas do Spotify com filtros e agregações.

| Query | Descrição |
|-------|------------|
| `1.sql` | Nomes de todas as músicas |
| `2.sql` | Músicas ordenadas por tempo (crescente) |
| `3.sql` | 5 músicas mais longas |
| `4.sql` | Músicas dançantes, enérgicas e positivas (>0.75) |
| `5.sql` | Média de energia de todas as músicas |
| `6.sql` | Músicas de Post Malone |
| `7.sql` | Média de energia das músicas de Drake |
| `8.sql` | Músicas com "feat." no título |

---
```

---

## Principais Conceitos SQL Aplicados

- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- `JOIN` (INNER JOIN implícito e explícito)
- `AVG()`, `COUNT()`, `DISTINCT`
- Subconsultas com `IN` e `=`
- Filtros com `LIKE`, `BETWEEN`, `AND/OR`
- Múltiplas junções (até 4 tabelas no caso `log.sql`)

---

## Observações

- O arquivo `log.sql` contém todos os comandos da investigação comentados para fins didáticos.
- Os arquivos `1.sql` a `13.sql` em `movies/` seguem a numeração original do CS50.
- Em `songs/`, algumas queries usam subconsultas para filtrar por artista.

---

## Aprendizados

Com este projeto, foi possível praticar:

1. Leitura de *schemas* de banco de dados (`.schema`)
2. Cruzamento de informações de múltiplas tabelas
3. Investigação forense com SQL (caso Fiftyville)
4. Uso estratégico de `JOIN` para relacionar pessoas, contas bancárias, voos e chamadas
5. Filtros temporais e de duração (chamadas < 60 segundos)

---

## Créditos

Projeto desenvolvido como parte do curso **CC50 (CS50's Introduction to Computer Science)** de Harvard, adaptado pela Fundação Estudar.

---

## 📄 Licença

Este material é para fins educacionais. Sinta-se à vontade para usá-lo como referência em seus estudos de SQL.
```
Gustavo Sacomani Rafael

Este README documenta:
- **Todo o processo investigativo** do caso Fiftyville (passo a passo com resultados)
- **Resumo das 13 queries** de filmes com suas finalidades
- **Resumo das 8 queries** de músicas
- Instruções de execução
- Conceitos SQL aplicados
- Observações sobre a estrutura dos arquivos
