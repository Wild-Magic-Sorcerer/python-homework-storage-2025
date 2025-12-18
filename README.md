# Python Labs

Лабораторные работы по Python.

## Требования

- Python 3.11+

## Структура

```
├── LAB01/          # списки, кортежи, множества, словари
├── LAB02/          # строки
├── LAB03/          # функции, *args, **kwargs, рекурсия
├── LAB04/          # lambda, map, filter, reduce, декораторы
├── LAB05/          # файловые операции
├── LAB06/          # ООП: классы, наследование, инкапсуляция
├── LAB07/          # argparse, CLI
├── LAB08/          # регулярные выражения
└── Course/         # курсовая работа (minidiary)
```

## Запуск

```bash
# лабораторные
python3 LAB01/task_01.py
python3 LAB07/task_02.py 10 5 -o mul

# курсовая
cd Course && pip install -e .
minidiary add "Запись" --tags тег1
minidiary list
```

## Курсовая работа

Вариант 10 — мини-дневник с анализом настроения. См. `Course/README.md`.
