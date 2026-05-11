import json
from pathlib import Path


class DataLoader:

    @staticmethod
    def load_json(relative_path):

        project_root = Path(__file__).resolve().parents[2]

        file_path = project_root / relative_path

        print(f"DATA FILE PATH: {file_path}")

        if not file_path.exists():

            raise FileNotFoundError(
                f"Test data file not found: {file_path}"
            )

        with open(file_path, "r") as file:

            return json.load(file)