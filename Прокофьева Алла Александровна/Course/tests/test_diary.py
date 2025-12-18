"""Тесты Diary."""

from datetime import datetime
from pathlib import Path

import pytest

from minidiary.diary import Diary, EntryNotFoundError


def test_add_entry():
    diary = Diary()
    entry = diary.add_entry("Текст", {"тег"})
    assert diary.count == 1
    assert entry.text == "Текст"


def test_add_empty_text_raises():
    diary = Diary()
    with pytest.raises(ValueError):
        diary.add_entry("   ")


def test_delete_entry():
    diary = Diary()
    entry = diary.add_entry("Текст")
    diary.delete_entry(entry.id)
    assert diary.count == 0


def test_delete_nonexistent_raises():
    diary = Diary()
    with pytest.raises(EntryNotFoundError):
        diary.delete_entry("fake_id")


def test_find_by_date():
    diary = Diary()
    date = datetime(2024, 12, 17)
    diary.add_entry("1", date=date)
    diary.add_entry("2", date=date)
    diary.add_entry("3", date=datetime(2024, 12, 18))
    assert len(diary.find_by_date(date)) == 2


def test_find_by_tag():
    diary = Diary()
    diary.add_entry("1", {"work"})
    diary.add_entry("2", {"work", "python"})
    diary.add_entry("3", {"rest"})
    assert len(diary.find_by_tag("work")) == 2


def test_search_text():
    diary = Diary()
    diary.add_entry("Python programming")
    diary.add_entry("Rest day")
    assert len(diary.search_text("python")) == 1


def test_persistence(tmp_path: Path):
    path = tmp_path / "diary.json"
    
    diary1 = Diary(path)
    entry = diary1.add_entry("Test", {"tag"})
    
    diary2 = Diary(path)
    assert diary2.count == 1
    assert diary2.get_entry(entry.id).text == "Test"


def test_clear():
    diary = Diary()
    diary.add_entry("1")
    diary.add_entry("2")
    assert diary.clear() == 2
    assert diary.count == 0
