# Referência Power BI / DAX — Analista de Dados Sênior

## Conceitos Fundamentais (cobrados em prova)

### Contexto de Filtro vs Contexto de Linha

```
Contexto de Linha:
- Existe dentro de colunas calculadas e funções iteradoras (SUMX, AVERAGEX, etc.)
- Refere-se à linha ATUAL sendo processada
- NÃO filtra o modelo — só acessa colunas da linha atual

Contexto de Filtro:
- Existe em medidas
- Vem de: visuais, slicers, filtros de página, CALCULATE
- Filtra as tabelas do modelo antes de calcular
```

> **Armadilha clássica**: numa medida, `SUM(Vendas[Valor])` usa contexto de filtro.
> Numa coluna calculada, `Vendas[Valor]` acessa a linha atual (contexto de linha).

---

## CALCULATE — A Função Mais Importante

```dax
-- Sintaxe
CALCULATE(<expressão>, <filtro1>, <filtro2>, ...)

-- CALCULATE faz duas coisas:
-- 1. Avalia a expressão
-- 2. Modifica o contexto de filtro com os filtros fornecidos

-- Exemplo: total de vendas só do produto "X"
Vendas Produto X =
CALCULATE(
    SUM(Vendas[Valor]),
    Produtos[Nome] = "Produto X"
)

-- Remover todos os filtros de uma coluna (ALL)
Total Geral =
CALCULATE(SUM(Vendas[Valor]), ALL(Vendas))

-- Remover filtro de uma coluna específica
% do Total =
DIVIDE(
    SUM(Vendas[Valor]),
    CALCULATE(SUM(Vendas[Valor]), ALL(Vendas[Produto]))
)
```

---

## SUM vs SUMX

```dax
-- SUM: soma uma coluna existente (mais rápido)
Total Simples = SUM(Vendas[Valor])

-- SUMX: itera linha por linha e soma o resultado de uma expressão
-- Use quando precisa de cálculo por linha ANTES de somar
Total Receita = SUMX(Vendas, Vendas[Quantidade] * Vendas[PrecoUnitario])

-- Regra: se a coluna já existe → SUM. Se precisa calcular antes → SUMX
```

---

## Funções de Inteligência de Tempo (Time Intelligence)

```dax
-- Pré-requisito: tabela de datas marcada como "Tabela de Datas" no Power BI

-- Ano até a data
YTD Vendas = TOTALYTD(SUM(Vendas[Valor]), Calendario[Data])

-- Mês até a data
MTD Vendas = TOTALMTD(SUM(Vendas[Valor]), Calendario[Data])

-- Mesmo período do ano anterior
Vendas Ano Anterior =
CALCULATE(SUM(Vendas[Valor]), SAMEPERIODLASTYEAR(Calendario[Data]))

-- Variação percentual YoY
Variação YoY % =
DIVIDE(
    SUM(Vendas[Valor]) - [Vendas Ano Anterior],
    [Vendas Ano Anterior]
)

-- Últimos N dias
Últimos 30 dias =
CALCULATE(
    SUM(Vendas[Valor]),
    DATESINPERIOD(Calendario[Data], LASTDATE(Calendario[Data]), -30, DAY)
)
```

---

## Modelagem — Relacionamentos Corretos

```
Esquema Estrela (Star Schema) — padrão correto:
- Tabela fato no centro (ex: Vendas) — contém métricas e chaves estrangeiras
- Tabelas dimensão ao redor (ex: Produtos, Clientes, Calendario) — contém atributos

Cardinalidade:
- Muitos para Um (*:1) — o mais comum: Vendas → Produtos
- Um para Um (1:1) — raramente necessário
- Muitos para Muitos (*:*) — evitar; indica problema de modelagem

Direção do filtro:
- Single (→) — filtro fluye da dimensão para a fato (padrão, recomendado)
- Bidirectional (↔) — evitar; pode causar ambiguidade e resultados inesperados
```

---

## Medidas vs Colunas Calculadas

| | Medida | Coluna Calculada |
|---|---|---|
| Calculada em | Tempo de consulta | Tempo de refresh |
| Contexto | Contexto de filtro | Contexto de linha |
| Armazenada | Não (dinâmica) | Sim (ocupa memória) |
| Pode usar | Funções de agregação | Funções de linha |
| Quando usar | KPIs, totais, % | Segmentações, categorias |

```dax
-- Coluna calculada: categoria de valor por linha
Faixa Valor =
IF(Vendas[Valor] > 1000, "Alto", IF(Vendas[Valor] > 500, "Médio", "Baixo"))

-- Medida: total calculado dinamicamente
Total Vendas = SUM(Vendas[Valor])
Media Vendas = AVERAGE(Vendas[Valor])
Contagem = COUNTROWS(Vendas)
Distintos = DISTINCTCOUNT(Clientes[ID])
```

---

## DIVIDE — Sempre Usar em Vez de "/"

```dax
-- ERRADO: divisão direta causa erro se denominador = 0
% = [Vendas] / [Total]

-- CORRETO: DIVIDE retorna BLANK() ou valor alternativo se denominador = 0
% = DIVIDE([Vendas], [Total], 0)   -- retorna 0 se Total = 0
% = DIVIDE([Vendas], [Total])      -- retorna BLANK() se Total = 0
```

---

## Funções de Filtro e Tabela

```dax
-- ALL: remove filtros (retorna todos os valores de uma tabela/coluna)
ALL(Tabela)
ALL(Tabela[Coluna])

-- FILTER: cria tabela filtrada (usar dentro de CALCULATE)
CALCULATE(
    SUM(Vendas[Valor]),
    FILTER(Produtos, Produtos[Categoria] = "Eletrônicos")
)

-- VALUES: retorna valores únicos de uma coluna (respeita contexto de filtro)
VALUES(Produtos[Categoria])

-- RELATED: acessa coluna de tabela relacionada (dentro de contexto de linha)
-- (equivalente ao JOIN do SQL, dentro de coluna calculada)
Categoria Produto = RELATED(Produtos[Categoria])
```

---

## Armadilhas Mais Comuns

| Erro | Causa | Solução |
|---|---|---|
| Medida retorna valor errado em contexto diferente | Não usar CALCULATE para modificar contexto | Envolver com CALCULATE + filtro adequado |
| SUMX mais lento que SUM | Iteração desnecessária | Usar SUM quando coluna já existe |
| Relacionamento não filtra | Direção errada ou relação inativa | Verificar cardinalidade e direção |
| Blank vs 0 em medida | BLANK() se propaga | Usar `+ 0` ou `IF(ISBLANK(...), 0, ...)` |
| Coluna calculada consome memória | Calcular algo que deveria ser medida | Converter para medida |
