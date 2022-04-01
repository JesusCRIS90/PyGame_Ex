"""
Created on Wed Mar 9 05:34:00 2022

In this file it will build the main clase of the game

@author: jesus
"""

import pygame
import Game as SKG
import SettingFile as STF
import ImageRegister as IR
import InGame_Parameters as IGP
import LevelMaker
from Player import Player
# import json


# background_rect = background_image.get_rect()
# background_rect.topleft = (0, 0)

class ZombieGame( SKG.Game ):
    
    def __init__( self ):
        # Calling the init method from Base Class
        super().__init__()
        
        # Setting Canvas Display to Game Dictionary
        IGP.GAME_PARAMETERS["CanvasGame"] = self.display_surface
        
        # Dictionary with Images
        self.sprite_dictionary = IR.ImageRegister()
        
        # Main Sprites groups for Game
        self.platforms_group    = pygame.sprite.Group()
        self.all_tiles_group    = pygame.sprite.Group()
        self.player_gruop       = pygame.sprite.Group()
        self.enemies_group      = pygame.sprite.Group()
        self.portals_group      = pygame.sprite.Group()
        self.rubi_groups        = pygame.sprite.Group()
        self.bullet_group       = pygame.sprite.Group()
        
        # Assign these sprites to the GroupSprite Dictionary
        IGP.GAME_SPRITES_GROUPS["Tiles_Group"]          = self.all_tiles_group
        IGP.GAME_SPRITES_GROUPS["Platform_Group"]       = self.platforms_group 
        IGP.GAME_SPRITES_GROUPS["Player_Group"]         = self.player_gruop
        IGP.GAME_SPRITES_GROUPS["Enemies_Group"]        = self.enemies_group
        IGP.GAME_SPRITES_GROUPS["Portals_Group"]        = self.portals_group
        IGP.GAME_SPRITES_GROUPS["Rubies_Group"]         = self.rubi_groups
        IGP.GAME_SPRITES_GROUPS["PlayerBullet_Group"]   = self.bullet_group
        
        
        self.background_rect = self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ).get_rect()
        self.background_rect.topleft = ( 0, 0 )
        
        level_builder = LevelMaker.LevelMaker(STF.PATH_LEVEL_JSON, self.all_tiles_group, self.platforms_group, self.sprite_dictionary )
        self.isMapBult = level_builder.IsMapBuilded()
        
        
        # Create Player
        player_pos = level_builder.GetPlayerPosition()
        player = Player( player_pos[ 0 ]*32 - 32, 
                         player_pos[ 1 ]*32 + 32, 
                         self.sprite_dictionary, 
                         IGP.GAME_SPRITES_GROUPS["Platform_Group"], 
                         IGP.GAME_SPRITES_GROUPS["Portals_Group"],
                         IGP.GAME_SPRITES_GROUPS["PlayerBullet_Group"] )
        self.player = player       
        IGP.GAME_SPRITES_GROUPS["Player_Group"].add( player )

        
        
    def __UpdateGameState__( self ):
        """
            Update Logic Game each Frame Game. This is the function that the base clase
            Game is executation countinously inside the loop game
        """
        
        # Fill the display surface to cover old images
        self.display_surface.blit( self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ), self.background_rect )   

        #Draw tiles
        self.all_tiles_group.draw( self.display_surface )
        self.all_tiles_group.update()

        # Draw and Update Player
        self.player_gruop.update()
        self.player_gruop.draw( self.display_surface )

        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )
        
        
    def _CheckingEvents_( self ):
        """Checking Player Events"""
        # Loop through a list of Event Objects that have occured
        for event in pygame.event.get():
            # print( event )
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                #Player wants to jump
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                #Player wants to fire
                if event.key == pygame.K_UP:
                    self.player.fire()
                        
                        

    
    
my_game = ZombieGame() 
my_game.RunGame()




# imag_reg = IR.ImageRegister()


# temp_sprite_list1 = imag_reg.GetSprite( IR.Player_Sprites_Types.IDLE_LEFT )
# temp_sprite_list2 = imag_reg.GetSprite( IR.Player_Sprites_Types.IDLE_RIGTH )

# temp_sprite_list3 = imag_reg.GetSprite( IR.Player_Sprites_Types.ATTACK_LEFT )
# temp_sprite_list4 = imag_reg.GetSprite( IR.Player_Sprites_Types.ATTACK_RIGTH )

# temp_sprite_list5 = imag_reg.GetSprite( IR.Player_Sprites_Types.JUMP_LEFT )
# temp_sprite_list6 = imag_reg.GetSprite( IR.Player_Sprites_Types.JUMP_RIGHT )

# temp_sprite_list7 = imag_reg.GetSprite( IR.Player_Sprites_Types.RUN_LEFT )
# temp_sprite_list8 = imag_reg.GetSprite( IR.Player_Sprites_Types.RUN_RIGTH )

