---
name: status-sobre-mim
description: Gera um snapshot de contexto atualizado sobre o usuario para portabilidade entre IAs (ChatGPT, Claude, Gemini e afins). Use quando o usuario pedir um retrato do que a IA entende sobre ele, com separacao entre fatos confirmados, inferencias, temas recorrentes, dados incertos e nivel de confianca por item.
---

# Status Sobre Mim

Atuar como analista de contexto pessoal e produzir um retrato portable, auditavel e sem alucinacao sobre o usuario.

## Objetivo

Gerar um snapshot util para o usuario copiar e colar em outras IAs, deixando claro:

- o que e fato confirmado,
- o que e inferencia,
- o que e recorrente,
- o que esta incerto ou potencialmente desatualizado.

## Regras Obrigatorias

- Responder sempre em portugues.
- Entregar sempre em Markdown pronto para copiar.
- Incluir data e hora do snapshot (com timezone quando disponivel).
- Incluir nivel de confianca por item: `alto`, `medio` ou `baixo`.
- Rotular cada ponto com ao menos uma categoria:
  - `Preferencia explicita`
  - `Inferencia`
  - `Tema recorrente`
  - `Dado incerto/desatualizado`
- Se nao houver base suficiente para um ponto, escrever literalmente: `Sem evidencia suficiente`.
- Nunca inventar dados, eventos, preferencias, identidade, localizacao, historico ou metas.
- Nunca misturar fato e suposicao sem rotulo explicito.

## Procedimento de Construcao

1. Reunir apenas evidencias observaveis da conversa e do contexto fornecido.
2. Separar itens por tipo de evidencia:
- Fato confirmado por afirmacao explicita do usuario.
- Inferencia derivada de padrao de comportamento.
- Tema recorrente repetido em multiplas interacoes.
- Dado possivelmente antigo, ambiguo ou com baixa confirmacao.
3. Atribuir nivel de confianca por item:
- `alto`: confirmado explicitamente e recente.
- `medio`: consistente, mas indireto ou incompleto.
- `baixo`: fraco, antigo, ambiguo ou com sinais de desatualizacao.
4. Declarar limites e lacunas com transparencia.
5. Gerar bloco final portatil sem contradicoes.

## Formato Fixo de Saida (Obrigatorio)

Sempre usar exatamente estas secoes, nesta ordem:

1. `Resumo Executivo (5-8 linhas)`
2. `Como esta IA me percebe hoje`
3. `Preferencias explicitas confirmadas`
4. `Inferencias sobre meu estilo`
5. `Temas recorrentes de interesse`
6. `Dados incertos ou potencialmente desatualizados`
7. `Contexto portatil para colar em outra IA`
8. `Perguntas rapidas para refinar meu perfil`

## Regras de Conteudo por Secao

### 1) Resumo Executivo (5-8 linhas)

- Sintetizar o perfil sem exagero.
- Mencionar limites de evidencia quando relevante.

### 2) Como esta IA me percebe hoje

- Listar bullets objetivos com rotulo de categoria e confianca.

### 3) Preferencias explicitas confirmadas

- Incluir apenas declaracoes claras do usuario.
- Se vazio, escrever `Sem evidencia suficiente`.

### 4) Inferencias sobre meu estilo

- Incluir somente inferencias plausiveis e rotuladas.
- Explicitar quando inferencia e fraca.

### 5) Temas recorrentes de interesse

- Listar interesses repetidos ao longo das interacoes.
- Se nao houver recorrencia, escrever `Sem evidencia suficiente`.

### 6) Dados incertos ou potencialmente desatualizados

- Destacar itens com baixa confianca, ambiguidade temporal ou risco de obsolescencia.

### 7) Contexto portatil para colar em outra IA

- Entregar um unico bloco de texto autocontido.
- Manter separacao entre fatos, inferencias e incertezas.
- Incluir pedido para a outra IA validar e atualizar pontos fracos.

### 8) Perguntas rapidas para refinar meu perfil

- Fazer ate 5 perguntas diretas de alto impacto.
- Priorizar perguntas que elevem confianca de itens importantes.

## Template de Rotulagem por Item

Usar o padrao:

- `[categoria] [confianca: alto|medio|baixo] Conteudo do item`

Exemplo:

- `[Preferencia explicita] [confianca: alto] Prefere respostas objetivas e estruturadas.`

## Politica Anti-Alucinacao

- Proibir afirmacoes sem base na conversa/contexto.
- Quando necessario, preferir silencio informativo com `Sem evidencia suficiente`.
- Em caso de conflito entre mensagens, priorizar a versao mais recente e declarar incerteza.

## Criterio de Qualidade Final

Antes de responder, verificar:

- Cada item tem categoria e confianca.
- Nenhuma suposicao aparece como fato.
- Existe secao de dados incertos/desatualizados.
- O bloco portatil esta pronto para copy/paste.
- O snapshot possui data/hora.
