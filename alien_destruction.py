import sys

import pygame

from settings import Settings

from ship import Ship
from bullet import Bullet

# from soldier import Soldier

class AlienDestruction:
      """Main class which manages overall game behavior
            assets"""
      def __init__(self):
            """Initializes the game and creates game
                  resources"""
            pygame.init()
            self.settings=Settings()
            self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_height = self.screen.get_rect().height
            self.settings.screen_width = self.screen.get_rect().width
            
            pygame.display.set_caption("Alien Destruction")
            self.ship = Ship(self)
            self.bullets = pygame.sprite.Group()
            # self.soldier=Soldier(self)#testing purpose
            #set the background color
            # #self.bg_color=(230,230,230);

      def run_game(self):
            """starts the main loop for the game"""
            while(True):
                  self._check_events()
                  self.ship.update()
                  self.bullets.update()
                  self._update_screen()                
      
      def _check_events(self):
            """Manages the user inputs"""
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()
                  elif event.type == pygame.KEYDOWN:
                        self._check_keydown_events(event)
                  elif event.type == pygame.KEYUP:
                        self._check_keyup_events(event)
      
      def _check_keydown_events(self,event):
            """responds to key presses"""
            if event.key == pygame.K_RIGHT:
                  self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                  self.ship.moving_left = True
            elif event.key == pygame.K_q:
                  sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

      def _check_keyup_events(self,event):
            """responds to key releases"""
            if event.key == pygame.K_RIGHT:
                  self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                  self.ship.moving_left = False
      
      def _fire_bullet(self):
            """create a new bullet and add it to the bullets group"""
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
      
      def _update_screen(self):
            """manages the updates to the screen as a result of user actions and flips to the new screen"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            # self.soldier.bring_soldier()#just for the testing purpose
            pygame.display.flip()

if __name__ == '__main__':
      #make a game instance and run the game
      ad = AlienDestruction()
      ad.run_game()