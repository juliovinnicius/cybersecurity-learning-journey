# Lab Setup

## Objetivo

Definir um ambiente leve para praticar Cyber Security sem consumir muito armazenamento local.

## Ambiente Atual

| Item | Valor |
| --- | --- |
| Sistema | macOS |
| Arquitetura | ARM64 |
| Python | Disponivel em `/usr/bin/python3` |
| Git | Disponivel em `/usr/bin/git` |
| Docker | Disponivel em `/usr/local/bin/docker` |
| Espaco livre medido | Aproximadamente 103 GiB |

## Decisao de Ambiente

Para a primeira fase do roadmap, nao sera usada VM local.

A estrategia escolhida e:

- macOS como workstation principal.
- Python local para scripts e automacoes.
- Git para versionamento.
- Docker apenas quando uma aplicacao vulneravel local for realmente necessaria.
- Labs online para cenarios mais pesados.
- Sem Kali local por enquanto.
- Sem Wazuh local por enquanto.
- Sem Elastic Stack ou Splunk local por enquanto.

## Justificativa

O Mac tem 256 GB de armazenamento total. Embora exista espaco livre suficiente no momento, manter VMs, ISOs e stacks de seguranca completas pode consumir armazenamento rapidamente e gerar custo de manutencao desnecessario.

Como o foco inicial e AppSec, automacao, analise de logs e fundamentos de SOC, a maior parte do aprendizado pode ser feita com:

- Scripts pequenos.
- Relatorios em Markdown.
- Logs de exemplo.
- Labs online.
- Containers pontuais.

## Papel do Linux no Roadmap

Linux continuara sendo estudado, mas de forma leve:

- Comandos e conceitos serao praticados quando necessarios aos projetos.
- Logs Linux serao usados no projeto `ssh-log-analyzer`.
- Containers Linux podem ser usados pontualmente.
- VM Linux so sera criada se uma tarefa exigir isolamento real ou comportamento de sistema que nao possa ser reproduzido de forma mais leve.

## Ferramentas Locais Necessarias

Ja disponiveis:

- [x] Python 3.
- [x] Git.
- [x] Docker CLI.

A validar ou instalar nas proximas tarefas:

- [ ] Nmap.
- [ ] Wireshark.
- [ ] Burp Suite Community.
- [ ] Editor de codigo.

## Comandos de Validacao

Sistema:

```bash
uname -a
```

Espaco livre:

```bash
df -h .
```

Python:

```bash
python3 --version
```

Git:

```bash
git --version
```

Docker:

```bash
docker --version
docker system df
```

## Criterio para Usar VM

Uma VM local so deve ser criada se:

1. O lab exigir kernel, init system ou logs reais de Linux.
2. Container nao for suficiente.
3. A alternativa online nao atender ao objetivo.
4. Houver espaco suficiente.
5. Existir plano de remocao depois do uso.

## Criterio para Usar Docker

Docker pode ser usado quando:

- O container for temporario.
- A imagem for pequena ou moderada.
- A tarefa depender de uma aplicacao local.
- Houver comando claro de limpeza depois.

Antes de usar Docker em labs:

```bash
docker system df
```

Depois de finalizar labs temporarios:

```bash
docker system prune
```

## Decisao Atual

Ambiente configurado como:

```text
macOS nativo + Python + Git + Docker pontual + labs online
```

Essa configuracao e suficiente para avancar no roadmap sem comprometer armazenamento.

