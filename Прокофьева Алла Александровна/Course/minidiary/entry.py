"""Класс Entry — запись дневника."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Entry:
    """
    Запись дневника с датой, текстом и метками.
    
    Attributes:
        date: Дата создания.
        text: Текст записи.
        tags: Набор меток.
        id: Уникальный идентификатор.
    """
    date: datetime
    text: str
    tags: frozenset[str] = field(default_factory=frozenset)
    id: str = field(default="")
    
    def __post_init__(self) -> None:
        if not self.id:
            self.id = f"{self.date.strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}"
        if not isinstance(self.tags, frozenset):
            object.__setattr__(self, "tags", frozenset(self.tags))
    
    def __str__(self) -> str:
        date_str = self.date.strftime("%d.%m.%Y %H:%M")
        preview = self.text[:50] + "..." if len(self.text) > 50 else self.text
        tags_str = ", ".join(sorted(self.tags)) if self.tags else "-"
        return f"[{date_str}] {preview} (#{tags_str})"
    
    def has_tag(self, tag: str) -> bool:
        """Проверяет наличие метки (регистронезависимо)."""
        return tag.lower() in {t.lower() for t in self.tags}
    
    def matches_date(self, target: datetime) -> bool:
        """Проверяет совпадение даты (без учёта времени)."""
        return self.date.date() == target.date()
    
    def to_dict(self) -> dict:
        """Сериализация в словарь."""
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "text": self.text,
            "tags": list(self.tags),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Entry":
        """Десериализация из словаря."""
        return cls(
            id=data["id"],
            date=datetime.fromisoformat(data["date"]),
            text=data["text"],
            tags=frozenset(data.get("tags", [])),
        )
