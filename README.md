# codex-skills

Repositorio de backup, versionamento e sincronizacao das skills pessoais do Codex.

As skills ficam em `skills/<nome-da-skill>` e normalmente seguem esta estrutura:

- `SKILL.md`: instrucoes principais da skill.
- `agents/openai.yaml`: nome, descricao curta e prompt padrao exibidos no seletor `$`.
- `references/`: materiais extras carregados somente quando a skill precisar.

## Skills Disponiveis

| Skill | Tipo | Descricao curta | Melhor uso |
|---|---|---|---|
| `analista-de-dados` | Dados | Mentoria senior para estudos e projetos academicos de dados. | Exercicios, provas, listas e explicacoes didaticas. |
| `analista-de-dados-codex` | Dados | Analise de dados profissional com foco em validacao, suposicoes e reducao de erro tecnico. | Projetos mais rigorosos, revisao de analises, SQL, estatistica, ML, Python, R e Power BI. |
| `analista-de-dados-claude` | Dados | Versao mais personalizada, com referencias separadas para SQL, estatistica, ML, Power BI e Python. | Estudo guiado e consultas detalhadas por area, especialmente quando referencias especificas ajudam. |
| `analista-de-dados-codex-e-claude` | Dados | Fusao das abordagens Codex e Claude, com modo anti-erro e estrutura robusta. | Quando quiser a versao mais completa para dados, estudo, projetos e comunicacao de resultados. |
| `criador-de-prompts` | Prompts | Cria prompts fortes com perguntas criticas antes da geracao final. | Prompts profundos, profissionais, multiuso e com refinamento iterativo. |
| `prompt-engineer` | Prompts | Cria e otimiza prompts com uma abordagem mais direta e calibrada por perguntas. | Prompts objetivos para codigo, texto, imagem, agentes e automacoes. |
| `editor-de-curriculo-por-vaga` | Carreira | Adapta curriculo para vagas especificas sem inventar informacoes. | Ajustar resumo, experiencias, palavras-chave ATS e carta curta. |
| `gerador-de-ppt-por-tema` | Apresentacoes | Cria estrutura de apresentacao a partir de um tema. | Montar narrativa, divisao de slides, texto e sugestoes visuais. |
| `pdf-para-md` | Conversao | Converte PDF para Markdown limpo e editavel. | Extrair conteudo de PDF para editar, versionar ou reutilizar. |
| `pesquisador-profundo-web` | Pesquisa | Pesquisa profunda na web com triangulacao de fontes e sintese confiavel. | Investigar temas atuais, comparar fontes e gerar dossies com links. |
| `resumidor-universal` | Resumo | Resume PDF, Word, texto, Markdown e codigo-fonte. | Sintese rapida, pontos-chave, riscos e proximos passos. |
| `resumidor-de-sessao` | Continuidade | Gera handoff verificavel da sessao atual para uma nova sessao. | Continuar trabalho em outro chat com contexto essencial e sem alucinacao. |
| `session-handoff` | Continuidade | Handoff completo e detalhado, com documento estruturado e bloco condensado. | Encerrar uma sessao longa e retomar em outra com maximo contexto. |
| `status-sobre-mim` | Contexto pessoal | Gera snapshot sobre o usuario com fatos, inferencias e incertezas. | Portar contexto pessoal entre IAs sem misturar fato com suposicao. |

## Comparacoes Por Familia

### Skills De Dados

| Skill | Perfil | Quando escolher |
|---|---|---|
| `analista-de-dados` | Mais simples e academica. | Use para duvidas rapidas de faculdade, explicacoes e exercicios diretos. |
| `analista-de-dados-codex` | Mais profissional, verificavel e anti-erro. | Use quando a resposta precisa ser tecnicamente mais cuidadosa e validar metodo, suposicoes e resultado. |
| `analista-de-dados-claude` | Mais personalizada e apoiada por referencias por area. | Use quando quiser uma mentoria mais guiada e detalhada em SQL, estatistica, ML, Power BI ou Python. |
| `analista-de-dados-codex-e-claude` | Mais completa, combinando rigor profissional e didatica. | Use como escolha principal quando quiser maxima qualidade em dados. |

Recomendacao padrao: use `analista-de-dados-codex-e-claude` para trabalhos importantes e `analista-de-dados-codex` para revisoes tecnicas mais objetivas.

### Skills De Prompts

| Skill | Perfil | Quando escolher |
|---|---|---|
| `prompt-engineer` | Mais enxuta, direta e orientada a montar prompts claros rapidamente. | Use quando quiser um prompt bom e objetivo sem uma estrutura muito extensa. |
| `criador-de-prompts` | Mais profunda, profissional e focada em prompts robustos. | Use quando quiser extrair o maximo da IA, com perguntas criticas, prompt principal, versao alternativa e refinamento. |

Recomendacao padrao: use `prompt-engineer` para velocidade e `criador-de-prompts` para qualidade maxima.

### Skills De Continuidade De Sessao

| Skill | Perfil | Quando escolher |
|---|---|---|
| `resumidor-de-sessao` | Handoff mais objetivo, com fatos verificados, arquivos e pendencias. | Use para trocar de sessao mantendo contexto essencial. |
| `session-handoff` | Handoff mais completo e documental, com estrutura fixa de 7 secoes. | Use para sessoes longas, projetos complexos ou quando quiser um documento completo para anexar. |
| `status-sobre-mim` | Snapshot do perfil do usuario, nao da sessao. | Use para levar preferencias, contexto pessoal e dados confirmados para outra IA. |

Recomendacao padrao: use `resumidor-de-sessao` para continuidade rapida, `session-handoff` para continuidade detalhada e `status-sobre-mim` para contexto pessoal.

### Skills De Resumo E Conversao

| Skill | Perfil | Quando escolher |
|---|---|---|
| `resumidor-universal` | Entende e resume conteudo. | Use quando quiser sintese, pontos-chave, riscos, explicacao ou proximos passos. |
| `pdf-para-md` | Converte arquivo, sem foco principal em interpretacao. | Use quando precisar transformar PDF em Markdown limpo antes de editar, versionar ou resumir. |

Recomendacao padrao: use `pdf-para-md` para extrair o conteudo e `resumidor-universal` para entender o conteudo.

### Skills Individuais

| Skill | Diferencial |
|---|---|
| `pesquisador-profundo-web` | Melhor para temas atuais ou incertos, porque exige pesquisa, fontes e triangulacao. |
| `editor-de-curriculo-por-vaga` | Melhor para carreira, ATS e aderencia entre curriculo e vaga sem inventar experiencia. |
| `gerador-de-ppt-por-tema` | Melhor para transformar assunto solto em narrativa de apresentacao. |

## Como Escolher Rapido

| Se voce quer... | Use |
|---|---|
| Resolver ou revisar algo de dados com rigor | `analista-de-dados-codex-e-claude` |
| Uma resposta de dados mais objetiva e profissional | `analista-de-dados-codex` |
| Criar um prompt profundo e muito bem calibrado | `criador-de-prompts` |
| Criar um prompt bom com menos complexidade | `prompt-engineer` |
| Resumir um arquivo, texto ou codigo | `resumidor-universal` |
| Continuar uma conversa em outra sessao | `resumidor-de-sessao` |
| Fazer um handoff longo e documental | `session-handoff` |
| Converter PDF para Markdown | `pdf-para-md` |
| Pesquisar algo atual na internet | `pesquisador-profundo-web` |
| Adaptar curriculo para uma vaga | `editor-de-curriculo-por-vaga` |
| Criar uma apresentacao por tema | `gerador-de-ppt-por-tema` |

## Sincronizacao

Este repositorio tambem guarda as skills instaladas localmente em:

`C:\Users\Lucas\.codex\skills`

Ao editar ou criar skills, o fluxo recomendado e:

1. Atualizar a skill local.
2. Espelhar para `skills/<nome-da-skill>` neste repositorio.
3. Fazer commit.
4. Fazer push para `main`.
