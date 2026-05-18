import sys
import os
from analytics.book_analyzer import BookAnalyzer
from analytics.processor import TextBatchProcessor
from analytics.utils import LineReaderGenerator
from data.manager import DatabaseManager

BOOKS_DIR = "books"


def clear_screen():
    """Helper to keep the CLI layout clean across execution blocks."""
    os.system('cls' if os.name == 'nt' else 'clear')


def scan_books_directory():
    """Scans the books folder and returns a list of .txt files."""
    if not os.path.exists(BOOKS_DIR):
        os.makedirs(BOOKS_DIR)
        return []

    # Filter only .txt files using the built-in os module
    return [f for f in os.listdir(BOOKS_DIR) if f.endswith('.txt')]


def execution_loop():
    """Main execution loop controlling standard tracking runtimes."""
    db = DatabaseManager()
    batch_processor = TextBatchProcessor()

    while True:
        print("\n" + "=" * 50)
        print("     COLLABORATIVE BOOK ANALYTICS CONSOLE")
        print("=" * 50)
        print("1. Scan 'books/' Folder and Analyze a Book")
        print("2. Filter Tracked Analytics Logs (Functional Tool)")
        print("3. Print Batch Processing History Dashboard")
        print("4. Exit System Application")
        print("-" * 50)

        user_selection = input("Select processing option (1-4): ").strip()

        if user_selection == "1":
            clear_screen()
            available_books = scan_books_directory()

            if not available_books:
                print(f"\n[SYSTEM WARN] No .txt files found in '{BOOKS_DIR}/' folder.")
                print(f"Please drop some text files into the '{BOOKS_DIR}' directory and try again.")
                continue

            print("Available books for analysis:")
            for index, book_file in enumerate(available_books, 1):
                print(f"{index}. {book_file}")
            print("-" * 30)

            try:
                book_choice = int(input(f"Select a book number (1-{len(available_books)}): ")) - 1
                if book_choice < 0 or book_choice >= len(available_books):
                    print("\n[INVALID INPUT] Selection out of range.")
                    continue
            except ValueError:
                print("\n[INVALID INPUT] Please enter a valid number.")
                continue

            selected_filename = available_books[book_choice]
            full_file_path = os.path.join(BOOKS_DIR, selected_filename)

            print(f"\n[SYSTEM] Loading '{selected_filename}' using custom LineReaderGenerator...")

            # Utilizing Section 6 Requirement: Custom Generator/Iterator to stream data
            reader = LineReaderGenerator(full_file_path)
            lines = list(reader.read_lines())
            compiled_content = " ".join(lines)

            # Creating the entity object
            document_title = selected_filename.replace(".txt", "").replace("_", " ").title()
            analyzer = BookAnalyzer(document_title, compiled_content)
            batch_processor.add_analyzer(analyzer)

            # Polymorphic execution
            metrics_results = analyzer.analyze()

            print("\n" + "*" * 40)
            print(f"       PROCESSED SUMMARY REPORT")
            print("*" * 40)
            print(f"Cleaned Title : {metrics_results['title']}")
            print(f"Word Metrics  : {metrics_results['total_words']} processed tokens.")
            print(f"Sentiment     : {metrics_results['sentiment']}")
            print(f"Core Keywords : {metrics_results['top_features']}")

            # Committing state parameters into permanent JSON store paths
            db.commit_record(metrics_results)

        elif user_selection == "2":
            clear_screen()
            target_query = input("Filter tracking logs by sentiment category (Positive/Negative/Neutral): ").strip()
            filtered_matches = batch_processor.filter_by_sentiment(target_query)

            print(f"\n--- Search results matching '{target_query}' ({len(filtered_matches)} found) ---")
            for item in filtered_matches:
                print(f"-> Verified Document Reference Match: {item.title}")

        elif user_selection == "3":
            clear_screen()
            print("\n--- EXTRACTING ALL RECOVERED FILE TRACKS (MAP/LAMBDA RUNTIME) ---")
            all_summaries = batch_processor.extract_all_summaries()
            if not all_summaries:
                print("No live operational track records generated yet during this terminal run.")
            for summary_line in all_summaries:
                print(summary_line)

            print("\n--- PERSISTED SYSTEM RECORDS HISTORY (JSON DATA FILE STORE) ---")
            saved_records = db.pull_historical_records()
            if not saved_records:
                print("No records extracted from backend flat data repositories.")
            for index, historical_log in enumerate(saved_records, 1):
                print(f"{index}. [{historical_log['title']}] Sentiment: {historical_log['sentiment']}")

        elif user_selection == "4":
            print("\nShutting down analytics interfaces securely. Goodbye.")
            sys.exit(0)

        else:
            print("\n[INVALID INPUT] Entry parameters must match standard ranges (1-4).")


if __name__ == "__main__":
    try:
        execution_loop()
    except KeyboardInterrupt:
        print("\nForced termination capture flagged. Exiting framework runtime safely.")
        sys.exit(0)