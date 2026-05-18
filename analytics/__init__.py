"""
Analytics package initialization.
Exposes core text-processing entities for easier importing.
"""
from .base_analyzer import BaseAnalyzer
from .book_analyzer import BookAnalyzer
from .processor import TextBatchProcessor
from .utils import log_action, LineReaderGenerator