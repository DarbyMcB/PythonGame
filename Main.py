"""
Main File.

Contains the primary game loop

"""

import pygame
import pygame_menu
from Player import Player
from Map import Map


WIN_SIZE = [1080, 720]


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
    player_list = list(Player(f"Player {x}") for x in range(4))

    print(player_list[0].__dict__.keys())
    for player in player_list:
        print(player.name)

    # Create Game Board
    map = Map(1, WIN_SIZE[0], WIN_SIZE[1])
    # Generate a Background color and fill
    screen.fill((0, 0, 0))
    # Draw the board
    map.drawmap(screen)
    # Prepare the Game Clock
    clock = pygame.time.Clock()
    run = True
    fps = 30
    while run:
        # lock Framerate
        clock.tick(fps)
        # Process Input
        pygame.display.set_caption('Python Hex Game')
        menu = pygame_menu.Menu(width=800, height=600,
                                theme=pygame_menu.themes.THEME_DARK, title='Sick Menu Huh?')
        menu.mainloop(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Updates the display with all changes
        pygame.display.update()
    return 1


if __name__ == '__main__':
    main()
