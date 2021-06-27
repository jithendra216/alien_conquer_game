import sys

import pygame

from settings import Settings

from ship import Ship

# from soldier import Soldier

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
            self.ship=Ship(self)
            # self.soldier=Soldier(self)#testing purpose
            #set the background color
            # #self.bg_color=(230,230,230);

      def run_game(self):
            """starts the main loop for the game"""
            while(True):
                  self._check_events()
                  self.ship.update()
                  self._update_screen()
                  
      
      def _check_events(self):
            """Manages the user inputs"""
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()
                  elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                              self.ship.moving_right = True
                        elif event.key == pygame.K_LEFT:
                              self.ship.moving_left = True
                  elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                              self.ship.moving_right = False
                        elif event.key == pygame.K_LEFT:
                              self.ship.moving_left = False
      
      def _update_screen(self):
            """manages the updates to the screen as a result of user actions and flips to the new screen"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # self.soldier.bring_soldier()#just for the testing purpose
            pygame.display.flip()

if __name__ == '__main__':
      #make a game instance and run the game
      ad = AlienDestruction()
      ad.run_game()