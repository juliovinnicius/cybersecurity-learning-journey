# Regras Eticas e Escopo de Testes

## Objetivo

Definir limites claros para estudos, labs e ferramentas de Cyber Security neste roadmap.

## Principios

- Testar apenas sistemas proprios, ambientes de laboratorio ou alvos com autorizacao explicita.
- Respeitar termos de uso de plataformas online, CTFs e labs.
- Evitar coleta, exposicao ou publicacao de dados sensiveis.
- Documentar objetivo, alvo, ferramenta e limite de cada teste.
- Parar qualquer atividade que gere impacto inesperado, instabilidade ou acesso indevido.
- Usar evidencias somente para aprendizado, relatorios tecnicos e portfolio responsavel.

## Escopo Permitido

Atividades permitidas neste projeto:

- Labs locais criados para estudo.
- Aplicacoes vulneraveis intencionalmente, como Juice Shop, quando executadas localmente ou em instancia autorizada.
- Plataformas de treinamento que permitam explicitamente testes de seguranca.
- Scripts proprios contra `localhost`, maquinas proprias, containers proprios ou arquivos de exemplo.
- Analise de logs pequenos, anonimizados ou gerados para estudo.
- Captura de trafego local de labs proprios com Wireshark.
- Verificacao de headers e configuracoes apenas em dominios proprios, labs ou ambientes autorizados.

## Fora de Escopo

Atividades proibidas neste projeto:

- Scanning, brute force, fuzzing ou exploracao contra sistemas de terceiros sem autorizacao.
- Testes contra redes publicas, corporativas, universitarias ou domesticas de outras pessoas.
- Captura de trafego de terceiros ou redes compartilhadas sem consentimento.
- Tentativas de bypass de autenticacao em sistemas reais.
- Uso de credenciais vazadas, tokens, chaves privadas ou dados pessoais reais.
- Publicacao de payloads, evidencias ou logs que exponham dados sensiveis.
- Persistencia, malware, phishing real ou qualquer atividade com impacto operacional.

## Uso das Ferramentas

Nmap:

- Permitido contra `localhost`, containers proprios, VMs proprias e labs autorizados.
- Nao usar contra IPs publicos ou redes de terceiros sem autorizacao formal.

Wireshark:

- Permitido para trafego local de labs e interfaces controladas.
- Nao capturar trafego de outras pessoas, redes abertas ou ambientes corporativos sem permissao.

Burp Suite Community:

- Permitido com aplicacoes vulneraveis intencionais, apps proprios e labs autorizados.
- Nao interceptar sessoes, cookies ou credenciais de terceiros.

Python:

- Permitido para automacao defensiva, parsers, validadores e ferramentas controladas.
- Scripts de enumeracao devem ter alvo, taxa e objetivo documentados.

## Modelo de Registro de Teste

Antes de executar um teste pratico, registrar:

```text
Data:
Objetivo:
Alvo autorizado:
Ferramentas:
Limites:
Resultado esperado:
Evidencias geradas:
```

## Regra de Parada

Se um teste sair do escopo, causar erro inesperado, afetar disponibilidade ou revelar dado sensivel, a atividade deve ser interrompida e registrada no diario com o que aconteceu e qual ajuste sera feito antes de continuar.
