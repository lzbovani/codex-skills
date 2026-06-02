# Referência SQL — Analista de Dados Sênior

## Ordem de Execução SQL (CRÍTICO)

```
1. FROM / JOIN       → quais tabelas e como combiná-las
2. WHERE             → filtrar linhas ANTES de agregar
3. GROUP BY          → agrupar linhas
4. HAVING            → filtrar grupos DEPOIS de agregar
5. SELECT            → escolher colunas e calcular expressões
6. DISTINCT          → eliminar duplicatas do resultado
7. ORDER BY          → ordenar resultado final
8. LIMIT / TOP       → limitar quantidade de linhas
```

> **Pegadinha**: não dá para usar alias do SELECT no WHERE porque SELECT roda depois do WHERE.

---

## JOINs — Comportamento Real

```sql
-- INNER JOIN: só linhas com match nos dois lados
SELECT a.id, b.valor
FROM tabela_a a
INNER JOIN tabela_b b ON a.id = b.id_a;

-- LEFT JOIN: todas as linhas da esquerda, NULL onde não tem match
SELECT a.id, b.valor  -- b.valor será NULL onde não há match
FROM tabela_a a
LEFT JOIN tabela_b b ON a.id = b.id_a;

-- Detectar linhas sem match (anti-join):
SELECT a.id
FROM tabela_a a
LEFT JOIN tabela_b b ON a.id = b.id_a
WHERE b.id_a IS NULL;  -- linhas de 'a' sem correspondência em 'b'
```

**NULL em JOIN**: `NULL = NULL` é FALSE em SQL. Use `IS NULL` / `IS NOT NULL`.

---

## Agregações e GROUP BY

```sql
-- Regra: toda coluna no SELECT que não é agregação DEVE estar no GROUP BY
SELECT
    departamento,
    COUNT(*) AS total_funcionarios,
    AVG(salario) AS media_salarial,
    MAX(salario) AS maior_salario
FROM funcionarios
GROUP BY departamento;

-- HAVING filtra GRUPOS (depois de agregar)
-- WHERE filtra LINHAS (antes de agregar)
SELECT departamento, COUNT(*) AS total
FROM funcionarios
WHERE ativo = 1               -- filtra linhas antes de agrupar
GROUP BY departamento
HAVING COUNT(*) > 5;          -- filtra grupos com menos de 6 funcionários
```

---

## CTEs (Common Table Expressions)

```sql
-- CTE básica: deixa o código legível e reutilizável
WITH vendas_mensais AS (
    SELECT
        DATE_TRUNC('month', data_venda) AS mes,
        produto_id,
        SUM(valor) AS total
    FROM vendas
    GROUP BY 1, 2
),
ranking AS (
    SELECT
        mes,
        produto_id,
        total,
        RANK() OVER (PARTITION BY mes ORDER BY total DESC) AS posicao
    FROM vendas_mensais
)
SELECT * FROM ranking WHERE posicao <= 3;
```

---

## Window Functions (Funções de Janela)

```sql
-- Sintaxe geral
FUNCAO() OVER (
    PARTITION BY coluna_de_agrupamento   -- opcional
    ORDER BY coluna_de_ordem             -- opcional (obrigatório para ranking/lag/lead)
    ROWS BETWEEN ...                     -- opcional (frame)
)

-- Ranking
ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salario DESC)  -- único, sem empate
RANK()       OVER (PARTITION BY dept ORDER BY salario DESC)  -- empata, pula posição
DENSE_RANK() OVER (PARTITION BY dept ORDER BY salario DESC)  -- empata, não pula

-- Acesso a linhas vizinhas
LAG(coluna, 1)  OVER (ORDER BY data)   -- valor da linha anterior
LEAD(coluna, 1) OVER (ORDER BY data)   -- valor da próxima linha

-- Agregação janelada (NÃO colapsa linhas — diferente de GROUP BY)
SUM(valor) OVER (PARTITION BY cliente ORDER BY data)   -- soma acumulada por cliente
AVG(valor) OVER (PARTITION BY regiao)                  -- média da região em cada linha

-- Diferença entre window e GROUP BY:
-- GROUP BY: 5 linhas agrupadas → 1 linha de resultado
-- WINDOW:   5 linhas originais → 5 linhas com novo campo calculado
```

---

## Subqueries — Quando Usar vs CTE

| Situação | Preferir |
|---|---|
| Reutilizar resultado em mais de um lugar | CTE |
| Filtro simples com IN/EXISTS | Subquery |
| Legibilidade e manutenção | CTE |
| Performance crítica (verificar com EXPLAIN) | Testar os dois |

```sql
-- EXISTS é mais eficiente que IN para grandes volumes
-- IN: carrega todos os valores
SELECT * FROM pedidos WHERE cliente_id IN (SELECT id FROM clientes WHERE ativo = 1);

-- EXISTS: para assim que encontra o primeiro match
SELECT * FROM pedidos p
WHERE EXISTS (SELECT 1 FROM clientes c WHERE c.id = p.cliente_id AND c.ativo = 1);
```

---

## Tratamento de NULL

```sql
-- COALESCE: retorna o primeiro valor não-nulo
SELECT COALESCE(telefone_celular, telefone_fixo, 'Sem telefone') FROM clientes;

-- NULLIF: retorna NULL se os dois valores são iguais (útil para evitar divisão por zero)
SELECT valor / NULLIF(quantidade, 0) AS preco_unitario FROM vendas;

-- IS NULL vs = NULL
WHERE campo IS NULL      -- CORRETO
WHERE campo = NULL       -- SEMPRE FALSE (nunca usar)
```

---

## Otimização Básica

```sql
-- Use índices: filtrar por colunas indexadas no WHERE
-- Evite funções em colunas indexadas no WHERE (impede uso do índice)
WHERE YEAR(data_venda) = 2024          -- MAL: função impede índice
WHERE data_venda >= '2024-01-01'       -- BEM: intervalo usa índice

-- EXPLAIN / EXPLAIN ANALYZE para ver o plano de execução
EXPLAIN SELECT * FROM pedidos WHERE cliente_id = 123;
```
