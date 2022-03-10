"""
Created on Wed Mar 9 05:34:00 2022

In this file it will build the main clase of the game

@author: jesus
"""

import pygame
import Game as SKG
import SettingFile as STF
import ImageRegister as IR
import LevelMaker
# import json


# background_rect = background_image.get_rect()
# background_rect.topleft = (0, 0)

class ZombieGame( SKG.Game ):
    
    def __init__( self ):
        # Calling the init method from Base Class
        super().__init__()
        
        # Main Sprites groups for Game
        self.platforms_group    = pygame.sprite.Group()
        self.all_tiles_group    = pygame.sprite.Group()
        self.player_gruop       = pygame.sprite.Group()
        self.enemies_group      = pygame.sprite.Group()
        self.portals_group      = pygame.sprite.Group()
        self.rubi_groups        = pygame.sprite.Group()
        self.bullet_group       = pygame.sprite.Group()
        
        # Dictionary with Images
        self.sprite_dictionary = IR.ImageRegister()
        
        self.background_rect = self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ).get_rect()
        self.background_rect.topleft = ( 0, 0 )
        
        level_builder = LevelMaker.LevelMaker(STF.PATH_LEVEL_JSON, self.all_tiles_group, self.platforms_group, self.sprite_dictionary )
        self.isMapBult = level_builder.IsMapBuilded()
        
    def __UpdateGameState__( self ):
        """
            Update Logic Game each Frame Game. This is the function that the base clase
            Game is executation countinously inside the loop game
        """
        
        # Fill the display surface to cover old images
        self.display_surface.blit( self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ), self.background_rect )   

        #Draw tiles and update ruby maker
        self.all_tiles_group.update()
        self.all_tiles_group.draw( self.display_surface )

        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )
    
    
my_game = ZombieGame(); my_game.RunGame()

# f = open( STF.PATH_LEVEL_JSON )
# level = json.load( f )
# level = level["level"]
# f.close()
