# Estrategia de Laboratorio Leve para Mac com 256 GB

## Contexto

O ambiente principal de estudo e um Mac com 256 GB de armazenamento. A estrategia do laboratorio precisa permitir pratica real em Cyber Security sem transformar o estudo em manutencao de infraestrutura pesada.

Como ja existe experiencia previa em desenvolvimento de software, o foco sera usar o Mac como uma workstation leve para:

- AppSec.
- Automacao de seguranca.
- Analise de logs.
- Relatorios tecnicos.
- Labs web pontuais.
- Investigacoes defensivas com datasets pequenos.

## Principios

- Priorizar labs online quando o ambiente local for pesado.
- Usar Docker apenas de forma pontual.
- Evitar manter multiplas VMs.
- Evitar imagens, ISOs, dumps e wordlists grandes.
- Versionar apenas arquivos pequenos, scripts e documentacao.
- Apagar artefatos temporarios ao final de cada projeto.
- Medir uso de disco antes de instalar stacks pesadas.

## Limites Praticos

| Item | Limite recomendado |
| --- | --- |
| Laboratorio local total | 10 GB a 20 GB |
| Projeto individual | Ate 1 GB |
| Logs versionados | Pequenos arquivos de exemplo |
| Containers ativos | 1 ou 2 por vez |
| VMs locais | Evitar; usar apenas se indispensavel |
| Screenshots | Apenas evidencias relevantes |
| Videos | Evitar |

## Ferramentas Preferidas

### Locais e leves

- Python.
- Git.
- Nmap.
- Wireshark.
- Burp Suite Community.
- Docker, apenas quando necessario.
- VS Code ou editor equivalente.

### Online ou remotas

- PortSwigger Web Security Academy.
- TryHackMe.
- Hack The Box Academy.
- LetsDefend.
- Blue Team Labs Online.

## O Que Evitar

- Manter Kali, Ubuntu, Windows e outras VMs ao mesmo tempo.
- Instalar Elastic Stack completo localmente sem necessidade.
- Instalar Splunk Enterprise local para tarefas simples.
- Manter Wazuh local se o espaco estiver apertado.
- Baixar SecLists completo sem necessidade especifica.
- Manter RockYou duplicado ou wordlists gigantes.
- Guardar ISOs depois de terminar instalacao.
- Versionar dumps, bancos, capturas grandes ou logs extensos.

## Estrategia por Projeto

### Semana 1: Laboratorio

Usar apenas ferramentas essenciais. Documentar ambiente e escopo.

### Semana 2: Port Scanner

Projeto 100% local e leve. Nao precisa de Docker nem VM.

### Semanas 3 e 4: Juice Shop

Preferencia:

1. PortSwigger Web Security Academy para parte web online.
2. Juice Shop via Docker apenas quando for necessario praticar localmente.

Se usar Docker, remover container e imagem quando terminar.

### Semanas 5 e 6: SSH Log Analyzer

Usar arquivos pequenos de log em `sample_logs/`. Evitar datasets grandes.

### Semanas 7 a 9: Mini SOC

Preferencia:

1. LetsDefend ou Blue Team Labs Online.
2. Wazuh local apenas se houver espaco e necessidade clara.

Antes de instalar Wazuh, medir o espaco livre e definir criterio de remocao.

### Semanas 10 e 11: Web Security Header Checker

Projeto 100% local e leve. Usar Python e requisicoes HTTP.

### Semana 12: Playbooks

Projeto apenas Markdown. Consumo de armazenamento irrelevante.

## Comandos de Monitoramento

Ver uso geral do disco:

```bash
df -h
```

Ver tamanho dos arquivos na pasta atual:

```bash
du -sh .
```

Ver uso do Docker:

```bash
docker system df
```

Listar imagens Docker:

```bash
docker image ls
```

Listar containers:

```bash
docker container ls -a
```

Listar volumes:

```bash
docker volume ls
```

## Limpeza do Docker

Limpeza moderada:

```bash
docker system prune
```

Limpeza mais agressiva, apenas quando tiver certeza de que nao precisa das imagens paradas:

```bash
docker system prune -a
```

Limpar volumes nao usados, apenas quando tiver certeza de que nao guardam dados importantes:

```bash
docker volume prune
```

## Regras de Versionamento

Versionar:

- Markdown.
- Scripts.
- Configuracoes pequenas.
- Logs pequenos de exemplo.
- Relatorios.
- Checklists.

Nao versionar:

- ISOs.
- Dumps.
- Bancos locais.
- Capturas grandes.
- Wordlists grandes.
- Arquivos com credenciais.
- Tokens.
- Chaves privadas.

## Criterio de Decisao

Antes de instalar uma ferramenta pesada, responder:

1. Essa ferramenta e essencial para a tarefa atual?
2. Existe alternativa online ou mais leve?
3. O aprendizado depende da instalacao local?
4. Quanto espaco ela vai consumir?
5. Como remover tudo depois?

Se a resposta nao justificar a instalacao local, usar alternativa online ou dataset pequeno.

## Decisao Atual

Para este roadmap, o laboratorio sera leve por padrao:

- Projetos de codigo e relatorio ficam locais.
- Labs pesados ficam online sempre que possivel.
- Docker sera usado apenas pontualmente.
- SIEM local sera opcional, nao requisito.
- O portfolio priorizara clareza tecnica, raciocinio de seguranca e qualidade dos relatorios.

