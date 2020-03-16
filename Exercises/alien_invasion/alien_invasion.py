import pygame

from settings import Settings
from ship import Ship, BadShip
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship and a bad ship.
    ship = Ship(ai_settings, screen)
    bad_ship = BadShip(screen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bad_ship)

run_game()
