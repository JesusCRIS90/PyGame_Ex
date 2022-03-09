"""
Created on Wed Mar 9 05:34:00 2022

In this file it will build the main clase of the game

@author: jesus
"""

import pygame
import Game as SKG
import SettingFile as STF
import ImageRegister as IR


# background_rect = background_image.get_rect()
# background_rect.topleft = (0, 0)

class ZombieGame( SKG.Game ):
    
    def __init__( self ):
        # Calling the init method from Base Class
        super().__init__()
        
        self.sprite_dictionary = IR.ImageRegister()
        
        self.background_rect = self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ).get_rect()
        self.background_rect.topleft = ( 0, 0 )
        
    def __UpdateGameState__( self ):
        """
            Update Logic Game each Frame Game. This is the function that the base clase
            Game is executation countinously inside the loop game
        """
        
        # Fill the display surface to cover old images
        self.display_surface.blit( self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ), self.background_rect )   


        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )
    
        pass
    
    
my_game = ZombieGame(); my_game.RunGame()

# a = pygame.transform.scale(pygame.image.load("Assets/images/background.png"), (STF.WINDOW_WIDTH, STF.WINDOW_HEIGHT) )