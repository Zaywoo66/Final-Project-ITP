import functools
import time

def log_action(func):
    """Custom Decorator (Section 6) that profiles execution metrics of actions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG TRACE] Entering method context: '{func.__name__}'")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"[LOG TRACE] Finished '{func.__name__}' in {duration:.6f} seconds.")
        return result
    return wrapper

class LineReaderGenerator:
    """Custom Iterator/Generator implementation (Section 6) for large streaming structures."""
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_lines(self):
        """Yield-based text line stream to prevent high-memory system stalls."""
        with open(self.file_path, 'r', encoding='utf-8') as selected_file:
            for native_line in selected_file:
                cleaned_line = native_line.strip()
                if cleaned_line:
                    yield cleaned_line