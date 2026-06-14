# Cyber Security Study Harness

Harness leve para acompanhar o roadmap de Cyber Security por projetos.

Ele foi feito para consumir pouco armazenamento:

- Sem banco de dados.
- Sem dependencias externas.
- Sem Docker.
- Sem arquivos grandes.
- Apenas JSON, Markdown e um script Python.

## Comandos

Execute a partir da raiz deste diretorio:

```bash
python3 study-harness/study.py status
python3 study-harness/study.py next
python3 study-harness/study.py week 1
python3 study-harness/study.py done 1 1
python3 study-harness/study.py log "Montei o ambiente inicial e instalei ferramentas"
```

## Fluxo Recomendado

1. Veja o proximo passo:

```bash
python3 study-harness/study.py next
```

2. Trabalhe no projeto.

3. Marque uma tarefa como concluida:

```bash
python3 study-harness/study.py done <semana> <numero-da-tarefa>
```

4. Registre o que aprendeu:

```bash
python3 study-harness/study.py log "Descricao curta da sessao"
```

## Arquivos

- `study.py`: CLI do harness.
- `tasks.json`: tarefas do roadmap.
- `progress.json`: progresso local.
- `journal.md`: diario de estudo.

