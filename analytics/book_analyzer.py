import re
from .base_analyzer import BaseAnalyzer
from .utils import log_action

class BookAnalyzer(BaseAnalyzer):
    """
    Specialized entity demonstrating Inheritance and Polymorphic behaviors.
    Analyzes vocabulary and general text metrics.
    """
    def __init__(self, title: str, raw_text: str):
        super().__init__(title, raw_text)
        self.words = self._tokenize()

    def _tokenize(self) -> list:
        """Cleans and converts raw text string into a list of normalized words."""
        if not self._raw_text:
            return []
        clean_text = re.sub(r'[^\w\s]', '', self._raw_text.lower())
        return clean_text.split()

    @log_action
    def get_top_words(self, limit: int = 5) -> list:
        """Extracts most common meaningful words from the internal list."""
        stop_words = {'the', 'and', 'is', 'in', 'it', 'of', 'to', 'a', 'that', 'this', 'he', 'she', 'was', 'for', 'on'}
        word_counts = {}

        for word in self.words:
            if word not in stop_words and len(word) > 2:
                word_counts[word] = word_counts.get(word, 0) + 1

        sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_words[:limit]

    def analyze_sentiment(self) -> str:
        """Evaluates textual sentiment metrics based on lexicon maps."""
        positive_words = {'good', 'great', 'happy', 'excellent', 'love', 'best', 'beautiful', 'hero'}
        negative_words = {'bad', 'sad', 'terrible', 'worst', 'hate', 'awful', 'evil', 'villain', 'death'}

        score = 0
        for word in self.words:
            if word in positive_words:
                score += 1
            elif word in negative_words:
                score -= 1

        if score > 0:
            return f"Positive (Score: {score})"
        elif score < 0:
            return f"Negative (Score: {score})"
        return "Neutral (Score: 0)"

    def analyze(self) -> dict:
        """Polymorphic execution overriding the BaseAnalyzer signature."""
        return {
            "title": self.title,
            "total_words": len(self.words),
            "sentiment": self.analyze_sentiment(),
            "top_features": dict(self.get_top_words(limit=3))
        }