class Settings:
      """A class to store all settings for alien destruction game."""
      def __init__(self):
            """Initialize the game's settings."""
            #screen settings
            self.screen_width = 800
            self.screen_height = 600
            self.bg_color = (220,220,220)
            self.ship_speed = 1.0
            #bullet settings
            self.bullet_speed = 0.8
            self.bullet_width = 3
            self.bullet_height = 10
            self.bullet_color = (60,60,0)

