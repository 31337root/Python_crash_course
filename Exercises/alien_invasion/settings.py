class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the gam's settings."""
        # Screen settings
        self.screen_width = 1350
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 252, 0, 255
        self.bullets_allowed = 3
