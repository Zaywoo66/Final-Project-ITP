import json
import os


class FileHandler:
    """Handles raw interactions with File System operations securely."""

    @staticmethod
    def read_json(path: str) -> list:
        """Loads execution state lists safely via target standard paths."""
        if not os.path.exists(path):
            return []
        try:
            with open(path, 'r', encoding='utf-8') as data_file:
                return json.load(data_file)
        except (json.JSONDecodeError, IOError) as error_context:
            print(f"[IO SYSTEM ERROR] Could not read file entity cleanly: {error_context}")
            return []

    @staticmethod
    def write_json(path: str, persistent_payload: list) -> bool:
        """Writes execution history to persistent JSON files safely."""
        try:
            with open(path, 'w', encoding='utf-8') as output_file:
                json.dump(persistent_payload, output_file, indent=4)
                return True
        except IOError as io_error:
            print(f"[IO SYSTEM ERROR] Serialization execution failure: {io_error}")
            return False