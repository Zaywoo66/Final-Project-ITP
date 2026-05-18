from .storage import FileHandler

class DatabaseManager:
    """Manages records processing and bridges system actions to disk assets."""
    def __init__(self, system_storage_path: str = "project_database.json"):
        self.database_path = system_storage_path

    def commit_record(self, historical_payload: dict) -> None:
        """Appends and updates records history into flat records files safely."""
        current_state_records = FileHandler.read_json(self.database_path)
        current_state_records.append(historical_payload)
        FileHandler.write_json(self.database_path, current_state_records)
        print(f"[DATABASE MANAGER] Session tracking committed to '{self.database_path}'.")

    def pull_historical_records(self) -> list:
        """Retrieves history metrics lists parsed for verification checks."""
        return FileHandler.read_json(self.database_path)