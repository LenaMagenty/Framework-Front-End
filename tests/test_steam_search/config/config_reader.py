import json


class ConfigReader:

    def __init__(self):
        with open('tests/test_steam_search/config/config.json', encoding='utf-8') as f:
            self.config = json.load(f)

    def get(self, key):
        return self.config[key]
