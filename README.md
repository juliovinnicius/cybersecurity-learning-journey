# Cybersecurity Learning Journey

Sou desenvolvedor de software ha mais de 7 anos, entao o foco aqui nao e aprender programacao do zero. A proposta e usar minha experiencia em engenharia de software para desenvolver habilidades praticas em seguranca, especialmente nas areas de AppSec, Blue Team, automacao de seguranca, analise de logs e resposta a incidentes.

## Objetivo

Construir um portfolio pratico que demonstre:

- Pensamento adversarial aplicado a software.
- Analise de riscos e vulnerabilidades.
- Seguranca de aplicacoes web.
- Automacao com scripts.
- Analise de logs e deteccao.
- Escrita de relatorios tecnicos.
- Fundamentos de SOC e resposta a incidentes.

## Abordagem

Este estudo segue um ciclo simples:

```text
Projeto -> problema -> teoria minima -> pratica -> relatorio -> GitHub
```

Em vez de estudar teoria de forma isolada, cada tema e explorado por meio de uma entrega pratica.

## Restricao de Ambiente

O ambiente principal e um Mac com 256 GB de armazenamento. Por isso, este roadmap prioriza:

- Labs online quando fizer sentido.
- Docker apenas de forma pontual.
- Poucas ferramentas locais.
- Arquivos pequenos de exemplo.
- Markdown, JSON e Python sem dependencias pesadas.
- Evitar VMs grandes, ISOs, dumps, wordlists gigantes e stacks locais completas.

A estrategia detalhada esta documentada em:

- [lab/storage-strategy.md](./lab/storage-strategy.md)

## Roadmap

O plano principal esta em:

- [cybersecurity-roadmap.md](./cybersecurity-roadmap.md)

Resumo das etapas:

| Semana | Projeto | Foco |
| --- | --- | --- |
| 1 | Laboratorio de seguranca leve | Ambiente, escopo e etica |
| 2 | Port scanner em Python | Redes e enumeracao controlada |
| 3-4 | Juice Shop Security Report | AppSec e OWASP Top 10 |
| 5-6 | SSH Log Analyzer | Blue Team e analise de logs |
| 7-9 | Mini SOC leve | Investigacao e resposta a incidentes |
| 10-11 | Web Security Header Checker | AppSec e automacao |
| 12 | Incident Response Playbooks | Processo e comunicacao |

## Study Harness

Este repositorio inclui um harness leve para acompanhar progresso:

- [study-harness/](./study-harness/)

Comandos principais:

```bash
python3 study-harness/study.py status
python3 study-harness/study.py next
python3 study-harness/study.py week 1
python3 study-harness/study.py done 1 1
python3 study-harness/study.py log "Descricao curta da sessao"
```

Fluxo recomendado:

```bash
python3 study-harness/study.py next
# executar a tarefa
python3 study-harness/study.py done <semana> <tarefa>
python3 study-harness/study.py log "O que foi feito e aprendido"
```

## Estrutura

```text
.
├── README.md
├── cybersecurity-roadmap.md
├── lab/
│   ├── lab-setup.md
│   └── storage-strategy.md
└── study-harness/
    ├── README.md
    ├── study.py
    ├── tasks.json
    ├── progress.json
    └── journal.md
```

## Projetos Planejados

Os projetos tecnicos principais podem virar repositorios separados:

- `port-scanner-python`
- `juice-shop-security-report`
- `ssh-log-analyzer`
- `mini-soc-wazuh-lab`
- `web-security-header-checker`
- `incident-response-playbooks`

Este repositorio central mantem o roadmap, o diario, o progresso e as decisoes de estudo.

## Regras Eticas

- Nao testar sistemas sem autorizacao.
- Nao publicar credenciais, tokens, chaves ou dados sensiveis.
- Usar apenas laboratorios, maquinas proprias e ambientes permitidos.
- Documentar escopo e limitacoes de cada teste.
- Tratar evidencias com cuidado.

## Status

Roadmap iniciado.
