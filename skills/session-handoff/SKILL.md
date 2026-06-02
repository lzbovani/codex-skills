---
name: session-handoff
description: >
  Gera um resumo completo da sessão atual para ser colado no início de uma nova conversa,
  permitindo continuidade total sem perda de contexto. Use esta skill SEMPRE que Lucas disser
  "resume a sessão", "prepara o handoff", "quero continuar em outra sessão", "faz o resumo para
  nova sessão", "status da sessão", ou qualquer variação que indique que ele quer encerrar a
  conversa atual e continuar em outra. A skill entrega: (1) um bloco de texto pronto para colar
  na nova sessão e (2) um arquivo .md para baixar e anexar. O objetivo é que a nova sessão pareça
  uma continuação natural da atual, sem alucinações.
---

# Session Handoff

Você é responsável por gerar um documento de handoff completo e preciso da sessão atual.
Seu objetivo: permitir que uma nova sessão do Claude retome o trabalho exatamente de onde parou,
sem inventar nada que não aconteceu nesta conversa.

---

## REGRA DE OURO — Anti-Alucinação

> **Documente apenas o que realmente aconteceu nesta sessão. Nunca infira, suponha ou complete
> lacunas com suposições. Se não tem certeza de algo, omita ou marque como incerto.**

---

## Passo a Passo

### 1. Varrer a sessão inteira

Releia mentalmente toda a conversa desde o início. Identifique:

- Qual era o objetivo principal da sessão?
- Quais tarefas foram iniciadas, concluídas ou ficaram pendentes?
- Quais arquivos foram gerados, modificados ou referenciados?
- Quais decisões importantes foram tomadas (técnicas, de design, de negócio)?
- Quais erros ocorreram e como foram resolvidos?
- O que ficou para a próxima sessão?

### 2. Montar o documento de handoff

O documento tem **7 seções fixas**. Preencha apenas com informações confirmadas na sessão.
Se uma seção não tiver conteúdo relevante, escreva `(nada relevante nesta sessão)`.

---

## Estrutura do Documento de Handoff

```
# 🔁 Session Handoff — [data e hora aproximada]

## 1. Contexto do Projeto / Tarefa

[Descreva em 3–5 frases o que estava sendo feito: qual projeto, qual objetivo, qual o estado
atual. Seja específico o suficiente para que alguém sem contexto entenda imediatamente.]

---

## 2. O que foi feito nesta sessão

[Lista das tarefas concluídas, em ordem cronológica. Use bullet points curtos e concretos.
Ex: "- Criou o arquivo dashboard.html com 4 abas e gráficos SVG"
    "- Corrigiu o bug de encoding no CSV de entrada"
    "- Definiu que o modelo final seria XGBoost com threshold 0.42"]

---

## 3. Arquivos gerados ou modificados

[Lista de TODOS os arquivos relevantes para a continuidade. Para cada um, informe:]

| Arquivo | Localização | Status | Descrição |
|---|---|---|---|
| nome.ext | /caminho/completo/ | ✅ Completo / 🔄 Em andamento / ⚠️ Incompleto | O que ele contém |

[Se Lucas precisar anexar algum arquivo na nova sessão, marque com 📎]

---

## 4. Decisões importantes tomadas

[Decisões técnicas, de design ou de negócio que afetam o que vem a seguir. Inclua o MOTIVO
quando relevante.
Ex: "- Escolhido Power BI em vez de Streamlit (motivo: Lucas já tem acesso corporativo)"
    "- Threshold definido como 0.42 em vez de 0.5 (motivo: minimizar falsos negativos)"]

---

## 5. Erros encontrados e como foram resolvidos

[Problemas que apareceram e as soluções aplicadas. Útil para não repetir os mesmos erros.
Ex: "- Erro de encoding UTF-8 no CSV → resolvido com encoding='latin-1' no pd.read_csv"
    "- docx-js não suportava WidthType.PERCENTAGE → trocado para WidthType.DXA"]

---

## 6. Próximos passos pendentes

[O que ainda precisa ser feito, em ordem de prioridade. Seja específico.
Ex: "1. Adicionar a aba de 'Análise Preditiva' no dashboard (estrutura já discutida)"
    "2. Testar o modelo com o dataset de validação (arquivo: validation_set.csv)"
    "3. Exportar o currículo adaptado para BTG em formato PDF"]

---

## 7. Instruções para a nova sessão

[Mensagem direta para o Claude da nova sessão. Inclua:]

**Para retomar esta sessão corretamente:**
- [Quais arquivos Lucas deve anexar na nova conversa]
- [Qual contexto específico colar no início]
- [Qualquer aviso importante para o próximo Claude não cometer erros]

**Cole isto no início da nova sessão:**
---
[BLOCO DE CONTEXTO PRONTO PARA COLAR — versão ultra-condensada do handoff, máximo 10 linhas,
escrita em 2ª pessoa para o Claude: "Você está ajudando Lucas com X. Na sessão anterior foi feito
Y. Os arquivos relevantes são Z. O próximo passo é W. Não invente nada além disto."]
---
```

---

### 3. Gerar os dois formatos de entrega

#### Formato 1 — Arquivo .md

Salve o documento completo em:
```
/mnt/user-data/outputs/session-handoff-[YYYYMMDD-HHMM].md
```

Use a data/hora aproximada da sessão no nome do arquivo.

#### Formato 2 — Bloco de texto no chat

Após apresentar o arquivo, exiba no chat o **bloco de contexto condensado** (seção 7, último
quadro) pronto para colar. Formate assim:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 COLE ISTO NO INÍCIO DA NOVA SESSÃO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[bloco condensado aqui]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Checklist de qualidade antes de entregar

Antes de gerar o output, confirme internamente:

- [ ] Tudo que documentei realmente aconteceu nesta sessão?
- [ ] Listei todos os arquivos gerados com caminhos corretos?
- [ ] O bloco condensado é suficiente para o próximo Claude entender sem contexto adicional?
- [ ] Não inventei nenhuma decisão, erro ou próximo passo que não foi mencionado?
- [ ] A lista de "arquivos para anexar" está correta e completa?

---

## Dicas de escrita

- **Seja específico nos nomes**: "dashboard.html" não "o arquivo HTML"
- **Inclua valores concretos**: "threshold=0.42", "k=25", "encoding='latin-1'"
- **Marque o status real**: se algo ficou pela metade, diga isso claramente
- **Escreva o bloco condensado como se fosse um system prompt**: direto, imperativo, sem rodeios
- **Nunca use "provavelmente", "deve ser", "acredito que"**: se não tem certeza, omita

---

## Exemplo de bloco condensado bem escrito

```
Você está ajudando Lucas Zappia (Data Science, FIAP/C6 Bank) a construir um dashboard HTML
de gestão de incidentes IT chamado PredictOps. Na sessão anterior foram criadas 4 abas
(Overview, Tendências, Equipes, Predição) com gráficos SVG e tema dark. O arquivo principal é
PredictOps_Dashboard.html (completo, funcional). O próximo passo é adicionar filtro de data
interativo na aba Overview. Não invente dados — use apenas o que Lucas fornecer.
```
