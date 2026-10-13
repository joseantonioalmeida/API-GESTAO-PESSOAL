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
8. `PROMPTS/PROMPT_MASTER_SONNET_5_F1_FUNDACAO_API.md`: Prompt Master da primeira fase, executado. F1 `APROVADO_COM_P3`, aguardando integração.
9. `docs/auditorias/AUDITORIA_F1_FUNDACAO_API.md` e `docs/auditorias/REAUDITORIA_F1_CORRECOES_POS_AUDITORIA.md`: auditoria da F1 (`BLOQUEADO`, histórico) e reauditoria das correções (`APROVADO_COM_P3`), com os achados ACH-MV-F1-001 a 007. O prompt das correções está em `PROMPTS/PROMPT_MASTER_SONNET_5_F1_CORRECOES_POS_AUDITORIA.md`.

## 2. Inventário de documentos

| Caminho | Tipo | Estado |
| --- | --- | --- |
| `CLAUDE.md` | Norma do projeto (usuário) | Vigente. Revisado em 2026-10-11 sem alteração necessária: os requisitos já tratam o financeiro como manual e a forma de pagamento como descritiva (10.2.3, 11.2.3, 11.4.3). Alterações propostas em `analise_projeto_minhavida.md` §10, **não aplicadas** (DEC-MV-06 e 22 pendentes) |
| `PROMPTS/PROMPT_MASTER_SONNET_5_IMPLEMENTACAO_BANCO_DADOS.md` | Prompt anterior (banco) | **SUSPENSO**, confirmado pelo usuário em 2026-10-11. Não usar como autorização. Substituído pela F2 do plano. Arquivo não alterado |
| `docs/adr/0001_arquitetura_api_minhavida.md` | ADR | **PARCIALMENTE ACEITO**: D-01, D-02, D-03, D-04, D-08 e D-14 aceitas; D-09 aceita somente na convenção de nomes (DEC-MV-25). Demais PROPOSTAS |
| `docs/adr/0002_identificadores_uuid.md` | ADR | PROPOSTO (DEC-MV-06). Não alterado |
| `docs/arquitetura/analise_projeto_minhavida.md` | Análise | PROPOSTO, com DEC-MV-01 a 05, 25 e 26 aprovadas |
| `docs/arquitetura/arquitetura_api_minhavida.md` | Arquitetura | **PARCIALMENTE ACEITO**: §2, §4.4, §5, §3 (itens da F1) e §10.1 somente na convenção de nomes. §1.1 registra instrução do usuário. §3.4 ganhou o limite de `hide_parameters` e o contrato de log do 500 de banco (P-DOC-03) |
| `docs/arquitetura/matriz_requisitos_api.md` | Rastreabilidade | PROPOSTO |
| `docs/arquitetura/plano_fases_api.md` | Plano | PROPOSTO. F1 `APROVADO_COM_P3`, aguardando integração |
| `docs/arquitetura/plano_validacao_auditoria.md` | Validação e auditoria | **PARCIALMENTE ACEITO**: §2, §3, §5 e catálogo da F1 (DEC-MV-04), com CT-F1-21 e 22 acrescentados (P-DOC-04) |
| `PROMPTS/PROMPT_MASTER_SONNET_5_F1_FUNDACAO_API.md` | Prompt Master F1 | **Executado.** F1 `APROVADO_COM_P3` (reauditoria de 2026-10-11). §8.5, §11.1 e §14, passo 10, atualizados (P-DOC-01, 02 e 06). Histórico: `PRONTO_PARA_ETAPA_A` em 2026-10-11 |
| `PROMPTS/PROMPT_MASTER_SONNET_5_F1_CORRECOES_POS_AUDITORIA.md` | Prompt de correções da F1 | **Executado** e verificado na reauditoria. Preservado sem alteração como evidência histórica (a emenda `env_file=None` está registrada no §4) |
| `docs/auditorias/AUDITORIA_F1_FUNDACAO_API.md` | Relatório de auditoria | Evidência histórica: F1 `BLOQUEADO` em 2026-10-11. Não alterar |
| `docs/auditorias/REAUDITORIA_F1_CORRECOES_POS_AUDITORIA.md` | Relatório de reauditoria | Evidência histórica: F1 `APROVADO_COM_P3` em 2026-10-11. Não alterar |

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

Referências das mensagens do usuário na sessão `8f60e6c4-621a-44be-a17d-8b16d858086c`. M1 a M6 são de 2026-10-11, M7 e M8 de 2026-10-13:

- **M1:** primeira mensagem do dia, com o texto “Aprovo as seguintes decisões, conforme descritas em `docs/arquitetura/analise_projeto_minhavida.md`, seção 9: DEC-MV-01. DEC-MV-02. DEC-MV-03. DEC-MV-04. DEC-MV-05.”
- **M2:** segunda mensagem do dia, com o texto “Aprovo expressamente a DEC-MV-25.”
- **M3:** mensagem que pediu a auditoria independente da F1 (“Prompt Master — Opus 5.5 — Auditoria independente da F1 e preparação condicionada da F2”). Ela declara, no seu §1.2, aprovações dadas antes ao Sonnet, em sessão que não está disponível aqui.
- **M4:** mensagem com o texto “Aprovo a DEC-MV-26, opção B”.
- **M5:** mensagem que pediu a resposta à Etapa A das correções. O Opus preparou a emenda `env_file=None`, e o usuário a encaminhou ao Sonnet como instrução própria (atestado em M6, §1.3).
- **M6:** mensagem que pediu a reauditoria das correções (“Prompt Master — Opus 5.5 — Reauditoria independente das correções da F1”).
- **M7:** mensagem com o texto “Aprovo a P-DOC-06 e a P-DOC-07, exatamente nos escopos da seção 9.1 de docs/auditorias/REAUDITORIA_F1_CORRECOES_POS_AUDITORIA.md.”
- **M8:** mensagem com o texto “Autorizo atualizar a nota desatualizada do indice.md §5 e registrar no §4 as aprovações de P-DOC-06 e P-DOC-07 que já concedi.”

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
| 2026-10-11 | Implementação da F1 | “Pode implementar” dado ao Sonnet após a Etapa A, com revalidação prévia do baseline | Declarado em M3 (§1.2). A mensagem original ao Sonnet não está disponível nesta sessão | Opus (registro em 2026-10-11, na reauditoria) |
| 2026-10-11 | Imports relativos em `tests/` | Autorizados expressamente, preservando a estrutura e sem mudar Ruff, Pyright, `sys.path`, `PYTHONPATH` ou dependências | Declarado em M3 (§1.2) | Opus (registro na reauditoria) |
| 2026-10-11 | **DEC-MV-26, opção B** | `exclude = ["*.md"]` em `[tool.ruff.format]` do `pyproject.toml`, com os comentários do anexo B de `docs/auditorias/AUDITORIA_F1_FUNDACAO_API.md`. Não muda comandos nem a cobertura de `.py`. Não inclui `alembic/` nos gates (ACH-MV-F1-005 segue pendente). Alternativas A e C não escolhidas | M4 | Opus (registro na reauditoria; adiado para não alterar os hashes travados pelo prompt de correções) |
| 2026-10-11 | Correções pós-auditoria da F1 | Implementação de `PROMPTS/PROMPT_MASTER_SONNET_5_F1_CORRECOES_POS_AUDITORIA.md` (ACH-MV-F1-001 a 003), inclusive o log de `DBAPIError` 500 (§7.2) e a fixture (§7.3), autorizada ao Sonnet após a Etapa A | Declarado em M6 (§1.2) | Opus |
| 2026-10-11 | Emenda `env_file=None` | `SettingsTeste` com `model_config = SettingsConfigDict(env_file=None)` e asserção estrutural no REG-F1-02. É instrução do usuário ao Sonnet, com precedência sobre o prompt de correções §7.3 e §7.5. Não é desvio do implementador | M5 e M6 (§1.3) | Opus |
| 2026-10-11 | Atualizações documentais P-DOC-01 a 05 | Prompt F1 §8.5 e §11.1; arquitetura §3.4; plano de validação, catálogo da F1 (CT-F1-21 e 22); este índice §4 e §5; `analise` §9. Não alcançam `CLAUDE.md`, ADRs, código ou configuração | M6 (§0, item 5, e §9) | Opus |
| 2026-10-11 | **Fora destas aprovações** | DEC-MV-06 a 24; a liberação da F2; a decisão sobre `alembic/` nos gates (ACH-MV-F1-005); o commit da F1, que cabe ao usuário | M3, M4 e M6 | Opus |
| 2026-10-13 | **P-DOC-06** | Conforme a reauditoria §9.1: Prompt F1 §14, passo 10, passa a usar `POSTGRES_USER=verificacao POSTGRES_PASSWORD=verificacao POSTGRES_DB=verificacao docker compose --env-file /dev/null config --quiet`, que também serve de modelo para os próximos prompts. Corrige no Prompt F1 o comando do ACH-MV-F1-007 | M7 | Opus |
| 2026-10-13 | **P-DOC-07** | Conforme a reauditoria §9.1: estados descritivos em `indice.md` §1, §2, §6 e §7, no cabeçalho do Prompt F1 e em `plano_fases_api.md` (cabeçalho e §3, linha da F1). Prompt F1 executado; F1 `APROVADO_COM_P3`, aguardando integração; contagem de CTs (173 + 2) e próxima ação | M7 | Opus |
| 2026-10-13 | Fechamento documental da F1 | Atualização da nota do §5 e este registro no §4. Não alcança código, testes, configuração, dependências, relatórios de auditoria, `CLAUDE.md` nem ADRs | M8 | Opus |
| 2026-10-13 | **Fora destas aprovações** | DEC-MV-06, o restante da DEC-MV-07, DEC-MV-08 e a opção do ACH-MV-F1-005, a tratar separadamente; DEC-MV-09 a 24; qualquer mudança da F2; o commit da F1, que cabe ao usuário | M7 e M8 | Opus |

## 5. Estado dos gates

| Gate | Estado | Observação |
| --- | --- | --- |
| G0 — Baseline e fontes | **Cumprido** | Fontes lidas e lacunas registradas (`analise` §2). Hashes conferidos novamente em 2026-10-11 |
| G1 — Arquitetura da F1 | **Cumprido** (2026-10-11) | DEC-MV-01 a 05 e DEC-MV-25 aceitas. DEC-MV-26 aprovada depois, na auditoria (M4) |
| G1 — demais fases | AGUARDANDO_DECISAO | DEC-MV-06 a 24, conforme `analise` §9 |
| G2 — Prompt Master F1 | **Cumprido**: `PRONTO_PARA_ETAPA_A` (2026-10-11) | §8.5 e §11.1 atualizados depois da reauditoria (P-DOC-01 e 02) |
| G3 — Etapa A da F1 | **Cumprido** (declarado pelo usuário em M3) | O relatório da Etapa A não está arquivado no repositório nem disponível nesta sessão |
| Pré-condição da Etapa B da F1 (ACH-MV-ARQ-019) | **Critério substantivo atendido; encerramento formal pendente** | Commit `bd2b2e0` com exatamente os 22 arquivos de `analise` §3.5, verificado pelo Opus na auditoria e na reauditoria. Os arquivos da F1 têm `mtime` posterior ao commit (19:13:38). Falta anexar o bloco de revalidação do Sonnet (Prompt F1 §1.2, a–e), declarada pelo usuário em M3 |
| Autorização da Etapa B | **Concedida** | F1 e correções (M3 e M6) |
| G4 — Entrega da F1 | **Cumprido** | `ENTREGUE_PARA_AUDITORIA`, duas vezes: a F1 e depois as correções |
| G5 — Auditoria independente da F1 | Histórico: **`BLOQUEADO`** (auditoria de 2026-10-11, ACH-MV-F1-001 a 003, P2). Atual: **`APROVADO_COM_P3`** (reauditoria de 2026-10-11) | `docs/auditorias/AUDITORIA_F1_FUNDACAO_API.md` e `docs/auditorias/REAUDITORIA_F1_CORRECOES_POS_AUDITORIA.md`. P3 em acompanhamento: ACH-MV-F1-005, 006 e 007. O veredito vale só para o objeto do manifesto da reauditoria |
| G6 — Integração da F1 | **Pendente (usuário)** | Commit local do objeto reauditado, com lista explícita de arquivos e sem `.env`. Uma mudança posterior invalida a aplicação automática do veredito |

Pendências:

| Pendência | Fonte | Impacto | Resolução |
| --- | --- | --- | --- |
| Integração da F1 (G6) | Reauditoria §10 | A F2 depende da F1 integrada | Commit do usuário |
| ACH-MV-ARQ-019: encerramento formal | `analise` §3.1 e §3.5; reauditoria §4 | Lacuna documental; não afeta o veredito técnico da F1 | Anexar o bloco de revalidação do relatório da F1, ou decisão expressa do usuário |
| ACH-MV-F1-005 (P3): `alembic/` fora do Ruff e do Pyright | Auditoria F1 §8 | Revisões da F2 ficariam fora dos gates | Decisão do usuário antes do Prompt F2 |
| ACH-MV-F1-007 (P3): `docker compose config` sem `--env-file /dev/null` lê o `.env` real | Reauditoria §4 | Leitura indireta do `.env` por ferramenta, sem exposição | Aprovar a correção dos comandos normativos (P-DOC-06, reauditoria §9) |
| Gates da F2 | `plano_fases_api.md` (F2) | Prompt F2 não liberado | F1 integrada; DEC-MV-06, DEC-MV-07 (restante), DEC-MV-08; `CLAUDE.md` e modelo físico reconciliados; decisão do ACH-MV-F1-005 |
| DEC-MV-24 pendente | REC-MV-029, ACH-MV-ARQ-021 | Não afeta F1 a F4. Bloqueia a F5 | Decidir antes do Prompt Master da F5 |

> **Atualização de 2026-10-13 (M7 e M8).** A P-DOC-07 atualizou §1, §2, §6 e §7 deste índice, o cabeçalho do Prompt F1 e o `plano_fases_api.md`, que agora estão coerentes com esta §5. A P-DOC-06 corrigiu o comando do Compose no Prompt F1 §14, passo 10. Assim, a resolução do ACH-MV-F1-007 indicada na tabela de pendências já foi aplicada ao Prompt F1. O achado segue P3 em acompanhamento até os próximos prompts adotarem o mesmo comando. Histórico: em 2026-10-11, após a reauditoria, §1, §2, §6 e §7 ficaram desatualizadas por estarem fora do escopo de M6, e esta §5 era a fonte dos estados vigentes.

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
- **Contagem atualizada em 2026-10-13 (P-DOC-07):** 175 CTs (CT-F1-21 e 22 acrescentados pela P-DOC-04) e 26 DECs (DEC-MV-26). RECs (32), ACH-MV-ARQ (25) e ESC-FIN (5) não mudaram. Os 263 IDs desses tipos citados em `docs/` e nos dois Prompts da F1 existem na origem. Os achados ACH-MV-F1-001 a 007 estão nos relatórios de `docs/auditorias/`.
- Todas as referências `§` da arquitetura existem. As referências `§` entre documentos (análise, índice, planos, ADRs e Prompt F1) foram conferidas contra os títulos de seção.
- Cercas de código balanceadas em todos os documentos.
- Nenhuma credencial do `compose.yaml` reproduzida nos documentos.
- A convenção de nomes tem os mesmos cinco padrões na arquitetura §10.1, no ADR-0001 D-09 e no Prompt F1 §6.
- A lista de 22 arquivos de `analise` §3.5 corresponde aos arquivos não ignorados do repositório, menos `compose.yaml` e `__pycache__/`.
- O nome antigo da F8 só aparece como registro histórico: `plano_fases_api.md` §1 e REC-MV-028.
- Arquivos protegidos (`CLAUDE.md`, prompt anterior, código e configuração) com os hashes do baseline.

## 7. Próxima ação do usuário

Atualizado em 2026-10-13 (P-DOC-07). Os passos da F0 (commit de baseline, Etapa A, “pode implementar”) foram cumpridos.

1. **Integrar a F1 (G6):** commit local do objeto reauditado, com **lista explícita** de arquivos, sem `.env`, `.venv/` ou caches. Não usar `git add -A` nem `git add .`. Qualquer mudança nos arquivos aprovados antes do commit invalida a aplicação automática do veredito.
2. Preencher o `.env` conforme o Prompt F1 §9.3 (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` e um `DATABASE_URL` válido), se ainda não o fez.
3. Antes do Prompt F2, decidir:
   - DEC-MV-06 (ADR-0002);
   - o restante da DEC-MV-07;
   - DEC-MV-08;
   - a inclusão ou não de `alembic/` nos gates (ACH-MV-F1-005);
   - a atualização do `CLAUDE.md` (`analise` §10).
4. Opcional: encerrar formalmente o ACH-MV-ARQ-019, anexando o bloco de revalidação do relatório da F1 ou decidindo expressamente.
5. Antes da F5: decidir DEC-MV-24.
6. Opcional: restaurar as linhas truncadas do `CLAUDE.md` (ACH-MV-ARQ-012).
