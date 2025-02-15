class Settings:
    """Class to store all settings for Cosmic Invaders"""

    def __init__(self):
        """Initialize game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 20, 50)

        # Starry background settings
        self.num_stars = 300
        self.star_min_brightness = 100
        self.star_max_brightness = 255
        self.star_min_radius = 1
        self.star_max_radius = 1
        self.star_color_variation = True

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 7

        # Enemy ship settings
        self.enemy_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
