"""
Main File.

Contains the primary game loop

"""


import pygame
import pygame_menu
from GameController import GameController


WIN_SIZE = [1920, 1020]


def main():
    """
    Run Main().

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """
    # Initialize the Game
    pygame.init()
    # Generate Screen entity
    screen = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
    # Create Player list

    # Generate a Background color and fill
    screen.fill((0, 0, 0))
    # Draw the board
    pygame.display.set_caption('Python Hex Game')
    menu = pygame_menu.Menu(width=800, height=600,
                            theme=pygame_menu.themes.THEME_DARK,
                            title='Sick Menu Huh?',
                            onclose=pygame_menu.events.CLOSE)
    player_num = menu.add.text_input('Number of Players: ', default='2', maxchar=1)
    menu.add.button('Start Game', pygame_menu.events.CLOSE)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    while menu.is_enabled():
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame_menu.events.EXIT
        if menu.is_enabled():
            menu.draw(screen)
            menu.update(events)
        pygame.display.update()
    screen.fill((0, 0, 0))
    start_game(screen, int(player_num.get_value()))
    return 1


def start_game(screen, player_num) -> None:
    """
    Hold Space for Primary GameLoop.

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """
    game = GameController(screen, WIN_SIZE[0], WIN_SIZE[1], player_num)
    game.run_game()


if __name__ == '__main__':
    main()
