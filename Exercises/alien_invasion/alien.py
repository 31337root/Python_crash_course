import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Fraw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen

        # Load the star imagen and set its rect attribute.
        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1350)
        self.rect.y = randint(0, 460)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
