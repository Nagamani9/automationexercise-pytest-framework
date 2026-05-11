from pathlib import Path
import yaml


class ConfigManager:

    _config = None

    @classmethod
    def load_config(cls):

        if cls._config is None:

            current_file = Path(__file__).resolve()

            project_root = current_file.parents[2]

            config_path = project_root / "configs" / "config.yaml"

            print(f"CONFIG PATH: {config_path}")

            if not config_path.exists():
                raise FileNotFoundError(
                    f"Config file not found: {config_path}"
                )

            with open(config_path, "r") as file:
                cls._config = yaml.safe_load(file)

        return cls._config

    @classmethod
    def get(cls, key):

        config = cls.load_config()

        return config.get(key)