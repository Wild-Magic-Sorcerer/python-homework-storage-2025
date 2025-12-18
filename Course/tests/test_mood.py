"""Тесты MoodAnalyzer."""

import pytest

from minidiary.mood import Mood, MoodAnalyzer


def test_positive_text():
    analyzer = MoodAnalyzer()
    result = analyzer.analyze("Счастье радость любовь!")
    assert result.mood in (Mood.POSITIVE, Mood.VERY_POSITIVE)
    assert result.score > 0


def test_negative_text():
    analyzer = MoodAnalyzer()
    result = analyzer.analyze("Грусть тоска печаль")
    assert result.mood in (Mood.NEGATIVE, Mood.VERY_NEGATIVE)
    assert result.score < 0


def test_neutral_text():
    analyzer = MoodAnalyzer()
    result = analyzer.analyze("Сегодня понедельник")
    assert result.mood == Mood.NEUTRAL


def test_empty_text():
    analyzer = MoodAnalyzer()
    result = analyzer.analyze("")
    assert result.mood == Mood.NEUTRAL
    assert result.score == 0.0


def test_score_bounds():
    analyzer = MoodAnalyzer()
    r1 = analyzer.analyze("счастье " * 50)
    r2 = analyzer.analyze("грусть " * 50)
    assert -1.0 <= r1.score <= 1.0
    assert -1.0 <= r2.score <= 1.0


def test_emoji():
    assert MoodAnalyzer.get_emoji(Mood.POSITIVE) == "🙂"
    assert MoodAnalyzer.get_emoji(Mood.NEGATIVE) == "😔"
