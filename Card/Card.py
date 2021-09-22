"""
Card Object File

Card is a base class containing a name and rules text

"""
import os
import os.path


class Card(object):

    def __init__(self, card_path):
        self._full_path = card_path
        self._title = ""
        self._cost = 0
        self._rules = ""
        with open(card_path, 'r') as new_card_file:
            print("card_file_open")
            card_title = new_card_file.readline().split("=")
            if os.path.getsize(self._full_path) == 0:
                print("file is empty\n")
                return
            if card_title[0] == "card_name":
                self._title = card_title[1].rstrip()
            card_cost = new_card_file.readline().split("=")
            if card_cost[0] == "card_cost":
                self._cost = int(card_cost[1].rstrip())
            card_rules = new_card_file.readline().split("=")
            if card_rules[0] == "card_rules":
                self._rules = card_rules[1].rstrip()
            print(self._title)
            print(self._cost)
            print(self._rules + '\n')

    def display(self):
        print(self._title)
        print(self._cost)
        print(self._rules + '\n')
