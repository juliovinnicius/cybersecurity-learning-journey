#!/usr/bin/env python3
import argparse
import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TASKS_PATH = BASE_DIR / "tasks.json"
PROGRESS_PATH = BASE_DIR / "progress.json"
JOURNAL_PATH = BASE_DIR / "journal.md"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path, data):
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")


def load_state():
    return load_json(TASKS_PATH), load_json(PROGRESS_PATH)


def find_week(tasks, week_number):
    for week in tasks["weeks"]:
        if week["week"] == week_number:
            return week
    raise SystemExit(f"Semana {week_number} nao encontrada.")


def completed_for(progress, week_number):
    return set(progress.get("completed", {}).get(str(week_number), []))


def print_week(week, progress):
    done = completed_for(progress, week["week"])
    print(f"Semana {week['week']}: {week['title']}")
    print(f"Objetivo: {week['goal']}")
    print(f"Projeto: {week['project']}")
    print()
    for index, task in enumerate(week["tasks"], start=1):
        marker = "x" if index in done else " "
        print(f"[{marker}] {index}. {task}")


def cmd_status(_args):
    tasks, progress = load_state()
    total = 0
    completed = 0

    for week in tasks["weeks"]:
        total += len(week["tasks"])
        completed += len(completed_for(progress, week["week"]))

    current_week = progress.get("current_week", 1)
    percent = round((completed / total) * 100, 1) if total else 0

    print("Cyber Security Study Harness")
    print(f"Semana atual: {current_week}")
    print(f"Progresso: {completed}/{total} tarefas ({percent}%)")
    print(f"Sessoes registradas: {len(progress.get('sessions', []))}")
    print()
    print_week(find_week(tasks, current_week), progress)


def cmd_week(args):
    tasks, progress = load_state()
    progress["current_week"] = args.week
    save_json(PROGRESS_PATH, progress)
    print_week(find_week(tasks, args.week), progress)


def cmd_next(_args):
    tasks, progress = load_state()
    current_week = progress.get("current_week", 1)

    for week_number in range(current_week, len(tasks["weeks"]) + 1):
        week = find_week(tasks, week_number)
        done = completed_for(progress, week_number)
        for index, task in enumerate(week["tasks"], start=1):
            if index not in done:
                if progress.get("current_week") != week_number:
                    progress["current_week"] = week_number
                    save_json(PROGRESS_PATH, progress)
                print(f"Proximo passo: Semana {week_number}, tarefa {index}")
                print(f"Projeto: {week['project']}")
                print(f"Tarefa: {task}")
                return

    print("Todas as tarefas foram concluidas.")


def cmd_done(args):
    tasks, progress = load_state()
    week = find_week(tasks, args.week)

    if args.task < 1 or args.task > len(week["tasks"]):
        raise SystemExit(f"Tarefa {args.task} nao existe na semana {args.week}.")

    completed = progress.setdefault("completed", {})
    week_done = set(completed.get(str(args.week), []))
    week_done.add(args.task)
    completed[str(args.week)] = sorted(week_done)

    if args.week >= progress.get("current_week", 1):
        progress["current_week"] = args.week

    save_json(PROGRESS_PATH, progress)
    print(f"Concluido: Semana {args.week}, tarefa {args.task}")
    print(week["tasks"][args.task - 1])


def cmd_undo(args):
    tasks, progress = load_state()
    find_week(tasks, args.week)

    completed = progress.setdefault("completed", {})
    week_done = set(completed.get(str(args.week), []))
    week_done.discard(args.task)
    completed[str(args.week)] = sorted(week_done)

    save_json(PROGRESS_PATH, progress)
    print(f"Reaberto: Semana {args.week}, tarefa {args.task}")


def cmd_log(args):
    _tasks, progress = load_state()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = {
        "timestamp": now,
        "week": progress.get("current_week", 1),
        "text": args.text,
    }
    progress.setdefault("sessions", []).append(entry)
    save_json(PROGRESS_PATH, progress)

    with JOURNAL_PATH.open("a", encoding="utf-8") as file:
        file.write(f"\n### {now} - Semana {entry['week']}\n\n")
        file.write(f"{args.text}\n")

    print("Sessao registrada no journal.md.")


def build_parser():
    parser = argparse.ArgumentParser(description="Harness de estudo para o roadmap de Cyber Security.")
    subparsers = parser.add_subparsers(required=True)

    status = subparsers.add_parser("status", help="Mostra progresso geral e semana atual.")
    status.set_defaults(func=cmd_status)

    next_step = subparsers.add_parser("next", help="Mostra a proxima tarefa pendente.")
    next_step.set_defaults(func=cmd_next)

    week = subparsers.add_parser("week", help="Seleciona e mostra uma semana.")
    week.add_argument("week", type=int)
    week.set_defaults(func=cmd_week)

    done = subparsers.add_parser("done", help="Marca uma tarefa como concluida.")
    done.add_argument("week", type=int)
    done.add_argument("task", type=int)
    done.set_defaults(func=cmd_done)

    undo = subparsers.add_parser("undo", help="Reabre uma tarefa concluida.")
    undo.add_argument("week", type=int)
    undo.add_argument("task", type=int)
    undo.set_defaults(func=cmd_undo)

    log = subparsers.add_parser("log", help="Registra uma sessao de estudo.")
    log.add_argument("text")
    log.set_defaults(func=cmd_log)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
