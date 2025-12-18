"""Анализ настроения текста на основе ключевых слов."""

from dataclasses import dataclass
from enum import Enum


class Mood(Enum):
    """Категории настроения."""
    VERY_POSITIVE = "очень позитивное"
    POSITIVE = "позитивное"
    NEUTRAL = "нейтральное"
    NEGATIVE = "негативное"
    VERY_NEGATIVE = "очень негативное"


@dataclass(frozen=True)
class MoodResult:
    """Результат анализа настроения."""
    mood: Mood
    score: float  # от -1.0 до 1.0
    positive_words: tuple[str, ...]
    negative_words: tuple[str, ...]


class MoodAnalyzer:
    """
    Анализатор настроения на основе словарей позитивных/негативных слов.
    
    Использует простой подход: подсчёт слов из словарей.
    """
    
    # Базовые словари (русский)
    POSITIVE = frozenset({
        "счастье", "счастлив", "радость", "рад", "отлично", "прекрасно",
        "замечательно", "любовь", "люблю", "хорошо", "успех", "победа",
        "удача", "интересно", "вдохновение", "позитив", "благодарность",
        "улыбка", "смех", "весело", "праздник", "красиво", "добро",
        "нравится", "приятно", "здорово", "круто", "супер", "класс",
    })
    
    NEGATIVE = frozenset({
        "грусть", "грустно", "печаль", "тоска", "плохо", "ужасно",
        "кошмар", "страх", "боюсь", "тревога", "беспокойство", "злость",
        "раздражение", "бесит", "ненависть", "разочарование", "обида",
        "одиночество", "скучно", "усталость", "устал", "стресс",
        "провал", "неудача", "болезнь", "болит", "слёзы", "плачу",
        "проблема", "сложно", "трудно",
    })
    
    def __init__(self, positive: frozenset[str] | None = None,
                 negative: frozenset[str] | None = None) -> None:
        self._positive = positive or self.POSITIVE
        self._negative = negative or self.NEGATIVE
    
    def analyze(self, text: str) -> MoodResult:
        """Анализирует текст и возвращает результат."""
        words = self._tokenize(text)
        
        pos_found = [w for w in words if w in self._positive]
        neg_found = [w for w in words if w in self._negative]
        
        score = self._calc_score(len(pos_found), len(neg_found))
        mood = self._score_to_mood(score)
        
        return MoodResult(
            mood=mood,
            score=score,
            positive_words=tuple(set(pos_found)),
            negative_words=tuple(set(neg_found)),
        )
    
    def _tokenize(self, text: str) -> list[str]:
        """Извлекает слова (>2 букв) в нижнем регистре."""
        cleaned = "".join(c if c.isalpha() else " " for c in text.lower())
        return [w for w in cleaned.split() if len(w) > 2]
    
    def _calc_score(self, pos: int, neg: int) -> float:
        """Вычисляет показатель от -1 до 1."""
        total = pos + neg
        if total == 0:
            return 0.0
        return max(-1.0, min(1.0, (pos - neg) / total))
    
    def _score_to_mood(self, score: float) -> Mood:
        if score >= 0.6:
            return Mood.VERY_POSITIVE
        if score >= 0.2:
            return Mood.POSITIVE
        if score <= -0.6:
            return Mood.VERY_NEGATIVE
        if score <= -0.2:
            return Mood.NEGATIVE
        return Mood.NEUTRAL
    
    @staticmethod
    def get_emoji(mood: Mood) -> str:
        """Возвращает эмодзи для настроения."""
        return {
            Mood.VERY_POSITIVE: "😄",
            Mood.POSITIVE: "🙂",
            Mood.NEUTRAL: "😐",
            Mood.NEGATIVE: "😔",
            Mood.VERY_NEGATIVE: "😢",
        }.get(mood, "❓")
