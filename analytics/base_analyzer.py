import re

class BaseAnalyzer:
    """
    Abstract Base Class demonstrating Inheritance and Encapsulation.
    All specialized text analyzers must inherit from this class.
    """
    def __init__(self, title: str, raw_text: str):
        # Encapsulation: Protected attributes
        self._title = self._validate_title(title)
        self._raw_text = raw_text

    @property
    def title(self) -> str:
        """Getter for the protected title attribute."""
        return self._title

    def _validate_title(self, title: str) -> str:
        """Regex implementation for input validation (Section 6 Requirement)."""
        # Cleans title to contain only alphanumeric values and spaces
        cleaned = re.sub(r'[^\w\s]', '', title)
        return cleaned.strip() if cleaned.strip() else "Untitled_Document"

    def analyze(self) -> dict:
        """
        Polymorphic interface method.
        Must be overridden by subclasses to provide custom metrics.
        """
        raise NotImplementedError("Subclasses must implement the analyze method.")

    def get_summary(self) -> str:
        """Returns a generic overview of the file entity."""
        return f"Document Title: {self._title} | Content Length: {len(self._raw_text)} chars"