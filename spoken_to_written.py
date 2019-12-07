import json


class spoken_to_written:

    def __init__(self, rules_file='conversion_rules.json'):
        self.rules = None
        with open("conversion_rules.json", "r") as rules:
            self.rules = json.load(rules)

    def parse(self):
        pass
