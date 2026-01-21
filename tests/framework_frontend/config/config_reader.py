import json
from pathlib import Path


class ConfigReader:
    CONFIG_FILE = Path(__file__).parent / 'config.json'

    def __init__(self):
        with open(self.CONFIG_FILE, encoding='utf-8') as f:
            self.config = json.load(f)

    def get(self, key):
        return self.config[key]
