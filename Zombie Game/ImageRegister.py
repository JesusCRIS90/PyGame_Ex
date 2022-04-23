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
class Levels_Sprites_Types( IntEnum ):
    DIRT_PLATFORM               = 0
    LITTLE_CENTRAL_PLATFORM     = 1
    BIG_CENTRAL_PLATFORM        = 2
    LEFT_PLATFORM               = 3
    RIGTH_PLATFORM              = 4
    GREEN_PORTAL                = 5
    PURPLE_PORTAL               = 6
    RUBY                        = 7
    BACKGROUND_IMAGE            = 8

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
class Bullet_Player_Sprites_Types( IntEnum ):
    BULLET_LEFT     = 19
    BULLET_RIGTH    = 20
    
@unique
class Enemy_Sprites_Types( IntEnum ):
    FEMALE_ZOMBIE_WALK_RIGTH        = 21
    FEMALE_ZOMBIE_WALK_LEFT         = 22
    FEMALE_ZOMBIE_DIE_RIGTH         = 23
    FEMALE_ZOMBIE_DIE_LEFT          = 24
    FEMALE_ZOMBIE_RISE_RIGTH        = 25
    FEMALE_ZOMBIE_RISE_LEFT         = 26
    MALE_ZOMBIE_WALK_RIGTH          = 27
    MALE_ZOMBIE_WALK_LEFT           = 28
    MALE_ZOMBIE_DIE_RIGTH           = 29
    MALE_ZOMBIE_DIE_LEFT            = 30
    MALE_ZOMBIE_RISE_RIGTH          = 31
    MALE_ZOMBIE_RISE_LEFT           = 32
    
class ImageRegister():
    
    def __init__( self ):        
        
        # Sprite Dictionary
        self.Sprite_Dictionary = {}


        self._Load_Levels_Sprites_()
        self._Load_Portals_Sprites_()
        self._Load_Player_Sprites_()
        self._Load_Bullet_Sprites_()
        self._Load_Enemy_Sprites_()
        self._Load_Rubies_Sprites()

                
    def _Load_Player_Sprites_( self ):
        
        """ Adding Runing Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run1.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run2.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run3.png"), (64,64) ) )    
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run4.png"), (64,64) ) )        
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run5.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run6.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run7.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run8.png"), (64,64) ) ) 
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run9.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/run/Run10.png"), (64,64) ) ) 
        
        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
        
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
 
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump1.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump2.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump3.png"), (64,64) ) )    
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump4.png"), (64,64) ) )        
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump5.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump6.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump7.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump8.png"), (64,64) ) ) 
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump9.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/jump/Jump10.png"), (64,64) ) ) 
        
        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))


        self.Sprite_Dictionary[ Player_Sprites_Types.JUMP_RIGHT ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Player_Sprites_Types.JUMP_LEFT ]  = temp_left_sprite


        """ Adding Attacking Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []
 
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack1.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack2.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack3.png"), (64,64) ) )    
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack4.png"), (64,64) ) )        
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack5.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack6.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack7.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack8.png"), (64,64) ) ) 
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack9.png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/player/attack/Attack10.png"), (64,64) ) ) 
        
        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))


        self.Sprite_Dictionary[ Player_Sprites_Types.ATTACK_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Player_Sprites_Types.ATTACK_LEFT ]  = temp_left_sprite

    def _Load_Bullet_Sprites_( self ):
        self.Sprite_Dictionary.update( { Bullet_Player_Sprites_Types.BULLET_LEFT: pygame.transform.scale(pygame.image.load("Assets/images/player/slash.png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Bullet_Player_Sprites_Types.BULLET_RIGTH: pygame.transform.scale(pygame.transform.flip(pygame.image.load("Assets/images/player/slash.png"), True, False), (32,32)) } )

    def _Load_Enemy_Sprites_( self ):
        
        """ Adding boy Walking Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (1).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (2).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (4).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (5).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (6).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (7).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (8).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (9).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/walk/Walk (10).png"), (64,64) ) )

        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
      
        self.Sprite_Dictionary[ Enemy_Sprites_Types.MALE_ZOMBIE_WALK_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Enemy_Sprites_Types.MALE_ZOMBIE_WALK_LEFT ]  = temp_left_sprite


        """ Adding boy Diying Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (1).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (2).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (4).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (5).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (6).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (7).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (8).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (9).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (10).png"), (64,64) ) )

        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
      
        self.Sprite_Dictionary[ Enemy_Sprites_Types.MALE_ZOMBIE_DIE_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Enemy_Sprites_Types.MALE_ZOMBIE_DIE_LEFT ]  = temp_left_sprite


        """ Adding boy Rising Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (10).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (9).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (7).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (6).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (5).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (4).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (2).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/boy/dead/Dead (1).png"), (64,64) ) )

        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
      
        self.Sprite_Dictionary[ Enemy_Sprites_Types.MALE_ZOMBIE_RISE_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Enemy_Sprites_Types.MALE_ZOMBIE_RISE_LEFT ]  = temp_left_sprite


        """ Adding girl Walking Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (1).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (2).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (4).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (5).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (6).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (7).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (8).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (9).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/walk/Walk (10).png"), (64,64) ) )

        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
      
        self.Sprite_Dictionary[ Enemy_Sprites_Types.FEMALE_ZOMBIE_WALK_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Enemy_Sprites_Types.FEMALE_ZOMBIE_WALK_LEFT ]  = temp_left_sprite


        """ Adding girl Diying Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (1).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (2).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (4).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (5).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (6).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (7).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (8).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (9).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (10).png"), (64,64) ) )

        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
      
        self.Sprite_Dictionary[ Enemy_Sprites_Types.FEMALE_ZOMBIE_DIE_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Enemy_Sprites_Types.FEMALE_ZOMBIE_DIE_LEFT ]  = temp_left_sprite


        """ Adding girl Rising Sprites to Registers """
        temp_left_sprite = []; temp_rigth_sprite = []         

        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (10).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (9).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (7).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (6).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (5).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (4).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (3).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (2).png"), (64,64) ) )
        temp_rigth_sprite.append( pygame.transform.scale( pygame.image.load("Assets/images/zombie/girl/dead/Dead (1).png"), (64,64) ) )

        for sprite in temp_rigth_sprite:
            temp_left_sprite.append(pygame.transform.flip(sprite, True, False))
      
        self.Sprite_Dictionary[ Enemy_Sprites_Types.FEMALE_ZOMBIE_RISE_RIGTH ] = temp_rigth_sprite
        self.Sprite_Dictionary[ Enemy_Sprites_Types.FEMALE_ZOMBIE_RISE_LEFT ]  = temp_left_sprite
    
    def _Load_Portals_Sprites_( self ):
        """ Adding Purple Portals to Registers """
        temp_list = []
        
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile000.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile001.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile002.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile003.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile004.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile005.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile006.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile007.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile008.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile009.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile010.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile011.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile012.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile013.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile014.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile015.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile016.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile017.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile018.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile019.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile020.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/purple/tile021.png"), (80,80) ) )
        
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.PURPLE_PORTAL: temp_list } )
        
        """ Adding Green Portals to Registers """
        temp_list = []

        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile000.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile001.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile002.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile003.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile004.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile005.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile006.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile007.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile008.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile009.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile010.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile011.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile012.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile013.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile014.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile015.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile016.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile017.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile018.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile019.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile020.png"), (80,80) ) )
        temp_list.append( pygame.transform.scale( pygame.image.load("Assets/images/portals/green/tile021.png"), (80,80) ) )

        self.Sprite_Dictionary.update( { Levels_Sprites_Types.GREEN_PORTAL: temp_list } )
  
    def _Load_Levels_Sprites_( self ):
        
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.DIRT_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (1).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.LITTLE_CENTRAL_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (4).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.BIG_CENTRAL_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (2).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.LEFT_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (3).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.RIGTH_PLATFORM: pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tile (5).png"), (32,32)) } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.BACKGROUND_IMAGE: pygame.transform.scale(pygame.image.load("Assets/images/background.png"), (STF.WINDOW_WIDTH, STF.WINDOW_HEIGHT) ) } )
        
    def _Load_Rubies_Sprites( self ):

        """"  Load the Rubies Sprites """
        temp_list = []
        
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile000.png"), (40,40)))
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile001.png"), (40,40)))
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile002.png"), (40,40)))
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile003.png"), (40,40)))
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile004.png"), (40,40)))
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile005.png"), (40,40)))
        temp_list.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile006.png"), (40,40)))

        self.Sprite_Dictionary.update( { Levels_Sprites_Types.RUBY: temp_list } )
    
    @overload
    def GetSprite( self, enum_sprite:Levels_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]

    @overload
    def GetSprite( self, enum_sprite:Player_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]

    @overload
    def GetSprite( self, enum_sprite:Bullet_Player_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    @overload
    def GetSprite( self, enum_sprite:Enemy_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    def GetSprite( self, enum_sprite ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
        

