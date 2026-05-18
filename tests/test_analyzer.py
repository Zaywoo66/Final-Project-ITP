import unittest
from analytics.base_analyzer import BaseAnalyzer
from analytics.book_analyzer import BookAnalyzer
from analytics.processor import TextBatchProcessor


class SystemComprehensiveTestSuite(unittest.TestCase):
    """Verification Suite executing 5 distinctive test targets (Section 6)."""

    def setUp(self):
        """Prepare system mocks prior to executing individual test cases."""
        self.mock_title = "The Great Adventure!"
        self.mock_text = "The hero fought bravely against an evil villain. A beautiful ending!"
        self.analyzer = BookAnalyzer(self.mock_title, self.mock_text)

    def test_regex_title_cleaning(self):
        """Test 1: Verifies Regex engine isolates illegal punctuation from names."""
        # 'The Great Adventure!' should filter to 'The Great Adventure'
        self.assertEqual(self.analyzer.title, "The Great Adventure")

    def test_tokenization_integrity(self):
        """Test 2: Validates character split conversion works without data loss."""
        self.assertGreater(len(self.analyzer.words), 0)
        self.assertNotIn("bravely.", self.analyzer.words)  # Checks text sanitization

    def test_functional_filters(self):
        """Test 3: Confirms functional lambda filters correctly extract target elements."""
        orchestrator = TextBatchProcessor()
        orchestrator.add_analyzer(self.analyzer)

        positive_hits = orchestrator.filter_by_sentiment("Positive")
        self.assertEqual(len(positive_hits), 1)

    def test_polymorphic_payload_generation(self):
        """Test 4: Verifies structured dictionaries deliver target signature fields."""
        payload = self.analyzer.analyze()
        self.assertIn("total_words", payload)
        self.assertIn("sentiment", payload)

    def test_encapsulation_boundaries(self):
        """Test 5: Verifies protected variable paradigms work via standard getters."""
        with self.assertRaises(AttributeError):
            # Attempting to assign value directly to a read-only property context
            self.analyzer.title = "Malicious Title Re-assignment"


if __name__ == '__main__':
    unittest.main()