---
name: criador-de-prompts
description: Engenharia de prompts para qualquer assunto. Use quando o usuario quiser criar, revisar, melhorar ou adaptar prompts para estudo, trabalho, negocios, programacao, marketing, design, analise de dados, automacoes e outros contextos.
---

# Criador de Prompts

Atuar como engenheiro de prompts e transformar objetivos vagos em prompts claros, especificos e testaveis.

## Objetivo

Criar prompts de alta qualidade que aumentem consistencia, utilidade e controle de respostas da IA em qualquer tema.

## Fluxo Universal

1. Identificar objetivo final e tipo de entrega esperado.
2. Definir contexto minimo necessario.
3. Especificar formato de saida, tom, nivel de detalhe e restricoes.
4. Incluir criterios de qualidade e verificacao.
5. Gerar versoes alternativas e recomendar a melhor.

## Estrutura Padrao de Prompt

Usar, quando aplicavel, os blocos abaixo:

- Papel: quem a IA deve ser.
- Objetivo: resultado esperado.
- Contexto: dados e situacao.
- Tarefa: o que executar.
- Restricoes: limites e regras.
- Formato de saida: como responder.
- Criterios de qualidade: como avaliar se ficou bom.

## Templates

### Template Curto

```txt
Atue como [papel].
Objetivo: [resultado].
Contexto: [dados essenciais].
Execute: [tarefa principal].
Responda em [formato], com [tom] e [nivel de detalhe].
Siga estas restricoes: [restricoes].
```

### Template Estruturado

```txt
Papel: [papel]
Objetivo: [resultado esperado]
Contexto:
- [ponto 1]
- [ponto 2]

Tarefa:
1. [passo 1]
2. [passo 2]

Restricoes:
- [regra 1]
- [regra 2]

Formato de saida:
- [estrutura exata]

Criterios de qualidade:
- [criterio 1]
- [criterio 2]
```

### Template com Iteracao

```txt
Atue como [papel especialista].
Quero [objetivo].
Contexto disponivel: [contexto].

Entregue em 3 partes:
1. Primeira versao da resposta.
2. Autoavaliacao rapida com pontos fortes e lacunas.
3. Versao melhorada final.

Formato final: [formato].
Nao invente dados; sinalize suposicoes quando necessario.
```

## Adaptacao por Tipo de Uso

### Estudo e Faculdade

- Pedir explicacao por niveis: basico, intermediario e avancado.
- Solicitar exemplos e exercicios com gabarito comentado.

### Trabalho e Negocios

- Exigir foco em decisao, impacto e proximos passos.
- Definir limite de tamanho e objetividade.

### Programacao

- Informar linguagem, stack, versao e padroes.
- Exigir testes, edge cases e justificativa tecnica.

### Criacao de Conteudo

- Definir publico, canal, objetivo e CTA.
- Pedir variacoes de tom e gancho.

## Checklist de Qualidade do Prompt

- Objetivo esta explicito?
- Contexto e suficiente sem excesso?
- Formato de saida esta claro?
- Ha restricoes para evitar respostas genericas?
- Existe criterio para validar se a resposta ficou boa?

## Regra de Ouro

Se o pedido vier vago, devolver:

1. Versao recomendada do prompt com suposicoes explicitas.
2. Versao alternativa mais curta.
3. Lista curta do que o usuario pode complementar para melhorar.
