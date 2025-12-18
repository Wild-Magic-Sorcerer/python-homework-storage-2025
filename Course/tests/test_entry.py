"""Тесты Entry."""

from datetime import datetime

import pytest

from minidiary.entry import Entry


def test_entry_creation():
    entry = Entry(datetime(2024, 12, 17, 10, 30), "Тест", frozenset({"тег"}))
    assert entry.text == "Тест"
    assert "тег" in entry.tags
    assert entry.id


def test_entry_default_tags():
    entry = Entry(datetime.now(), "Текст")
    assert entry.tags == frozenset()


def test_has_tag_case_insensitive():
    entry = Entry(datetime.now(), "Текст", frozenset({"Работа"}))
    assert entry.has_tag("работа")
    assert entry.has_tag("РАБОТА")


def test_matches_date():
    entry = Entry(datetime(2024, 12, 17, 10, 30), "Текст")
    assert entry.matches_date(datetime(2024, 12, 17, 23, 59))
    assert not entry.matches_date(datetime(2024, 12, 18))


def test_serialization():
    entry = Entry(datetime(2024, 12, 17, 10, 30), "Текст", frozenset({"тег"}))
    data = entry.to_dict()
    restored = Entry.from_dict(data)
    assert restored.id == entry.id
    assert restored.text == entry.text
    assert restored.tags == entry.tags
