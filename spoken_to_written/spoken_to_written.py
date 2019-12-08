import json
import os
import re
from word2number import w2n


class logic_component:

    def __init__(self, rules_loc=None):
        self.set_rules(rules_loc)

    def set_rules(self, rules_loc):
        raise NotImplementedError(
            'Implement this method. This method sets rules for the logic')

    def logic(self, text):
        raise NotImplementedError(
            'Implement the logic of this component in this method')


class parsing_component:

    def __init__(self):
        raise NotImplementedError

    def parse_rule(self):
        raise NotImplementedError

    def parse_logic(self):
        raise NotImplementedError


class logic_numbers(logic_component):

    def set_rules(self, rules_loc):
        num_tokens = ('(one|two|three|four|five|six|seven|eight|nine|ten|'
                      'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|'
                      'twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|'
                      'hundred|thousand|million|billion|trillion)')

        self.num_reg = '( )' + '(' + num_tokens + \
            '(' + ' ' + num_tokens + ')' + '*' + ')'

    def logic(self, text):
        return re.sub(self.num_reg, word_to_number, text)


class logic_common_regex(logic_component):

    def set_rules(self, rules_loc):

        if rules_loc is None:
            rules_loc = os.path.dirname(os.path.realpath(
                __file__)) + '/conversion_rules.json'

        self.rules = None
        with open(rules_loc, "r") as rules:
            self.rules = json.load(rules)

    def logic(self, text):
        for rule in self.rules['rules']:
            if rule['type'] == 'regex':
                text = re.sub(rule['search'],
                              rule['replace'], text)

        return text


class stw:

    def __init__(self, rules_file=None):

        if rules_file is None:
            rules_file = os.path.dirname(os.path.realpath(
                __file__)) + '/conversion_rules.json'

        self.rules = None
        with open(rules_file, "r") as rules:
            self.rules = json.load(rules)

    def parse(self, text):
        text = self.replace_word_numbers(text)
        text = self.parse_on_regex_rules(text)

        return text

    def parse_on_regex_rules(self, text):
        for rule in self.rules['rules']:
            if rule['type'] == 'regex':
                text = re.sub(rule['search'],
                              rule['replace'], text)

        return text

    def replace_word_numbers(self, text):
        num_tokens = ('(one|two|three|four|five|six|seven|eight|nine|ten|'
                      'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|'
                      'twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|'
                      'hundred|thousand|million|billion|trillion)')

        num_reg = '( )' + '(' + num_tokens + \
            '(' + ' ' + num_tokens + ')' + '*' + ')'

        return re.sub(num_reg, word_to_number, text)


def word_to_number(match):
    word = match.group(0)
    try:
        num = w2n.word_to_num(word)
        if type(num) is int:
            return ' ' + str(num)
        else:
            return word
    except:
        return word
