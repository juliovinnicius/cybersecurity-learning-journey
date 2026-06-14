# Roadmap de Cyber Security por Projetos

Este roadmap foi pensado para quem ja tem experiencia como desenvolvedor de software e aprende melhor construindo projetos do que estudando teoria isolada. O foco principal e usar sua base de engenharia para entrar em Cyber Security, com enfase em AppSec, Blue Team, automacao de seguranca e SOC Analyst Junior.

## Perfil Considerado

Este plano assume que voce ja e desenvolvedor de software ha mais de 7 anos. Por isso, ele nao trata programacao, Git, terminal e organizacao de projetos como assuntos iniciantes. A ideia e reaproveitar sua experiencia em desenvolvimento para acelerar nos temas que normalmente diferenciam um profissional de seguranca:

- Pensamento adversarial.
- Analise de risco.
- Modelagem de ameacas.
- Seguranca de aplicacoes.
- Investigacao de logs.
- Automacao de deteccao.
- Escrita de relatorios tecnicos de seguranca.
- Comunicacao de impacto tecnico e de negocio.

## Objetivo

Em 12 semanas, voce deve ter:

- Um laboratorio local de seguranca.
- Projetos praticos publicados no GitHub.
- Relatorios tecnicos em Markdown.
- Scripts e ferramentas aplicadas a seguranca.
- Base para se candidatar a vagas de AppSec Junior, Security Engineer Junior, SOC Analyst, Analista de Seguranca ou funcoes hibridas entre desenvolvimento e seguranca.

## Como Usar Este Roadmap

Para cada projeto:

1. Tente construir primeiro.
2. Quando travar, estude apenas a teoria necessaria para destravar.
3. Aplique imediatamente.
4. Documente o que fez.
5. Transforme o resultado em portfolio.

O ciclo principal e:

```text
Projeto -> problema -> teoria minima -> pratica -> relatorio -> GitHub
```

## Harness de Estudo

Este diretorio tambem contem um harness leve em `study-harness/` para acompanhar o progresso do roadmap sem consumir muito armazenamento. Ele usa apenas Python, JSON e Markdown.

Comandos principais:

```bash
python3 study-harness/study.py status
python3 study-harness/study.py next
python3 study-harness/study.py week 1
python3 study-harness/study.py done 1 1
python3 study-harness/study.py log "Descricao curta da sessao"
```

## Rotina Semanal Recomendada

Se voce tiver entre 8 e 12 horas por semana:

- 2 dias para construir o projeto.
- 2 dias para laboratorio e testes.
- 1 dia para documentacao.
- 1 dia para revisao ou melhoria.
- 1 dia livre.

Exemplo:

```text
Segunda: construir
Terca: laboratorio
Quarta: construir
Quinta: testes
Sexta: corrigir e melhorar
Sabado: README, relatorio e GitHub
Domingo: descanso ou revisao leve
```

## Semana 1: Laboratorio de Seguranca

### Objetivo

Montar um ambiente seguro para praticar sem depender de sistemas reais de terceiros.

### Entregas

Criar um repositorio:

```text
cybersecurity-learning-journey/
├── README.md
├── lab-setup.md
└── notes/
```

### O Que Construir

- Uma VM Linux ou ambiente WSL.
- Uma aplicacao vulneravel local, como OWASP Juice Shop ou DVWA.
- Ferramentas basicas:
  - Wireshark
  - Burp Suite Community
  - Nmap
  - Python
  - VS Code
  - Git

### Teoria Minima

- Como isolar ambientes vulneraveis.
- Como definir escopo de testes.
- Como documentar risco e evidencia.
- Cuidados eticos em cyber security.

### Checklist

- [ ] Criar conta no GitHub.
- [ ] Criar repositorio `cybersecurity-learning-journey`.
- [ ] Instalar ou configurar ambiente Linux.
- [ ] Instalar ferramentas principais.
- [ ] Documentar o ambiente em `lab-setup.md`.

## Semana 2: Scanner Basico de Portas em Python

### Objetivo

Entender redes pela perspectiva de enumeracao e reconhecimento, criando uma ferramenta simples e controlada.

### Entregas

Criar um repositorio:

```text
port-scanner-python/
├── scanner.py
├── README.md
└── examples/
```

### O Que Construir

Um script que:

- Recebe um IP ou host.
- Recebe uma lista de portas.
- Testa quais portas estao abertas.
- Mostra o resultado no terminal.
- Exporta o resultado para `.txt` ou `.json`.

### Teoria Minima

- TCP.
- Portas.
- Socket.
- Timeout.
- Diferenca entre porta aberta, fechada e filtrada.
- Implicacoes eticas e legais de scanning.

### Regras de Uso

Use apenas em:

- `localhost`.
- Sua propria maquina.
- VMs do seu laboratorio.
- Ambientes autorizados.

### Checklist

- [ ] Criar conexao TCP com Python.
- [ ] Ler IP e portas por argumento ou input.
- [ ] Implementar timeout.
- [ ] Exibir portas abertas.
- [ ] Salvar resultado.
- [ ] Escrever README com exemplos de uso.

## Semanas 3 e 4: Relatorio de Vulnerabilidades no OWASP Juice Shop

### Objetivo

Aprender seguranca web explorando uma aplicacao feita para treinamento.

### Entregas

Criar um repositorio:

```text
juice-shop-security-report/
├── README.md
├── report.md
└── evidence/
```

### O Que Fazer

Analisar:

- Login.
- Cookies.
- Requisicoes HTTP.
- Inputs.
- Erros.
- Controle de acesso.
- XSS basico.
- SQL Injection basico, apenas dentro do laboratorio.

### Ferramentas

- OWASP Juice Shop.
- Burp Suite Community.
- Browser DevTools.
- `curl`.

### Teoria Minima

- HTTP.
- Metodos GET, POST, PUT e DELETE.
- Cookies e sessoes.
- OWASP Top 10.
- XSS.
- SQL Injection.
- Broken Access Control.

### Modelo de Relatorio

Para cada vulnerabilidade:

```text
Titulo:
Severidade:
Categoria OWASP:
Descricao:
Impacto:
Como foi identificada:
Evidencia:
Recomendacao:
Referencias:
```

### Checklist

- [ ] Subir o Juice Shop localmente.
- [ ] Configurar Burp Suite.
- [ ] Interceptar uma requisicao.
- [ ] Identificar pelo menos 3 vulnerabilidades do lab.
- [ ] Escrever relatorio tecnico.
- [ ] Publicar sem expor dados sensiveis, tokens ou respostas proibidas.

## Semanas 5 e 6: Analisador de Logs SSH

### Objetivo

Pensar como Blue Team, analisando logs e detectando tentativa de brute force.

### Entregas

Criar um repositorio:

```text
ssh-log-analyzer/
├── analyzer.py
├── README.md
├── sample_logs/
└── report.md
```

### O Que Construir

Um script em Python que:

- Le um arquivo de log.
- Identifica tentativas falhas de login.
- Conta falhas por IP.
- Detecta possivel brute force.
- Gera um resumo.
- Exporta resultado em `.csv` ou `.json`.

### Teoria Minima

- Logs Linux.
- SSH.
- Regex.
- Brute force.
- Indicadores de comprometimento.
- Falso positivo vs incidente real.

### Exemplo de Saida

```text
IP: 192.168.56.10
Falhas: 42
Periodo: 10:20 - 10:25
Classificacao: suspeito
Acao recomendada: bloquear IP e revisar autenticacoes bem-sucedidas
```

### Checklist

- [ ] Coletar ou criar logs de exemplo.
- [ ] Ler arquivo com Python.
- [ ] Extrair IPs com regex.
- [ ] Contar falhas por IP.
- [ ] Criar criterio de suspeita.
- [ ] Exportar resultado.
- [ ] Escrever `report.md` com conclusao.

## Semanas 7, 8 e 9: Mini SOC com Wazuh

### Objetivo

Montar um ambiente defensivo parecido com o usado em operacoes de seguranca.

### Entregas

Criar um repositorio:

```text
mini-soc-wazuh-lab/
├── README.md
├── setup.md
├── incident-report.md
└── screenshots/
```

### O Que Fazer

- Instalar Wazuh.
- Monitorar uma maquina Linux.
- Gerar eventos de login.
- Visualizar alertas no dashboard.
- Investigar um alerta.
- Criar um relatorio de incidente.

### Teoria Minima

- SIEM.
- Agente.
- Evento.
- Alerta.
- Incidente.
- IOC.
- MITRE ATT&CK.
- Resposta a incidente.

### Modelo de Relatorio de Incidente

```text
Titulo:
Data:
Resumo:
Alerta inicial:
Evidencias:
Linha do tempo:
Impacto:
Contencao:
Erradicacao:
Recuperacao:
Licoes aprendidas:
```

### Checklist

- [ ] Instalar Wazuh.
- [ ] Adicionar agente.
- [ ] Gerar eventos de autenticacao.
- [ ] Encontrar alertas no dashboard.
- [ ] Investigar um evento suspeito.
- [ ] Mapear o evento ao MITRE ATT&CK, se aplicavel.
- [ ] Escrever relatorio de incidente.

## Semanas 10 e 11: Web Security Header Checker

### Objetivo

Criar uma ferramenta util para avaliar configuracoes basicas de seguranca web.

### Entregas

Criar um repositorio:

```text
web-security-header-checker/
├── checker.py
├── README.md
└── examples/
```

### O Que Construir

Um script que recebe uma URL e verifica:

- Uso de HTTPS.
- `Strict-Transport-Security`.
- `Content-Security-Policy`.
- `X-Frame-Options`.
- `X-Content-Type-Options`.
- Cookies com `Secure`.
- Cookies com `HttpOnly`.
- Cookies com `SameSite`.

### Teoria Minima

- HTTP headers.
- HTTPS.
- Cookies.
- Clickjacking.
- Content Security Policy.
- Boas praticas de configuracao web.

### Checklist

- [ ] Fazer requisicao HTTP com Python.
- [ ] Ler headers da resposta.
- [ ] Validar headers esperados.
- [ ] Classificar resultado como OK, alerta ou ausente.
- [ ] Gerar relatorio no terminal.
- [ ] Adicionar exemplos ao README.

## Semana 12: Playbooks e Portfolio

### Objetivo

Organizar o portfolio e criar materiais que mostram maturidade profissional.

### Entregas

Criar um repositorio:

```text
incident-response-playbooks/
├── README.md
├── phishing.md
├── brute-force.md
├── malware-suspected.md
└── credential-leak.md
```

### Playbooks

Criar playbooks para:

- Phishing.
- Brute force.
- Malware suspeito.
- Vazamento de credenciais.
- Login anomalo.

### Modelo de Playbook

```text
Objetivo:
Sinais de alerta:
Triagem inicial:
Evidencias necessarias:
Ferramentas:
Acoes de contencao:
Erradicacao:
Recuperacao:
Comunicacao:
Licoes aprendidas:
```

### Checklist

- [ ] Revisar todos os READMEs.
- [ ] Padronizar nomes dos repositorios.
- [ ] Melhorar explicacoes dos projetos.
- [ ] Remover qualquer dado sensivel.
- [ ] Criar README no perfil do GitHub.
- [ ] Atualizar LinkedIn.
- [ ] Criar curriculo focado em seguranca.

## Portfolio Final Esperado

Ao final do roadmap, seu GitHub pode ter:

```text
cybersecurity-learning-journey
port-scanner-python
juice-shop-security-report
ssh-log-analyzer
mini-soc-wazuh-lab
web-security-header-checker
incident-response-playbooks
```

## Habilidades Que Voce Vai Demonstrar

- Fundamentos de redes.
- Uso de Linux.
- Python aplicado a seguranca.
- Analise de logs.
- Deteccao de brute force.
- Conceitos de SOC.
- Uso basico de SIEM.
- Seguranca web.
- OWASP Top 10.
- Escrita de relatorios tecnicos.
- Resposta a incidentes.

## Vagas Para Buscar

Procure por cargos como:

- SOC Analyst Junior.
- Analista de Seguranca Junior.
- Estagio em Seguranca da Informacao.
- Analista de Monitoramento de Seguranca.
- Blue Team Junior.
- Cybersecurity Intern.
- Analista de SIEM Junior.

## Palavras-Chave Para Curriculo

Inclua somente o que voce praticou:

- Linux
- Redes
- TCP/IP
- HTTP
- Python
- Logs
- SSH
- SIEM
- Wazuh
- Wireshark
- Burp Suite
- OWASP Top 10
- Incident Response
- Brute Force Detection
- Security Monitoring
- Vulnerability Report

## Certificacoes Opcionais

Certificacao nao substitui projeto, mas pode ajudar:

- ISC2 Certified in Cybersecurity.
- CompTIA Security+.
- BTL1.
- Cisco CyberOps Associate.
- eJPT, caso queira migrar para pentest depois.

## Regras Eticas

- Nunca teste sistemas sem autorizacao.
- Nunca publique credenciais, tokens, chaves ou dados reais.
- Use apenas laboratorios, maquinas proprias e ambientes permitidos.
- Em relatorios publicos, remova informacoes sensiveis.
- Documente sempre o escopo do teste.

## Indicador de Prontidao Para Aplicar

Voce esta pronto para comecar a aplicar para vagas quando tiver:

- [ ] Pelo menos 3 projetos publicados.
- [ ] Pelo menos 1 relatorio tecnico bem escrito.
- [ ] Um script Python funcional.
- [ ] Um projeto relacionado a logs ou SOC.
- [ ] README claro em cada repositorio.
- [ ] Curriculo destacando projetos.
- [ ] LinkedIn atualizado.

## Proximo Passo Imediato

Comece pela Semana 1:

1. Crie seu GitHub, se ainda nao tiver.
2. Crie o repositorio `cybersecurity-learning-journey`.
3. Configure seu ambiente Linux.
4. Instale as ferramentas principais.
5. Escreva o primeiro `lab-setup.md`.
