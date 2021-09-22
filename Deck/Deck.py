"""
Deck Object File.

Deck is a base class containing a list of Cards

"""

import os
import os.path
import random
import pygame
from Card import Card


class Deck(object):

    def __init__(self, filename=""):
        self._filename = filename
        self._full_path = os.path.abspath(filename)
        self._cards = []
        self._title = ""
        self._max_num = 0
        self._current_num = 0
        self._card_path = ""
        self._graveyard = []
        with open(self._full_path, 'r') as deck_file:
            if os.path.getsize(self._full_path) == 0:
                print("file is empty\n")
                return
            title_line = deck_file.readline()
            print(title_line)
            deck_title = title_line.split("=")
            print(deck_title[0])
            if deck_title[0] == "deck_title":
                self._title = deck_title[1].rstrip()
                print(self._title)
            num_line = deck_file.readline()
            num_cards = num_line.split("=")
            if num_cards[0] == "num_cards":
                self._max_num = int(num_cards[1].rstrip())
            source_line = deck_file.readline()
            card_source = source_line.split("=")
            if card_source[0] == "card_source":
                self._card_path = os.path.join(self._full_path, "../", card_source[1].rstrip())
                print(self._card_path)
            # Create append file to the list for each file in the directory, if it's a file
            # then assign the length of the list to card_folder_size
            # card_folder_size = len([filename for filename in os.listdir(self._card_source)])

            card_folder_size = len([name for name in os.listdir(self._card_path)
                                    if os.path.isfile(os.path.join(self._card_path, name))])
            print(card_folder_size)
            print(self._max_num)

            if(self._max_num != card_folder_size):
                print("Does not Match!")
                return
            self.build_deck()

    def build_deck(self):
        # for card in os.listdir(self._card_source):
        #    self._cards.append(Card(os.path.join(self._card_source, card)))
        for card in os.listdir(self._card_path):
            if os.path.getsize(os.path.join(self._card_path, card)) == 0:
                print("file is empty\n")
            else:
                self._cards.append(Card(os.path.join(self._card_path, card)))
        self._current_num = len(self._cards)
        random.shuffle(self._cards)

    def print_deck(self):
        for card in self._cards:
            card.display()

    def draw_deck(self):
        rect = pygame.Rect((0, 0), (150, 250))
        deck_surface = pygame.Surface((160, 260))
        if(len(self._cards) > 0):
            pygame.draw.rect(deck_surface, (100, 100, 100), rect, 0, 5)
        if(len(self._cards) > 1):
            rect = rect.move(5, 5)
            pygame.draw.rect(deck_surface, (255, 100, 100), rect, 0, 5)
        if(len(self._cards) > 2):
            rect = rect.move(5, 5)
            pygame.draw.rect(deck_surface, (100, 100, 100), rect, 0, 5)
        return deck_surface

    def draw_card(self):
        if (self.is_empty()):
            print(self._title, " is empty!")
            return
        return self._cards.pop()

    def go_to_graveyard(self, card):
        self._graveyard.append(card)

    def show_graveyard(self):
        for card in self._graveyard:
            card.display()

    def is_empty(self):
        if(len(self._cards) > 0):
            return False
        return self.reshuffle_from_graveyard()

    def reshuffle_from_graveyard(self) -> bool:
        if (len(self._graveyard) == 0):
            print("All cards are in play")
            return True
        print("Reshuffling Graveyard...")
        self._cards = random.shuffle(self._graveyard)
        self._graveyard = []
        return False
