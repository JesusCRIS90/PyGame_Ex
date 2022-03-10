"""
Created on Wed Mar 9 05:34:00 2022

In this file it will build the main clase of the game

@author: jesus
"""

from enum import unique, IntEnum
import pygame
import SettingFile as STF
from typing import overload

""" ENUMS FOR IMAGES """
@unique
class Player_Sprites_Types( IntEnum ):
    IDLE_LEFT     = 0
    IDLE_RIGTH    = 1
    ATTACK_LEFT   = 2
    ATTACK_RIGTH  = 3 
    JUMP_LEFT     = 4
    JUMP_RIFTG    = 5
    RUN_LEFT      = 6
    RUN_RIGTH     = 7    
    SLASH_LEFT    = 8
    SLASH_RIGTH   = 9

@unique
class Levels_Sprites_Types( IntEnum ):
    DIRT_PLATFORM               = 0
    LITTLE_CENTRAL_PLATFORM     = 1
    BIG_CENTRAL_PLATFORM        = 2
    LEFT_PLATFORM               = 3
    RIGTH_PLATFORM              = 4
    GREEN_PORTAL                = 5
    BLUE_PORTAL                 = 6
    RUBY                        = 7
    BACKGROUND_IMAGE            = 8
    
    
    
class ImageRegister():
    
    def __init__( self ):

        # Sprites list for Player
        self.player_move_right_sprites      = None
        self.player_move_left_sprites       = None
        self.player_idle_right_sprites      = None
        self.player_idle_left_sprites       = None
        self.player_jump_right_sprites      = None
        self.player_jump_left_sprites       = None
        self.player_attack_right_sprites    = None
        self.player_attack_left_sprites     = None
        
        # # Sprites list for Enemy
        # self.enemy_move_right_sprites      = None
        # self.enemy_move_left_sprites       = None
        # self.enemy_idle_right_sprites      = None
        # self.enemy_idle_left_sprites       = None
        # self.enemy_jump_right_sprites      = None
        # self.enemy_jump_left_sprites       = None
        # self.enemy_attack_right_sprites    = None
        # self.enemy_attack_left_sprites     = None

        # Sprites to Build Level Scenarie
        self.dirt_platform_sprites              = None
        self.little_central_platform_sprites    = None
        self.big_central_platform_sprites       = None
        self.left_platform_sprites              = None
        self.rigth_platform_sprites             = None
        self.background_image                   = None
        
        
        # Sprite Dictionary
        self.Sprite_Dictionary = {}


        # self._Load_Player_Sprites_()
        # self._Load_Enemy_Sprites_()
        self._Load_Levels_Sprites_()
        
        pass
    
    def _Load_Player_Sprites_( self ):
        
        """ Adding Runing Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (1).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (2).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (3).png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (4).png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (5).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (6).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (7).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (8).png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (9).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/run/Run (10).png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))
            
            
        self.player_move_right_sprites  = { Player_Sprites_Types.RUN_RIGTH: temp_rigth_sprite }
        self.player_move_left_sprites   = { Player_Sprites_Types.RUN_LEFT: temp_left_sprite }

        """ Adding IDLE Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []
 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (1).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (2).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (3).png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (4).png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (5).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (6).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (7).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (8).png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (9).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/idle/Idle (10).png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))
        
        self.player_idle_right_sprites  = { Player_Sprites_Types.IDLE_RIGTH: temp_rigth_sprite }
        self.player_idle_left_sprites   = { Player_Sprites_Types.IDLE_LEFT: temp_left_sprite }

        """ Adding Jumping Sprites to Registers """        
        temp_left_sprite = []; temp_rigth_sprite = []
 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (1).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (2).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (3).png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (4).png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (5).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (6).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (7).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (8).png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (9).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/jump/Jump (10).png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))
        
        self.player_jump_right_sprites  = { Player_Sprites_Types.JUMP_RIFTG: temp_rigth_sprite }
        self.player_jump_left_sprites   = { Player_Sprites_Types.JUMP_LEFT: temp_left_sprite }


        """ Adding Attacking Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []
 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (1).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (2).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (3).png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (4).png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (5).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (6).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (7).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (8).png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (9).png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Asset/images/player/attack/Attack (10).png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))
        
        self.player_attack_right_sprites  = { Player_Sprites_Types.ATTACK_RIGTH: temp_rigth_sprite }
        self.player_attack_left_sprites   = { Player_Sprites_Types.ATTACK_LEFT: temp_left_sprite }
        
        pass
    
    def _Load_Enemy_Sprites_( self ):
        pass
    
    def _Load_Levels_Sprites_( self ):
        
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.DIRT_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (1).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.LITTLE_CENTRAL_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (4).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.BIG_CENTRAL_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (2).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.LEFT_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (3).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.RIGTH_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (5).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.BACKGROUND_IMAGE: pygame.transform.scale(pygame.image.load("Assets/images/background.png"), (STF.WINDOW_WIDTH, STF.WINDOW_HEIGHT) ) } )
        
        pass
    
    def add2Register( self ):
        pass
    
    @overload
    def GetSprite( self, enum_sprite:Levels_Sprites_Types ):
        # return self.Sprite_Dictionary[ enum_sprite ]
        pass

    @overload
    def GetSprite( self, enum_sprite:Player_Sprites_Types ):
        # return self.Sprite_Dictionary[ enum_sprite ]
        pass
    
    def GetSprite( self, enum_sprite ):
        return self.Sprite_Dictionary[ enum_sprite ]
    