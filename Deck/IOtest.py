#!/usr/bin/python

import os
import os.path


def main():
    with open("test_deck.txt", 'r') as deck_file:
        cards = []
        title_line = deck_file.readline()
        print(title_line)
        deck_title = title_line.split("=")
        print(deck_title[0])
        if deck_title[0] == "deck_title":
            title = deck_title[1].rstrip()
        num_line = deck_file.readline()
        num_cards = num_line.split("=")
        if num_cards[0] == "num_cards":
            num = int(num_cards[1].rstrip())
        source_line = deck_file.readline()
        card_source = source_line.split("=")
        if card_source[0] == "card_source":
            source = card_source[1].rstrip()
            print(source)
        card_folder_size = len([name for name in os.listdir(source)
                                if os.path.isfile(os.path.join(source, name))])
        print(card_folder_size)

        if(num != card_folder_size):
            print("Does not Match!")
        else:
            add_cards(source, cards)


def add_cards(source, cards):
    for card in os.listdir(source):
        print(card)
        cards.append(add_card(source, card))

# For the Card initializer


def add_card(source, card):
    full_path = os.path.join(source, card)
    with open(full_path, 'r') as new_card_file:
        print("card_file_open")
        card_title = new_card_file.readline().split("=")
        if os.path.getsize(full_path) == 0:
            print("file is empty\n")
            return
        if card_title[0] == "card_name":
            title = card_title[1].rstrip()
        card_cost = new_card_file.readline().split("=")
        if card_cost[0] == "card_cost":
            cost = int(card_cost[1].rstrip())
        card_rules = new_card_file.readline().split("=")
        if card_rules[0] == "card_rules":
            rules = card_rules[1].rstrip()
        print(title)
        print(cost)
        print(rules + '\n')


if __name__ == '__main__':
    main()
