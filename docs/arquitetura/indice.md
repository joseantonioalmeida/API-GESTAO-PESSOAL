# Índice da arquitetura — API MinhaVida

| Campo | Valor |
| --- | --- |
| Documento | `docs/arquitetura/indice.md` |
| Fase | F0 — Arquitetura e reconciliação |
| Estado da F0 | **REVISADA PELO USUÁRIO.** DEC-MV-01 a 05 e DEC-MV-25 (escopo limitado) aprovadas em 2026-10-11. DEC-MV-06 a 24 pendentes |
| Data | 2026-10-10. Atualizado em 2026-10-11 |

## 1. Ordem de leitura

1. `docs/arquitetura/analise_projeto_minhavida.md`: baseline (inclusive o conteúdo do commit de baseline, §3.5), fontes, reconciliações (REC), achados (ACH), riscos e **decisões a aprovar (DEC, §9)**.
2. `docs/adr/0001_arquitetura_api_minhavida.md`: decisões D-01 a D-16.
3. `docs/adr/0002_identificadores_uuid.md`: UUIDv7 e diff do contrato.
4. `docs/arquitetura/arquitetura_api_minhavida.md`: **fonte canônica** dos contratos (escopo financeiro, módulos, HTTP, transações, concorrência, algoritmos, modelo físico, segurança e operação).
5. `docs/arquitetura/plano_fases_api.md`: fases F0–F11, grafo, fichas e cobertura.
6. `docs/arquitetura/plano_validacao_auditoria.md`: política de testes, catálogo de CTs, comandos, evidências, severidade, gates e protocolo de auditoria.
7. `docs/arquitetura/matriz_requisitos_api.md`: rastreabilidade das telas 1–11, do contrato de dados e do escopo financeiro.
8. `PROMPTS/PROMPT_MASTER_SONNET_5_F1_FUNDACAO_API.md`: Prompt Master da primeira fase (`PRONTO_PARA_ETAPA_A`).

## 2. Inventário de documentos

| Caminho | Tipo | Estado |
| --- | --- | --- |
| `CLAUDE.md` | Norma do projeto (usuário) | Vigente. Revisado em 2026-10-11 sem alteração necessária: os requisitos já tratam o financeiro como manual e a forma de pagamento como descritiva (10.2.3, 11.2.3, 11.4.3). Alterações propostas em `analise_projeto_minhavida.md` §10, **não aplicadas** (DEC-MV-06 e 22 pendentes) |
| `PROMPTS/PROMPT_MASTER_SONNET_5_IMPLEMENTACAO_BANCO_DADOS.md` | Prompt anterior (banco) | **SUSPENSO**, confirmado pelo usuário em 2026-10-11. Não usar como autorização. Substituído pela F2 do plano. Arquivo não alterado |
| `docs/adr/0001_arquitetura_api_minhavida.md` | ADR | **PARCIALMENTE ACEITO**: D-01, D-02, D-03, D-04, D-08 e D-14 aceitas; D-09 aceita somente na convenção de nomes (DEC-MV-25). Demais PROPOSTAS |
| `docs/adr/0002_identificadores_uuid.md` | ADR | PROPOSTO (DEC-MV-06). Não alterado |
| `docs/arquitetura/analise_projeto_minhavida.md` | Análise | PROPOSTO, com DEC-MV-01 a 05 e 25 aprovadas |
| `docs/arquitetura/arquitetura_api_minhavida.md` | Arquitetura | **PARCIALMENTE ACEITO**: §2, §4.4, §5, §3 (itens da F1) e §10.1 somente na convenção de nomes. §1.1 registra instrução do usuário |
| `docs/arquitetura/matriz_requisitos_api.md` | Rastreabilidade | PROPOSTO |
| `docs/arquitetura/plano_fases_api.md` | Plano | PROPOSTO. Todas as decisões da F1 aprovadas |
| `docs/arquitetura/plano_validacao_auditoria.md` | Validação e auditoria | **PARCIALMENTE ACEITO**: §2, §3, §5 e catálogo da F1 (DEC-MV-04) |
| `PROMPTS/PROMPT_MASTER_SONNET_5_F1_FUNDACAO_API.md` | Prompt Master F1 | **`PRONTO_PARA_ETAPA_A`** (2026-10-11). Etapa B dependente do baseline e de “pode implementar” |

## 3. Precedência normativa

1. Instruções explícitas do usuário na sessão corrente, dentro do escopo.
2. `CLAUDE.md`.
3. ADRs **ACEITOS**, por decisão. Um ADR aceito que substitua expressamente uma cláusula do `CLAUDE.md` (ADR-0002 → tipos de ID) prevalece sobre ela. O gate da fase afetada, porém, exige o `CLAUDE.md` já atualizado, para que não haja duas fontes contraditórias vigentes.
4. `arquitetura_api_minhavida.md`, `plano_fases_api.md`, `plano_validacao_auditoria.md` e `matriz_requisitos_api.md`, que precisam estar conformes a 2 e 3.
5. Prompt Master da fase (operacional).
6. O prompt anterior do banco não tem precedência (SUSPENSO).

Regras complementares:

- Documentos e decisões PROPOSTOS não autorizam implementação.
- Uma decisão aceita alcança as seções de detalhe que ela cita **somente na parte que detalha essa decisão**. Partes dessas seções que servem a fases posteriores seguem as decisões dessas fases (por exemplo, as variáveis de F3 e F9 na arquitetura §3.1).
- Uma aprovação com escopo limitado vale só para os itens nomeados. Exemplo: DEC-MV-25 aceita a convenção de nomes, e o restante de D-09 segue PROPOSTO.
- Conflito entre textos aceitos: aplica-se a ordem acima até o usuário decidir. Caso registrado: REC-MV-029. Até DEC-MV-24, vale ADR-0001 D-02 sobre a arquitetura §2.2. Nenhuma fase até a F4 é afetada.
- Instruções de escopo do usuário são registradas em §4 e no documento canônico correspondente (escopo financeiro: arquitetura §1.1).

## 4. Registro de aprovações

> Preenchido somente mediante aprovação explícita do usuário, com data e escopo. Uma aprovação não se estende a decisões ou documentos não citados.

Referências das mensagens do usuário, ambas de 2026-10-11 na sessão `8f60e6c4-621a-44be-a17d-8b16d858086c`:

- **M1:** primeira mensagem do dia, com o texto “Aprovo as seguintes decisões, conforme descritas em `docs/arquitetura/analise_projeto_minhavida.md`, seção 9: DEC-MV-01. DEC-MV-02. DEC-MV-03. DEC-MV-04. DEC-MV-05.”
- **M2:** segunda mensagem do dia, com o texto “Aprovo expressamente a DEC-MV-25.”

Os itens de cada mensagem são citados entre parênteses.

| Data | Decisão / documento | Escopo aprovado | Referência | Registrado por |
| --- | --- | --- | --- | --- |
| 2026-10-11 | DEC-MV-01 | Conforme `analise` §9: monólito em camadas `routers → services → models`, sem repository; organização de diretórios e nomenclatura; driver psycopg 3. Aceita ADR-0001 D-01, D-02 e D-03 e a arquitetura §2. Ressalva: conflito interno entre D-02 e §2.2 (REC-MV-029), pendente em DEC-MV-24 | M1 (item 1) | Opus |
| 2026-10-11 | DEC-MV-02 | Sessão por requisição com autobegin; commit explícito apenas no router; service só com `flush`; jobs donos da própria transação; engine no `lifespan`. Aceita D-04 (e D-03), a arquitetura §5 e os itens da F1 da arquitetura §3 | M1 (item 1) | Opus |
| 2026-10-11 | DEC-MV-03 | `ErroNegocio`, formato JSON único, catálogo de códigos, validação sem eco. Aceita D-08 e a arquitetura §4.4 | M1 (item 1) | Opus |
| 2026-10-11 | DEC-MV-04 | Testes direcionados; suíte completa como exceção; Testcontainers `postgres:15-alpine`; Ruff de verificação com `--no-fix`; `task test` fora dos gates. Aceita D-14 e o plano de validação §2, §3, §5 e o catálogo da F1 | M1 (item 1) | Opus |
| 2026-10-11 | DEC-MV-05 | Higiene da F1, conforme `analise` §9: `compose.yaml` com `.env` em `127.0.0.1`, `.gitignore`, `requires-python >=3.14`, `pydantic-settings` direto, `httpx` dev, remoção da rota `/` e de `schemas/message.py`, criação de `__init__.py`. Não corresponde a uma decisão do ADR | M1 (item 1) | Opus |
| 2026-10-11 | **DEC-MV-25 (escopo limitado)** | **Somente** a convenção `CONVENCAO_NOMES`, conforme a arquitetura §10.1 e o Prompt F1 §6, com os padrões `pk`, `uq`, `ck`, `fk` e `ix` preservados exatamente, e sua aplicação ao `Base.metadata` por `MetaData(naming_convention=CONVENCAO_NOMES)` na F1. Aceita D-09 apenas nesse item | M2 (item 1) | Opus |
| 2026-10-11 | **Fora da aprovação de DEC-MV-25** | Restante de DEC-MV-07 e de D-09; DEC-MV-06 e ADR-0002; tabelas, migrações e seeds de domínio; alterações no `TimestampMixin`; `eager_defaults`; qualquer outra decisão pendente; a implementação da F1 | M2 (item 1) | Opus |
| 2026-10-11 | **Fora das aprovações deste dia** | DEC-MV-06 a 24; ADR-0001 como um todo e suas decisões D-05 a D-07, D-10 a D-13, D-15 e D-16; ADR-0002; a implementação da F1, que depende do baseline e de “pode implementar”; a aprovação de qualquer fase. DEC-MV-24 permanece pendente, para decisão antes da F5 | M1 (itens 1, 4 e 6) e M2 (itens 1 e 3) | Opus |
| 2026-10-11 | Instrução de escopo financeiro | Financeiro manual, com totais e saldo calculados a partir dos lançamentos; sem integrações financeiras externas nem infraestrutura “para uso futuro”; forma de pagamento descritiva; recuperação de senha por e-mail preservada. Registrado na arquitetura §1.1 (REC-MV-028). Reafirmado na M2 | M1 (itens 2 e 3) e M2 (item 1) | Opus |
| 2026-10-11 | Nomenclatura da F8 | F8 passa a se chamar “Vínculo interno entre despesas e importâncias”, com o mesmo identificador. Não autoriza implementar a F8 nem aprova decisões pendentes | M1 (item 4) | Opus |
| 2026-10-11 | Prompt anterior do banco | Permanece SUSPENSO | M1 (item 6) e M2 (item 2) | Opus |
| 2026-10-11 | Baseline sem credenciais | Instrução do usuário: baseline verificável antes da implementação, sem credenciais no histórico. Orientação em `analise` §3.5 (REC-MV-032). **Não** é exceção ao ACH-MV-ARQ-019, que segue ABERTO | M2 (item 3) | Opus |

## 5. Estado dos gates

| Gate | Estado | Observação |
| --- | --- | --- |
| G0 — Baseline e fontes | **Cumprido** | Fontes lidas e lacunas registradas (`analise` §2). Hashes conferidos novamente em 2026-10-11 |
| G1 — Arquitetura da F1 | **Cumprido** (2026-10-11) | DEC-MV-01 a 05 e DEC-MV-25 aceitas |
| G1 — demais fases | AGUARDANDO_DECISAO | DEC-MV-06 a 24, conforme `analise` §9 |
| G2 — Prompt Master F1 | **Cumprido**: `PRONTO_PARA_ETAPA_A` | Coerente com as fontes aceitas. Sem “a definir” |
| G3 — Etapa A da F1 | Não iniciado | Liberado para envio ao Sonnet |
| Pré-condição da Etapa B da F1 | **ABERTO** | ACH-MV-ARQ-019 (P2): commit de baseline com o conteúdo de `analise` §3.5, verificado pela revalidação do Prompt F1 §1.2, ou exceção aceita expressamente pelo usuário. Nenhuma exceção foi registrada |
| Autorização da Etapa B | Não concedida | Depende de “pode implementar”, dado pelo usuário após a Etapa A |
| G4 a G6 | Não iniciados | — |

Pendências que bloqueiam algo:

| Pendência | Fonte | Impacto | Resolução (usuário) |
| --- | --- | --- | --- |
| ACH-MV-ARQ-019 aberto (P2) | `analise` §3.1 e §3.5, REC-MV-031 e 032 | A Etapa B da F1 não começa. A Etapa A, somente leitura, pode ocorrer | Commit de baseline com a lista explícita de `analise` §3.5, sem o `compose.yaml` |
| DEC-MV-24 pendente | REC-MV-029, ACH-MV-ARQ-021 | Não afeta F1 a F4. Bloqueia a F5 | Decidir antes do Prompt Master da F5 |

## 6. Autoverificação dos critérios de aceite da sessão (F0)

| Critério | Situação | Evidência |
| --- | --- | --- |
| Fontes efetivamente lidas. Ausências e truncamentos declarados | Atendido | `analise` §1, §2, §2.2 (linhas 3, 10 e 12 do `CLAUDE.md`; anexos ausentes) |
| Baseline separado de propostas e decisões | Atendido | Legenda OBSERVADO / EXIGIDO / PROPOSTO / NÃO VERIFICADO. `analise` §3. Hashes abreviados de §3.2 corrigidos (ACH-MV-ARQ-023). Conteúdo do commit de baseline em §3.5 |
| INT/UUID com proposta concreta, impacto e gate | Atendido | ADR-0002 (diff de 32 colunas). DEC-MV-06. Gate F2 |
| Stack alvo e “service sem commit” refletidos | Atendido | ADR-0001 D-04 (aceita). Arquitetura §5. Prompt F1 §0 e §8.2 |
| Telas 1–11 e contrato rastreados até fase e teste | Atendido | `matriz_requisitos_api.md`, inclusive o escopo financeiro (ESC-FIN-1 a 5) |
| Decisões da F1 fechadas ou bloqueando a liberação | Atendido | DEC-MV-01 a 05 e 25 aprovadas. Prompt F1 em `PRONTO_PARA_ETAPA_A` |
| Nenhuma fase depende silenciosamente de capacidade futura | Atendido | `plano_fases_api.md` §1 e §2 (F6 sem `importancia_id`; F8 aditiva). Dependência da F5 em DEC-MV-24 explicitada |
| Operações críticas com fronteira, mecanismo e resultado | Atendido | Arquitetura §6.6 (15 corridas com CT) |
| Política de testes direcionados, sem gatilho de suíte completa | Atendido | `plano_validacao` §2. `task test` proibido |
| Modo Cloud preserva a auditoria local e o merge pelo usuário | Atendido | `plano_validacao` §10. Prompt F1 §0 |
| Auditoria com evidência real, sem alterar o objeto e sem correções pelo auditor | Atendido | `plano_validacao` §9. Ruff `--no-fix` (ACH-MV-ARQ-008) |
| Sem instruções contraditórias vigentes simultaneamente | Atendido, com ressalvas | Prompt anterior SUSPENSO. Diffs do `CLAUDE.md` pendentes (até lá o `CLAUDE.md` prevalece). Conflito D-02 × §2.2 entre textos aceitos, com regra provisória de precedência (§3) e decisão pendente (DEC-MV-24) |
| Severidade aplicada sem redução para liberar fase | Atendido | ACH-MV-ARQ-019 mantido em P2 e ABERTO, sem exceção registrada (REC-MV-031 e 032) |
| Baseline sem credenciais no histórico | Atendido na orientação | `analise` §3.5: lista explícita de 22 arquivos, `compose.yaml` fora. Orientação anterior corrigida (ACH-MV-ARQ-024). Execução pendente do usuário |
| Etapa A sem commit e Etapa B bloqueada, sem contradição | Atendido | Prompt F1 §1.1, §1.2 e §14, passo 0 (revalidação do baseline) |
| Nada implementado. Nenhum teste apresentado como executado | Atendido | Somente arquivos em `docs/` e o Prompt Master F1. Todos os testes estão PLANEJADOS. Nenhum `git add` ou commit executado |

Verificação documental (não é teste de implementação), refeita em 2026-10-11 após a aprovação de DEC-MV-25:

- Todos os IDs CT, DEC, REC, ACH e ESC-FIN citados existem no documento de origem (173 CTs, 25 DECs, 32 RECs, 25 ACHs e 5 ESC-FIN).
- Todas as referências `§` da arquitetura existem. As referências `§` entre documentos (análise, índice, planos, ADRs e Prompt F1) foram conferidas contra os títulos de seção.
- Cercas de código balanceadas em todos os documentos.
- Nenhuma credencial do `compose.yaml` reproduzida nos documentos.
- A convenção de nomes tem os mesmos cinco padrões na arquitetura §10.1, no ADR-0001 D-09 e no Prompt F1 §6.
- A lista de 22 arquivos de `analise` §3.5 corresponde aos arquivos não ignorados do repositório, menos `compose.yaml` e `__pycache__/`.
- O nome antigo da F8 só aparece como registro histórico: `plano_fases_api.md` §1 e REC-MV-028.
- Arquivos protegidos (`CLAUDE.md`, prompt anterior, código e configuração) com os hashes do baseline.

## 7. Próxima ação do usuário

1. Revisar a orientação de baseline em `analise` §3.5 e criar o commit com a **lista explícita** de 22 arquivos, sem o `compose.yaml`. Não usar `git add -A` nem `git add .`. Recomendado antes de enviar o prompt. Também é permitido depois da Etapa A: nesse caso, o Sonnet revalida o baseline no início da Etapa B (Prompt F1 §1.2).
2. Enviar `PROMPTS/PROMPT_MASTER_SONNET_5_F1_FUNDACAO_API.md` ao Sonnet. Ele executa **somente a Etapa A** e termina com “Aguardo ‘pode implementar’ para a F1.”
3. Revisar o relatório da Etapa A. Responder “pode implementar” somente com o commit de baseline feito.
4. Depois da F1, preencher o `.env` conforme o Prompt F1 §9.3.
5. Antes da F5: decidir DEC-MV-24. Antes da F2: DEC-MV-06 a 08 e a atualização do `CLAUDE.md`.
6. Opcional: restaurar as linhas truncadas do `CLAUDE.md` (ACH-MV-ARQ-012).
