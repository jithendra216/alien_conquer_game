import sys

import pygame

from settings import Settings

class AlienDestruction:
      """Main class which manages overall game behavior
            assets"""
      def __init__(self):
            """Initializes the game and creates game
                  resources"""
            pygame.init()
            self.settings=Settings()
            self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
            pygame.display.set_caption("Alien Destruction")
            #set the background color
            # #self.bg_color=(230,230,230);

      def run_game(self):
            """starts the main loop for the game"""
            while(True):
                  #watch for keyboard and mouse events
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              sys.exit()
                  
                  #fill the screen window with defined background color
                  self.screen.fill(self.settings.bg_color)

                  #make the most recently drawn screen visible
                  pygame.display.flip()
      

if __name__ == '__main__':
      #make a game instance and run the game
      ad = AlienDestruction()
      ad.run_game()