---
name: pdf-para-md
description: Conversao de PDF para Markdown (.md) com foco em texto limpo e legivel. Use quando o usuario precisar extrair conteudo de um PDF para editar, resumir, versionar ou reutilizar em fluxos baseados em Markdown.
---

# PDF para MD

Converter arquivos PDF em Markdown usando script local e padronizar saida para leitura e edicao.

## Fluxo

1. Receber caminho do PDF de entrada.
2. Rodar `scripts/pdf_to_md.py` para extrair texto por pagina.
3. Aplicar limpeza basica para Markdown legivel.
4. Entregar arquivo `.md` final e validar resultado.

## Como Executar

```powershell
python "C:/Users/Lucas/.codex/skills/pdf-para-md/scripts/pdf_to_md.py" "C:/caminho/arquivo.pdf"
```

Opcionalmente definir saida:

```powershell
python "C:/Users/Lucas/.codex/skills/pdf-para-md/scripts/pdf_to_md.py" "C:/caminho/arquivo.pdf" -o "C:/caminho/saida.md"
```

## Comportamento do Script

- Tenta extracao com `PyMuPDF`, depois `pdfplumber`, depois `pypdf`.
- Inclui marcacao de pagina no Markdown: `<!-- page N -->`.
- Faz limpeza de quebras de linha e hifenizacao.
- Detecta titulos obvios e converte para `##` quando apropriado.

## Qualidade e Limites

- PDFs digitalizados por imagem podem exigir OCR externo para melhor resultado.
- Tabelas complexas podem perder estrutura; revisar manualmente depois da conversao.
- Sempre revisar o `.md` final antes de uso em producao.

## Dependencias

Instalar ao menos uma biblioteca de extracao:

```powershell
pip install pymupdf
```

Alternativas:

```powershell
pip install pdfplumber
pip install pypdf
```
