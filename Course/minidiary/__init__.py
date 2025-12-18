"""
minidiary — пакет для ведения личного дневника с анализом настроения.

Модули:
    entry — класс записи дневника
    diary — менеджер записей
    mood — анализ настроения текста
"""

__version__ = "1.0.0"
__author__ = "Прокофьева Алла"

from minidiary.diary import Diary
from minidiary.entry import Entry
from minidiary.mood import Mood, MoodAnalyzer

__all__ = ["Entry", "Diary", "MoodAnalyzer", "Mood"]
