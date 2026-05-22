---
name: resumidor-universal
description: Resume conteudos enviados pelo usuario em PDF, Word (DOCX), texto puro, Markdown e codigo-fonte. Use quando o usuario pedir resumo, sintese, explicacao curta, visao geral, pontos-chave, highlights, takeaways ou material de estudo a partir de documentos e arquivos tecnicos.
---

# Resumidor Universal

## Objetivo

Produza resumos claros, fieis ao material original e adaptados ao objetivo do usuario.
Priorize utilidade pratica: entendimento rapido, decisao e estudo.

## Fluxo Padrao

1. Identifique o tipo de conteudo e o objetivo do resumo.
2. Detecte o nivel de profundidade pedido pelo usuario.
3. Extraia as ideias centrais sem copiar trechos longos literalmente.
4. Reorganize o conteudo em ordem logica.
5. Entregue o resumo no formato mais util para aquele contexto.

## Regras De Qualidade

1. Nao invente fatos.
2. Sinalize ambiguidades ou lacunas com clareza.
3. Preserve termos tecnicos importantes quando necessario.
4. Ajuste linguagem ao idioma e ao nivel do usuario.
5. Em codigo, destaque comportamento, arquitetura e riscos, nao apenas sintaxe.

## Formatos De Saida

Use o formato abaixo como padrao quando o usuario nao definir outro:

- Resumo curto: 3-5 linhas com a ideia principal.
- Pontos-chave: 5-10 bullets objetivos.
- Riscos, duvidas ou limites: itens que podem afetar entendimento ou decisao.
- Proximos passos: acoes praticas sugeridas.

## Adaptacoes Por Tipo De Conteudo

### PDF e Word

Preserve estrutura semantica (titulo, secoes, conclusao) e destaque argumentos centrais.
Se o documento for longo, resuma por secao e depois gere uma sintese final.

### Texto e Markdown

Extraia tese principal, evidencias, contrapontos e conclusao.
Quando houver lista de tarefas, converta em plano de acao curto.

### Codigo-Fonte

Explique:
1. objetivo do codigo;
2. fluxo principal de execucao;
3. componentes/funcoes relevantes;
4. riscos, bugs potenciais e pontos de manutencao.

## Pedidos Comuns Que Devem Disparar Esta Skill

- "Resuma este PDF em 10 pontos."
- "Faz um resumo desse DOCX para estudo."
- "Me explica esse codigo rapidinho."
- "Quero a sintese desse texto com acoes praticas."
