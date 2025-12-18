"""CLI для minidiary."""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from minidiary import Diary, MoodAnalyzer, __version__
from minidiary.diary import EntryNotFoundError

DEFAULT_PATH = Path.home() / ".minidiary" / "diary.json"


def parse_date(s: str) -> datetime:
    """Парсит дату из разных форматов."""
    for fmt in ["%Y-%m-%d %H:%M", "%Y-%m-%d", "%d.%m.%Y %H:%M", "%d.%m.%Y"]:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты: {s}")


def cmd_add(diary: Diary, args: argparse.Namespace) -> int:
    date = parse_date(args.date) if args.date else None
    entry = diary.add_entry(args.text, set(args.tags) if args.tags else None, date)
    print(f"Добавлено: {entry.id}")
    return 0


def cmd_list(diary: Diary, args: argparse.Namespace) -> int:
    entries = diary.entries
    if args.tag:
        entries = [e for e in entries if e.has_tag(args.tag)]
    if args.limit:
        entries = entries[:args.limit]
    
    if not entries:
        print("Записей нет")
        return 0
    
    for entry in entries:
        print(entry)
    return 0


def cmd_find(diary: Diary, args: argparse.Namespace) -> int:
    if args.date:
        entries = diary.find_by_date(parse_date(args.date))
    elif args.text:
        entries = diary.search_text(args.text)
    elif args.entry_id:
        try:
            entry = diary.get_entry(args.entry_id)
            print(f"Дата: {entry.date.strftime('%d.%m.%Y %H:%M')}")
            print(f"Метки: {', '.join(entry.tags) or '-'}")
            print(f"Текст:\n{entry.text}")
            return 0
        except EntryNotFoundError as e:
            print(str(e), file=sys.stderr)
            return 1
    else:
        return 1
    
    if not entries:
        print("Не найдено")
        return 0
    for e in entries:
        print(e)
    return 0


def cmd_delete(diary: Diary, args: argparse.Namespace) -> int:
    try:
        entry = diary.get_entry(args.entry_id)
    except EntryNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 1
    
    if not args.force:
        print(f"Удалить: {entry}")
        if input("(y/n): ").strip().lower() != "y":
            print("Отменено")
            return 0
    
    diary.delete_entry(args.entry_id)
    print("Удалено")
    return 0


def cmd_mood(diary: Diary, args: argparse.Namespace) -> int:
    try:
        entry = diary.get_entry(args.entry_id)
    except EntryNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 1
    
    analyzer = MoodAnalyzer()
    result = analyzer.analyze(entry.text)
    
    print(f"Текст: {entry.text[:80]}{'...' if len(entry.text) > 80 else ''}")
    print(f"Настроение: {MoodAnalyzer.get_emoji(result.mood)} {result.mood.value}")
    print(f"Показатель: {result.score:+.2f}")
    if result.positive_words:
        print(f"Позитивные: {', '.join(result.positive_words)}")
    if result.negative_words:
        print(f"Негативные: {', '.join(result.negative_words)}")
    return 0


def cmd_tags(diary: Diary, args: argparse.Namespace) -> int:
    counts = diary.get_tags_count()
    if not counts:
        print("Меток нет")
        return 0
    
    for tag, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  #{tag} ({cnt})")
    return 0


def cmd_clear(diary: Diary, args: argparse.Namespace) -> int:
    if diary.count == 0:
        print("Дневник пуст")
        return 0
    
    if not args.force:
        if input(f"Удалить {diary.count} записей? (y/n): ").strip().lower() != "y":
            print("Отменено")
            return 0
    
    deleted = diary.clear()
    print(f"Удалено: {deleted}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="minidiary", description="Мини-дневник")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("--data-file", default=str(DEFAULT_PATH), help="Файл данных")
    
    sub = parser.add_subparsers(dest="cmd")
    
    # add
    p = sub.add_parser("add", help="Добавить запись")
    p.add_argument("text", help="Текст записи")
    p.add_argument("-t", "--tags", nargs="+", default=[], help="Метки")
    p.add_argument("-d", "--date", help="Дата (YYYY-MM-DD)")
    
    # list
    p = sub.add_parser("list", help="Список записей")
    p.add_argument("-n", "--limit", type=int, help="Лимит")
    p.add_argument("--tag", help="Фильтр по метке")
    
    # find
    p = sub.add_parser("find", help="Поиск")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="По дате")
    g.add_argument("--text", help="По тексту")
    g.add_argument("--id", dest="entry_id", help="По ID")
    
    # delete
    p = sub.add_parser("delete", help="Удалить запись")
    p.add_argument("entry_id", help="ID записи")
    p.add_argument("-f", "--force", action="store_true", help="Без подтверждения")
    
    # mood
    p = sub.add_parser("mood", help="Анализ настроения")
    p.add_argument("entry_id", help="ID записи")
    
    # tags
    sub.add_parser("tags", help="Список меток")
    
    # clear
    p = sub.add_parser("clear", help="Очистить дневник")
    p.add_argument("-f", "--force", action="store_true", help="Без подтверждения")
    
    args = parser.parse_args()
    
    if not args.cmd:
        parser.print_help()
        return 0
    
    diary = Diary(args.data_file)
    
    handlers = {
        "add": cmd_add, "list": cmd_list, "find": cmd_find,
        "delete": cmd_delete, "mood": cmd_mood, "tags": cmd_tags, "clear": cmd_clear,
    }
    return handlers[args.cmd](diary, args)


if __name__ == "__main__":
    sys.exit(main())

