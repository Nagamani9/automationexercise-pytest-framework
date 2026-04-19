from pathlib import Path
import yaml


def load_config():
    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "test_data" / "config.yaml"

    print("Loading config from:", config_path)

    with open(config_path, "r") as f:
        return yaml.safe_load(f)