# Referência Python para Dados — Analista de Dados Sênior

## Pandas — Operações Essenciais e Armadilhas

### Leitura e inspeção inicial (sempre fazer primeiro)

```python
import pandas as pd
import numpy as np

df = pd.read_csv('arquivo.csv', encoding='utf-8')  # testar latin-1 se der erro
# df = pd.read_excel('arquivo.xlsx', sheet_name='Plan1')

# Inspeção obrigatória
df.shape          # (linhas, colunas)
df.dtypes         # tipos de cada coluna
df.head(5)        # primeiras linhas
df.tail(5)        # últimas linhas
df.info()         # tipos + nulls resumido
df.describe()     # estatísticas descritivas (só numéricas)
df.isnull().sum() # contagem de nulos por coluna
df.duplicated().sum()  # linhas duplicadas
```

---

### Seleção de dados — .loc vs .iloc

```python
# .loc — por RÓTULO (nome do índice e nome da coluna)
df.loc[0, 'nome']           # linha com índice 0, coluna 'nome'
df.loc[0:5, 'nome':'idade'] # intervalo INCLUSIVO dos dois lados
df.loc[df['idade'] > 30]    # filtro booleano

# .iloc — por POSIÇÃO inteira (0-based)
df.iloc[0, 1]               # primeira linha, segunda coluna
df.iloc[0:5, 0:3]           # linhas 0-4, colunas 0-2 (exclusivo no fim)
df.iloc[-1]                 # última linha

# ARMADILHA: após reset_index(), os rótulos mudam — verificar sempre
df = df.reset_index(drop=True)
```

---

### Filtragem e condições múltiplas

```python
# Condições múltiplas: usar & | ~ (não and/or/not)
df[(df['idade'] > 25) & (df['cidade'] == 'SP')]
df[(df['status'] == 'A') | (df['status'] == 'B')]
df[~df['nome'].isna()]     # não-nulos

# isin para múltiplos valores
df[df['cidade'].isin(['SP', 'RJ', 'BH'])]

# query (mais legível para condições complexas)
df.query("idade > 25 and cidade == 'SP'")
```

---

### Valores Nulos

```python
# Verificar
df.isnull().sum()
df.isnull().mean()  # proporção de nulos

# Remover
df.dropna()                        # remove qualquer linha com nulo
df.dropna(subset=['coluna'])       # remove só se 'coluna' for nula
df.dropna(thresh=3)                # mantém linhas com pelo menos 3 não-nulos

# Preencher
df['col'].fillna(0)
df['col'].fillna(df['col'].mean())
df['col'].fillna(method='ffill')   # forward fill (DEPRECATED em versões novas)
df['col'].ffill()                  # forma atual
df['col'].bfill()                  # backward fill

# ARMADILHA: comparar com NaN
df[df['col'] == np.nan]   # SEMPRE vazio — nunca usar
df[df['col'].isna()]      # CORRETO
```

---

### GroupBy

```python
# Agregação simples
df.groupby('categoria')['valor'].sum()
df.groupby('categoria')['valor'].agg(['mean', 'std', 'count'])

# Múltiplas colunas de agrupamento
df.groupby(['categoria', 'regiao'])['valor'].sum()

# agg com dicionário — diferentes funções por coluna
df.groupby('categoria').agg({
    'valor': ['sum', 'mean'],
    'quantidade': 'count'
})

# transform — mantém o mesmo número de linhas (útil para criar features)
df['media_categoria'] = df.groupby('categoria')['valor'].transform('mean')

# ARMADILHA: groupby retorna índice hierárquico — usar reset_index()
resultado = df.groupby('categoria')['valor'].sum().reset_index()
```

---

### Merge (equivalente ao JOIN do SQL)

```python
# inner join (padrão)
pd.merge(df_a, df_b, on='id')
pd.merge(df_a, df_b, on='id', how='inner')

# left join
pd.merge(df_a, df_b, on='id', how='left')

# chaves com nomes diferentes
pd.merge(df_a, df_b, left_on='id_cliente', right_on='cliente_id')

# verificar resultado (anti-join: linhas sem match)
resultado = pd.merge(df_a, df_b, on='id', how='left', indicator=True)
sem_match = resultado[resultado['_merge'] == 'left_only']
```

---

### Transformações de Tipo

```python
df['coluna'] = df['coluna'].astype(int)
df['coluna'] = df['coluna'].astype(float)
df['coluna'] = df['coluna'].astype(str)

# Datas — CRÍTICO
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['ano']  = df['data'].dt.year
df['mes']  = df['data'].dt.month
df['dia_semana'] = df['data'].dt.day_name()

# ARMADILHA: pd.to_numeric com erros
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')  # NaN onde não converte
```

---

### Apply — Quando Usar e Quando Evitar

```python
# apply é lento — preferir operações vetorizadas quando possível

# LENTO (apply)
df['nova'] = df['col'].apply(lambda x: x * 2)

# RÁPIDO (vetorizado)
df['nova'] = df['col'] * 2

# Use apply quando a lógica é complexa e não tem alternativa vetorizada
df['categoria'] = df['valor'].apply(lambda x: 'alto' if x > 1000 else 'baixo')

# Alternativa vetorizada com np.where
df['categoria'] = np.where(df['valor'] > 1000, 'alto', 'baixo')

# Múltiplas condições com np.select
condicoes = [df['valor'] > 1000, df['valor'] > 500, df['valor'] > 0]
escolhas  = ['alto', 'médio', 'baixo']
df['categoria'] = np.select(condicoes, escolhas, default='zero ou negativo')
```

---

### Visualização com Matplotlib/Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Estrutura padrão
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Distribuição
axes[0].hist(df['valor'], bins=30, edgecolor='black')
axes[0].set_title('Distribuição de Valor')
axes[0].set_xlabel('Valor')
axes[0].set_ylabel('Frequência')

# Boxplot para outliers
sns.boxplot(data=df, x='categoria', y='valor', ax=axes[1])
axes[1].set_title('Valor por Categoria')

plt.tight_layout()
plt.show()

# Heatmap de correlação
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Matriz de Correlação')
plt.show()
```

---

## Armadilhas Mais Comuns

| Erro | Causa | Solução |
|---|---|---|
| `SettingWithCopyWarning` | Modificar slice de DataFrame | `df = df.copy()` ou usar `.loc` |
| `KeyError` em coluna | Nome com espaço ou acento | `df.columns.tolist()` para verificar |
| Tipos mistos em coluna | CSV com nulos ou texto em coluna numérica | `pd.to_numeric(..., errors='coerce')` |
| `inplace=True` não funciona | Alguns métodos ignoram inplace | Sempre reatribuir: `df = df.dropna()` |
| Índice desalinhado após filter | groupby/filter muda índice | `reset_index(drop=True)` |
