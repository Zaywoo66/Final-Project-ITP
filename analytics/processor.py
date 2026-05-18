from .book_analyzer import BookAnalyzer

class TextBatchProcessor:
    """
    Demonstrates Association: This class acts as a Manager entity
    that aggregates, filters, and processes lists of BookAnalyzer objects.
    """
    def __init__(self):
        # Association collection storing internal analyzer object configurations
        self._analyzers = []

    def add_analyzer(self, analyzer: BookAnalyzer):
        """Appends a valid BookAnalyzer object instance to the tracker tracking."""
        self._analyzers.append(analyzer)

    def filter_by_sentiment(self, target_sentiment: str) -> list:
        """
        Uses Functional Programming tools (filter, lambda)
        to isolate analyzers targeting explicit sentiment outcomes.
        """
        # Section 4 Constraint: filter and lambda utilization
        result = filter(
            lambda obj: target_sentiment.lower() in obj.analyze_sentiment().lower(),
            self._analyzers
        )
        return list(result)

    def extract_all_summaries(self) -> list:
        """
        Uses Functional Programming tools (map, lambda)
        to cleanly transform object references to output structures.
        """
        # Section 4 Constraint: map and lambda utilization
        summaries = map(lambda obj: obj.get_summary(), self._analyzers)
        return list(summaries)