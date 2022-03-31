"""
Created on Wed Mar 9 05:34:00 2022

In this file it will build the main clase of the game

@author: jesus
"""

from enum import unique, IntEnum
import pygame
import SettingFile as STF
from typing import overload
import copy

""" ENUMS FOR IMAGES """
""""
    Be careful!!!. IntEnum's must not be repit because the dictionary's keys must be uniques
"""
@unique
class Player_Sprites_Types( IntEnum ):
    IDLE_LEFT     = 9
    IDLE_RIGTH    = 10
    ATTACK_LEFT   = 11
    ATTACK_RIGTH  = 12 
    JUMP_LEFT     = 13
    JUMP_RIGHT    = 14
    RUN_LEFT      = 15
    RUN_RIGTH     = 16    
    SLASH_LEFT    = 17
    SLASH_RIGTH   = 18

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
        self.player_move_right_sprites      = []
        self.player_move_left_sprites       = []
        self.player_idle_right_sprites      = []
        self.player_idle_left_sprites       = []
        self.player_jump_right_sprites      = []
        self.player_jump_left_sprites       = []
        self.player_attack_right_sprites    = []
        self.player_attack_left_sprites     = []
        
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


        self._Load_Player_Sprites_()
        # self._Load_Enemy_Sprites_()
        self._Load_Levels_Sprites_()
                
    
    def _Load_Player_Sprites_( self ):
        
        
        """ Adding Runing Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run1.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run2.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run3.png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run4.png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run5.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run6.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run7.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run8.png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run9.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run10.png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))
        
        self.Sprite_Dictionary[ Player_Sprites_Types.RUN_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Player_Sprites_Types.RUN_LEFT ]  = temp_left_sprite


        """ Adding IDLE Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []
 

        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle1.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle2.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle3.png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle4.png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle5.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle6.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle7.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle8.png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle9.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/idle/Idle10.png"), (64,64) ) ) 

        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))


        self.Sprite_Dictionary[ Player_Sprites_Types.IDLE_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Player_Sprites_Types.IDLE_LEFT ]  = temp_left_sprite


        """ Adding Jumping Sprites to Registers """        
        temp_left_sprite = []; temp_rigth_sprite = []
 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump1.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump2.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump3.png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump4.png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump5.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump6.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump7.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump8.png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump9.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump10.png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))


        self.Sprite_Dictionary[ Player_Sprites_Types.JUMP_RIGHT ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Player_Sprites_Types.JUMP_LEFT ]  = temp_left_sprite


        """ Adding Attacking Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []
 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack1.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack2.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack3.png"), (64,64) ) )    
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack4.png"), (64,64) ) )        
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack5.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack6.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack7.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack8.png"), (64,64) ) ) 
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack9.png"), (64,64) ) )
        temp_left_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack10.png"), (64,64) ) ) 
        
        for sprite in temp_left_sprite:
            temp_rigth_sprite.append(pygame.transform.flip(sprite, True, False))


        self.Sprite_Dictionary[ Player_Sprites_Types.ATTACK_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Player_Sprites_Types.ATTACK_LEFT ]  = temp_left_sprite

    
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
        return self.Sprite_Dictionary[ enum_sprite ]
        # pass

    @overload
    def GetSprite( self, enum_sprite:Player_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
        # pass
    
    def GetSprite( self, enum_sprite ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
        

