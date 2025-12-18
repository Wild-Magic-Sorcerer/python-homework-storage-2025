"""Класс Diary — менеджер записей дневника."""

import json
from datetime import datetime
from pathlib import Path
from typing import Iterator

from minidiary.entry import Entry


class DiaryError(Exception):
    """Базовая ошибка дневника."""
    pass


class EntryNotFoundError(DiaryError):
    """Запись не найдена."""
    pass


class Diary:
    """
    Менеджер записей с сохранением в JSON.
    
    Args:
        storage_path: Путь к файлу. None — только в памяти.
    """
    
    def __init__(self, storage_path: Path | str | None = None) -> None:
        self._entries: dict[str, Entry] = {}
        self._path = Path(storage_path) if storage_path else None
        
        if self._path and self._path.exists():
            self._load()
    
    @property
    def entries(self) -> list[Entry]:
        """Все записи, отсортированные по дате (новые первые)."""
        return sorted(self._entries.values(), key=lambda e: e.date, reverse=True)
    
    @property
    def count(self) -> int:
        return len(self._entries)
    
    def add_entry(self, text: str, tags: set[str] | None = None,
                  date: datetime | None = None) -> Entry:
        """Добавляет запись. Текст не может быть пустым."""
        text = text.strip()
        if not text:
            raise ValueError("Текст записи не может быть пустым")
        
        entry = Entry(
            date=date or datetime.now(),
            text=text,
            tags=frozenset(tags) if tags else frozenset(),
        )
        self._entries[entry.id] = entry
        self._save()
        return entry
    
    def delete_entry(self, entry_id: str) -> Entry:
        """Удаляет запись по ID."""
        if entry_id not in self._entries:
            raise EntryNotFoundError(f"Запись {entry_id} не найдена")
        entry = self._entries.pop(entry_id)
        self._save()
        return entry
    
    def get_entry(self, entry_id: str) -> Entry:
        """Возвращает запись по ID."""
        if entry_id not in self._entries:
            raise EntryNotFoundError(f"Запись {entry_id} не найдена")
        return self._entries[entry_id]
    
    def find_by_date(self, target: datetime) -> list[Entry]:
        """Записи за указанную дату."""
        return [e for e in self._entries.values() if e.matches_date(target)]
    
    def find_by_tag(self, tag: str) -> list[Entry]:
        """Записи с указанной меткой."""
        return [e for e in self._entries.values() if e.has_tag(tag)]
    
    def search_text(self, query: str) -> list[Entry]:
        """Поиск по тексту (регистронезависимо)."""
        q = query.lower()
        return [e for e in self._entries.values() if q in e.text.lower()]
    
    def get_all_tags(self) -> set[str]:
        """Все уникальные метки."""
        tags: set[str] = set()
        for entry in self._entries.values():
            tags.update(entry.tags)
        return tags
    
    def get_tags_count(self) -> dict[str, int]:
        """Метки с количеством использований."""
        counts: dict[str, int] = {}
        for entry in self._entries.values():
            for tag in entry.tags:
                counts[tag] = counts.get(tag, 0) + 1
        return counts
    
    def clear(self) -> int:
        """Удаляет все записи. Возвращает количество удалённых."""
        count = len(self._entries)
        self._entries.clear()
        self._save()
        return count
    
    def __iter__(self) -> Iterator[Entry]:
        return iter(self.entries)
    
    def __len__(self) -> int:
        return self.count
    
    def _save(self) -> None:
        if not self._path:
            return
        self._path.parent.mkdir(parents=True, exist_ok=True)
        data = {"entries": [e.to_dict() for e in self._entries.values()]}
        self._path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                              encoding="utf-8")
    
    def _load(self) -> None:
        if not self._path or not self._path.exists():
            return
        try:
            data = json.loads(self._path.read_text(encoding="utf-8"))
            for entry_data in data.get("entries", []):
                entry = Entry.from_dict(entry_data)
                self._entries[entry.id] = entry
        except (json.JSONDecodeError, KeyError) as e:
            raise DiaryError(f"Ошибка загрузки: {e}") from e
