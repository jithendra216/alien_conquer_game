import pygame

class Ship:
      """class to manage the player's ship behaviour"""
      def __init__(self,ad_game):
            """initializes the ship and sets it to starting position"""
            self.screen=ad_game.screen
            self.screen_rect=ad_game.screen.get_rect()
            #load the ship image and get its rect
            self.image=pygame.image.load('images/ship.bmp')
            self.rect=self.image.get_rect()
            #set each new ship at the center bottom
            self.rect.midbottom=self.screen_rect.midbottom
            #movement flag
            self.moving_right = False
            self.moving_left = False

      def blitme(self):
            """draw the ship at its current location"""
            self.screen.blit(self.image,self.rect)
      
      def update(self):
            """update the ship's position based on movement flags"""
            if self.moving_right:
                  self.rect.x += 1
            if self.moving_left:
                  self.rect.x -= 1