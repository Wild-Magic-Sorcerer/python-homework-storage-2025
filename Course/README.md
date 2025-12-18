# minidiary

Курсовая работа: мини-дневник с анализом настроения.

**Вариант 10** — CLI-приложение для ведения личного дневника с возможностью добавления записей, меток, поиска и анализа эмоциональной окраски текста.

## Требования

- Python 3.11+

## Установка

```bash
cd Course
pip install -e .
```

## Использование

```bash
# добавить запись
minidiary add "Сегодня хороший день" --tags работа

# список записей
minidiary list
minidiary list --tag работа

# поиск
minidiary find --text "хороший"
minidiary find --date 2024-12-17

# анализ настроения
minidiary mood <id>

# теги
minidiary tags

# удалить
minidiary delete <id>
```

## Структура

```
Course/
├── minidiary/
│   ├── __init__.py   # экспорт публичного API
│   ├── entry.py      # класс Entry (запись)
│   ├── diary.py      # класс Diary (менеджер)
│   ├── mood.py       # анализ настроения
│   └── cli.py        # CLI интерфейс
├── tests/            # unit-тесты
├── pyproject.toml
└── README.md
```

## Тесты

```bash
pip install pytest
pytest
```
