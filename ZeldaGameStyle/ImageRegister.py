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
    ROCK_TEST                    = 0
    BACKGROUND_IMAGE             = 1

@unique
class Player_Sprites_Types( IntEnum ):
    PLAYER_TEST   = 2


def CustomSingleton( cls ):

    instances= dict()

    def wrap( *args, **kwargs ):
        if cls not in instances:
            instances[ cls ] = cls( *args, **kwargs )

        return instances[ cls ]

    return wrap

@CustomSingleton
class ImageRegister( ):
    
    def __init__( self ):        
        
        # Sprite Dictionary
        self.Sprite_Dictionary = {}

        self._Load_Levels_Sprites_()
        self._Load_Player_Sprites_()


                
    def _Load_Player_Sprites_( self ):
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_TEST: pygame.image.load("Assets/player.png").convert_alpha() } )
  
    def _Load_Levels_Sprites_( self ):
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.ROCK_TEST: pygame.image.load("Assets/rock.png").convert_alpha() } )

        

    @overload
    def GetSprite( self, enum_sprite:Levels_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]

    @overload
    def GetSprite( self, enum_sprite:Player_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    def GetSprite( self, enum_sprite ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
        

