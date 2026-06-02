# Referência Estatística — Analista de Dados Sênior

## Estatística Descritiva

### Medidas de Tendência Central

| Medida | Fórmula | Quando usar |
|---|---|---|
| Média | Σx / n | Distribuições simétricas, sem outliers |
| Mediana | Valor central ordenado | Distribuições assimétricas, com outliers |
| Moda | Valor mais frequente | Dados categóricos, distribuições bimodais |

> **Regra**: outliers distorcem a média. Em renda, salários, preços de imóveis → use mediana.

### Medidas de Dispersão

```
Variância (s²) = Σ(xi - x̄)² / (n-1)   ← n-1 para amostra (não n)
Desvio Padrão (s) = √Variância
CV (Coeficiente de Variação) = s / x̄    ← compara dispersão entre grupos de escalas diferentes
IQR = Q3 - Q1                           ← resistente a outliers
```

### Identificar Outliers

```python
# Método IQR (robusto)
Q1 = df['coluna'].quantile(0.25)
Q3 = df['coluna'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
outliers = df[(df['coluna'] < limite_inferior) | (df['coluna'] > limite_superior)]

# Método Z-score (assume normalidade)
from scipy import stats
z_scores = np.abs(stats.zscore(df['coluna']))
outliers = df[z_scores > 3]
```

---

## Distribuições de Probabilidade

| Distribuição | Parâmetros | Quando aparece |
|---|---|---|
| Normal | μ, σ | Altura, QI, erros de medição |
| Binomial | n, p | Número de sucessos em n tentativas |
| Poisson | λ | Eventos raros por intervalo de tempo |
| Exponencial | λ | Tempo entre eventos |
| Uniforme | a, b | Sorteio equiprovável |

### Teorema Central do Limite (TCL)
> A distribuição das médias amostrais tende à Normal conforme n aumenta (n ≥ 30 como regra prática), independentemente da distribuição original.

---

## Testes de Hipótese — Fluxo Completo

```
1. Definir H0 (hipótese nula) e H1 (hipótese alternativa)
2. Escolher nível de significância α (padrão: 0.05)
3. Verificar pressupostos do teste
4. Calcular estatística de teste e p-valor
5. Decisão: se p-valor < α → rejeitar H0
6. Interpretação em linguagem do negócio
```

### O que é p-valor (definição correta)

> **p-valor** = probabilidade de observar um resultado tão extremo quanto o observado, **assumindo que H0 é verdadeira**.

> **NÃO é** a probabilidade de H0 ser verdadeira. Essa confusão custa pontos em prova.

### Escolha do Teste Correto

```
Comparar médias?
├── 1 grupo vs valor fixo → t-test uma amostra
├── 2 grupos independentes
│   ├── Normal + variâncias iguais → t-test independente
│   ├── Normal + variâncias diferentes → Welch t-test
│   └── Não-normal → Mann-Whitney U
├── 2 grupos pareados (antes/depois mesmo indivíduo) → t-test pareado
└── 3+ grupos
    ├── Normal → ANOVA (depois post-hoc: Tukey)
    └── Não-normal → Kruskal-Wallis

Comparar proporções?
├── 1 proporção vs valor → z-test proporção
└── 2 proporções → z-test duas proporções, ou qui-quadrado

Associação entre variáveis categóricas? → Qui-quadrado
Correlação entre contínuas?
├── Normal → Pearson
└── Não-normal ou ordinal → Spearman
```

```python
from scipy import stats

# t-test independente
stat, p = stats.ttest_ind(grupo_a, grupo_b, equal_var=False)  # Welch por padrão

# Mann-Whitney (não paramétrico)
stat, p = stats.mannwhitneyu(grupo_a, grupo_b, alternative='two-sided')

# Qui-quadrado
stat, p, dof, expected = stats.chi2_contingency(tabela_contingencia)

# Shapiro-Wilk (testar normalidade, n < 5000)
stat, p = stats.shapiro(amostra)
# p > 0.05 → não rejeita normalidade
```

---

## Correlação vs Causalidade

> **Correlação não implica causalidade.** Duas variáveis podem ser correlacionadas por:
> - Causa direta (A → B)
> - Causa reversa (B → A)
> - Variável confundidora (C → A e C → B)
> - Coincidência espúria

```python
# Pearson: correlação linear, sensível a outliers
corr_pearson = df['x'].corr(df['y'], method='pearson')

# Spearman: correlação monotônica, robusto a outliers
corr_spearman = df['x'].corr(df['y'], method='spearman')
```

---

## Regressão Linear

```
y = β0 + β1*x1 + β2*x2 + ... + ε

β0 = intercepto (valor de y quando todos x = 0)
βi = coeficiente (variação em y para +1 unidade em xi, mantendo os outros fixos)
R² = proporção da variância de y explicada pelo modelo (0 a 1)
R² ajustado = penaliza por adicionar variáveis irrelevantes
```

### Pressupostos da Regressão (cobrado em prova)
1. Linearidade — relação linear entre X e y
2. Independência dos erros — resíduos não autocorrelacionados
3. Homocedasticidade — variância dos erros constante
4. Normalidade dos resíduos — resíduos seguem distribuição Normal
5. Ausência de multicolinearidade — features não altamente correlacionadas entre si

```python
import statsmodels.api as sm

X_const = sm.add_constant(X)  # adiciona intercepto
model = sm.OLS(y, X_const).fit()
print(model.summary())
# Interpretar: coef, p-valor de cada variável, R², F-statistic
```

---

## Erros Clássicos em Prova

| Erro | Versão correta |
|---|---|
| "p=0.03 significa 3% de chance de H0 ser verdadeira" | p-valor é calculado assumindo H0 verdadeira |
| "Não rejeitamos H0 → H0 é verdadeira" | Apenas que não temos evidência suficiente para rejeitá-la |
| "Correlação de 0.8 significa causalidade forte" | Correlação não é causalidade |
| "R²=0.85 significa modelo bom" | Depende do contexto; verificar resíduos |
| Usar média em dados com outliers | Usar mediana |
| Usar t-test sem verificar normalidade | Verificar com Shapiro-Wilk primeiro |
