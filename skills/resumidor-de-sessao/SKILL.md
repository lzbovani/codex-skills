---
name: resumidor-de-sessao
description: Gera um handoff completo da sessao atual para iniciar uma nova sessao com continuidade segura. Use quando o usuario pedir resumo da sessao, transferencia de contexto, prompt para proxima sessao, checklist de arquivos necessarios, estado de tarefas, ou retomada de trabalho sem perder historico.
---

# Resumidor De Sessao

## Objetivo

Criar um pacote de handoff para abrir uma nova sessao com contexto util e verificavel.
Priorizar continuidade sem alucinacao: manter somente fatos confirmados e sinalizar lacunas.

## Fluxo De Handoff

1. Identificar o objetivo atual da sessao e o resultado esperado na proxima.
2. Coletar apenas fatos verificaveis de historico, arquivos lidos e comandos executados.
3. Consolidar estado do trabalho: concluido, em andamento e pendente.
4. Mapear arquivos, pastas, branch e commits necessarios para continuidade.
5. Listar bloqueios, riscos e decisoes em aberto.
6. Gerar mensagem pronta para iniciar a nova sessao com instrucoes claras.

## Regras Anti-Alucinacao

1. Nao inventar arquivos, commits, resultados de teste ou decisoes.
2. Marcar cada item importante como `FATO`, `NAO VERIFICADO` ou `SUPOSICAO`.
3. Quando faltar evidencia, declarar explicitamente o que precisa ser confirmado.
4. Separar fatos observados de interpretacoes.
5. Em caso de duvida, reduzir escopo e pedir somente os dados faltantes criticos.

## Formato De Saida Padrao

Use este formato quando o usuario nao pedir outro:

1. Objetivo Atual
2. Estado Atual (somente fatos verificaveis)
3. Arquivos E Contexto Obrigatorios Para A Proxima Sessao
4. Mudancas Realizadas (com branch e commit quando existir)
5. Pendencias Prioritarias
6. Riscos, Lacunas E Itens Nao Verificados
7. Prompt Pronto Para Abrir A Proxima Sessao

## Estrutura Recomendada Da Secao "Arquivos E Contexto Obrigatorios"

Para cada item, informar:

- Caminho absoluto
- Motivo de ser necessario
- Status: `existe`, `nao encontrado`, `nao verificado`
- Acao se estiver ausente

## Prompt De Continuidade (Template)

Use e adapte o template abaixo:

```text
Continuar trabalho da sessao anterior com base nos fatos abaixo.

Objetivo: <objetivo atual>
Estado atual confirmado: <resumo objetivo>
Repositorio/branch: <repo e branch, se houver>
Arquivos obrigatorios:
- <caminho absoluto 1> - <motivo>
- <caminho absoluto 2> - <motivo>

Pendencias prioritarias:
1. <pendencia 1>
2. <pendencia 2>

Riscos e lacunas:
- <item nao verificado>

Instrucao: nao assumir fatos fora deste handoff; validar primeiro os itens marcados como NAO VERIFICADO.
```

## Gatilhos Comuns

- "Resuma essa sessao para eu continuar em outra"
- "Crie um handoff completo"
- "Me passe o contexto para nova sessao"
- "Quero encerrar e retomar depois sem perder nada"
