# Referência Machine Learning — Analista de Dados Sênior

## Pipeline Correto — Ordem Obrigatória

```
1. Separar treino/teste ANTES de qualquer pré-processamento
2. Análise exploratória apenas no treino
3. Fit do scaler/encoder APENAS no treino → transform em treino e teste
4. SMOTE (se necessário) APENAS no treino após scaling
5. Treinar modelo no treino
6. Avaliar no teste (UMA VEZ — ou usar cross-validation)
```

> **Data Leakage**: qualquer informação do conjunto de teste que vaza para o treino invalida a avaliação. É o erro mais grave e mais comum.

---

## Pré-processamento Correto (sem leakage)

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # stratify para classificação
)

# ERRADO — fit no dataset completo (leakage)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # NÃO FAZER

# CORRETO — fit só no treino
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit + transform no treino
X_test_scaled  = scaler.transform(X_test)         # só transform no teste

# MELHOR — usar Pipeline (garante que nunca haverá leakage)
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

---

## SMOTE — Uso Correto

```python
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline  # importar do imblearn!

# ERRADO — SMOTE antes do split (leakage grave)
X_res, y_res = SMOTE().fit_resample(X, y)
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res)

# CORRETO — SMOTE dentro do pipeline ou após o split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train_res, y_train_res = SMOTE(random_state=42).fit_resample(X_train, y_train)
# Treinar com X_train_res, avaliar com X_test original (não resampleado)
```

---

## Métricas — Quando Usar Cada Uma

| Métrica | Usar quando | Fórmula |
|---|---|---|
| **Acurácia** | Classes balanceadas | (TP+TN) / Total |
| **Precisão** | Custo alto de falso positivo | TP / (TP+FP) |
| **Recall** | Custo alto de falso negativo | TP / (TP+FN) |
| **F1-Score** | Classes desbalanceadas | 2 × (P×R)/(P+R) |
| **AUC-ROC** | Comparar modelos, threshold livre | Área sob curva ROC |
| **MAE** | Regressão, erros em mesma unidade | mean(|y - ŷ|) |
| **RMSE** | Regressão, penaliza erros grandes | sqrt(mean((y-ŷ)²)) |
| **R²** | Regressão, proporção de variância | 1 - SS_res/SS_tot |

```python
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score
)

# Classificação — sempre mostrar o report completo
print(classification_report(y_test, y_pred))

# Regressão
mae  = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2   = r2_score(y_test, y_pred)
```

---

## Overfitting vs Underfitting

```
Overfitting:  train_score >> test_score  →  modelo memorizou o treino
Underfitting: train_score ≈ test_score (ambos baixos)  →  modelo muito simples

Diagnóstico:
- Curva de aprendizado (learning curve)
- Cross-validation com k-fold

Soluções Overfitting:
- Mais dados
- Regularização (Ridge/Lasso para regressão, max_depth/min_samples para árvores)
- Dropout (redes neurais)
- Reduzir complexidade do modelo

Soluções Underfitting:
- Modelo mais complexo
- Mais features relevantes
- Menos regularização
```

```python
from sklearn.model_selection import cross_val_score, learning_curve

# Cross-validation correto
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
print(f"F1 médio: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

## Seleção de Modelos — Guia Rápido

| Situação | Modelos recomendados |
|---|---|
| Baseline rápido | LogisticRegression, DummyClassifier |
| Dataset pequeno, interpretável | DecisionTree, LogisticRegression |
| Melhor performance geral | RandomForest, XGBoost, LightGBM |
| Dados com muitas features | Lasso, Ridge, ElasticNet |
| Clustering | KMeans (n conhecido), DBSCAN (n desconhecido) |
| Dimensionalidade | PCA (linear), t-SNE (visualização), UMAP |

---

## GridSearchCV / RandomizedSearchCV

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# GridSearch — testa todas as combinações (lento, exaustivo)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}
grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1,
    verbose=1
)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

# Avaliar sempre no teste — não no best_score_ do grid (que é validação cruzada)
y_pred = grid.predict(X_test)
```

---

## Encoding de Variáveis Categóricas

```python
# OneHotEncoding — variáveis nominais (sem ordem)
from sklearn.preprocessing import OneHotEncoder
# drop=None para FIAP (não usar drop_first em avaliações acadêmicas, a menos que peçam)
enc = OneHotEncoder(drop=None, sparse_output=False)

# OrdinalEncoding — variáveis ordinais (têm ordem: baixo/médio/alto)
from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder(categories=[['baixo', 'médio', 'alto']])

# LabelEncoding — apenas para o TARGET (y), nunca para features
from sklearn.preprocessing import LabelEncoder
```

---

## Erros que Invalidam a Avaliação

1. **Fit do scaler no dataset completo antes do split** → leakage
2. **SMOTE antes do split** → leakage grave
3. **Avaliar no teste durante tuning** → overfitting otimista
4. **Usar acurácia em dataset desbalanceado** → métrica enganosa
5. **Não usar stratify no split com classes desbalanceadas** → split não representativo
6. **Comparar modelos com métricas diferentes** → comparação inválida
