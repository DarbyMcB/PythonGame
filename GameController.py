"""
GameLoop Object File.

GameController Holds most "global" objects for the Game Loop

"""
import pygame

from Map import Map
from Deck import Deck
from Player import Player
from UI import UI


class GameController(object):
    """
    GameController Handles The Primary Game Loop.

    Contains Most Game Objects
    """

    def __init__(self, screen, win_size_x, win_size_y, player_num):
        """
        Initialize the GameController.

        Sets up Game Objects for the Rest of the Game
        """
        self._player_list = list(Player(f"Player {x}") for x in range(player_num))
        self._player_num = player_num
        print("The number of players is: ", player_num)
        self._screen = screen
        self._player_turn = 0
        self._ui_player_turn = UI((1820, 10), (100, 50), f"Player {self._player_turn}")
        self._screen.blit(self._ui_player_turn.update(
            f"Player {self._player_turn}"), self._ui_player_turn._location)
        self._core_deck = Deck("Deck/test_deck.txt")
        self._war_deck = []
        self._map = Map(self._player_num, win_size_x, win_size_y)
        self._clock = pygame.time.Clock()
        self._run = True
        self._fps = 30
        self.each_player_draws_hand(self._core_deck)

    def run_game(self):
        """
        Run Primary Game Loop.

        Contains the Primary Game loop
        """
        n = 1
        while self._run:
            # lock Framerate
            self._clock.tick(self._fps)
            # Process Input
            self._map.drawmap(self._screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False
                if (event.type == pygame.KEYDOWN):
                    print("KeyDown")
                    if (event.key == pygame.K_SPACE):
                        print("KeySpace")
                        self.move_to_next_turn()

            """
            All Test Code
            """
            if (self._player_turn == 1 and n == 1):
                self._screen.blit(self._core_deck.draw_deck(), (105, 130))
                for player in self._player_list:
                    self._screen.blit(self._core_deck.draw_deck(), (105, 130))
                for player in self._player_list:
                    print(player._name)
                    player.show_hand()
                    print("Deck: \n")
                    self._core_deck.print_deck()
                print(self._player_list[0]._name)
                print("Playing a card...")
                self._core_deck.go_to_graveyard(self._player_list[0].play_card(1))
                print("The hand:")
                self._player_list[0].show_hand()
                print("Main Deck:")
                self._core_deck.print_deck()
                print("Graveyard:")
                self._core_deck.show_graveyard()
                for player in self._player_list:
                    print(player._name)
                    player.print_units()
                n = 2
            pygame.display.update()

    def each_player_draws_hand(self, deck):
        for i in range(0, 3):
            for player in self._player_list:
                if(deck._title != "Core Deck"):
                    print("Core Deck is missing!")
                    return
                self.draw_cards_from(player, deck, 1)

    def draw_cards_from(self, player, deck, number_to_draw=0):
        for i in range(0, number_to_draw):
            if (deck.is_empty()):
                print("The Deck is empty!")
                return
            print(f"Player {player._name} is drawing card {i}.")
            player.draw_card(deck.draw_card())

    def move_to_next_turn(self):
        print(((self._player_turn + 1) % self._player_num))
        self._player_turn = ((self._player_turn + 1) % self._player_num)
        self._screen.blit(self._ui_player_turn.update(
            f"Player {self._player_turn}"), self._ui_player_turn._location)
