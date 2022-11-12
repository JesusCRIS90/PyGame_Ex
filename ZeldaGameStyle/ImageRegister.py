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
    BACKGROUND_IMAGE                = 0
    ROCK_TEST                       = 1
    NONE_SPRITE                     = 2
    GRASS_1                         = 3
    GRASS_2                         = 4
    GRASS_3                         = 5
    OBJECT_1                        = 6
    OBJECT_2                        = 7
    OBJECT_3                        = 8
    OBJECT_4                        = 9
    OBJECT_5                        = 10
    OBJECT_6                        = 11
    OBJECT_7                        = 12
    OBJECT_8                        = 13
    OBJECT_9                        = 14
    OBJECT_10                       = 15
    OBJECT_11                       = 16
    OBJECT_12                       = 17
    OBJECT_13                       = 18
    OBJECT_14                       = 19
    OBJECT_15                       = 20
    OBJECT_16                       = 21
    OBJECT_17                       = 22
    OBJECT_18                       = 23
    OBJECT_19                       = 24
    OBJECT_20                       = 25
    OBJECT_21                       = 26


@unique
class Player_Sprites_Types( IntEnum ):
    PLAYER_TEST   = 100


Grass_Dict = {
    8   : Levels_Sprites_Types.GRASS_1,
    9   : Levels_Sprites_Types.GRASS_2,
    10  : Levels_Sprites_Types.GRASS_3,
}

Object_Dict = {
    0   : Levels_Sprites_Types.OBJECT_1,
    1   : Levels_Sprites_Types.OBJECT_2,
    2   : Levels_Sprites_Types.OBJECT_3,
    3   : Levels_Sprites_Types.OBJECT_4,
    4   : Levels_Sprites_Types.OBJECT_5,
    5   : Levels_Sprites_Types.OBJECT_6,
    6   : Levels_Sprites_Types.OBJECT_7,
    7   : Levels_Sprites_Types.OBJECT_8,
    8   : Levels_Sprites_Types.OBJECT_9,
    9   : Levels_Sprites_Types.OBJECT_10,
    10  : Levels_Sprites_Types.OBJECT_11,
    11  : Levels_Sprites_Types.OBJECT_12,
    12  : Levels_Sprites_Types.OBJECT_13,
    13  : Levels_Sprites_Types.OBJECT_14,
    14  : Levels_Sprites_Types.OBJECT_15,
    15  : Levels_Sprites_Types.OBJECT_16,
    16  : Levels_Sprites_Types.OBJECT_17,
    17  : Levels_Sprites_Types.OBJECT_18,
    18  : Levels_Sprites_Types.OBJECT_19,
    19  : Levels_Sprites_Types.OBJECT_20,
    20  : Levels_Sprites_Types.OBJECT_21,
}


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
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_TEST: pygame.image.load("Assets/Player/player.png").convert_alpha() } )
  
    def _Load_Levels_Sprites_( self ):
        #self.Sprite_Dictionary.update( { Levels_Sprites_Types.ROCK_TEST: pygame.image.load("Assets/rock.png").convert_alpha() } )
        
        # Load Background
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.BACKGROUND_IMAGE: pygame.image.load("Assets/WorldMap/ground.png").convert() } )
        
        """" LOAD GRASS OBJECTS """
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.GRASS_1: pygame.image.load("Assets/WorldMap/Grass/grass_1.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.GRASS_2: pygame.image.load("Assets/WorldMap/Grass/grass_2.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.GRASS_3: pygame.image.load("Assets/WorldMap/Grass/grass_3.png").convert_alpha() } )

        """" LOAD OBJECTS """
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_1: pygame.image.load("Assets/WorldMap/Objects/00.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_2: pygame.image.load("Assets/WorldMap/Objects/01.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_3: pygame.image.load("Assets/WorldMap/Objects/02.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_4: pygame.image.load("Assets/WorldMap/Objects/03.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_5: pygame.image.load("Assets/WorldMap/Objects/04.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_6: pygame.image.load("Assets/WorldMap/Objects/05.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_7: pygame.image.load("Assets/WorldMap/Objects/06.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_8: pygame.image.load("Assets/WorldMap/Objects/07.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_9: pygame.image.load("Assets/WorldMap/Objects/08.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_10: pygame.image.load("Assets/WorldMap/Objects/09.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_11: pygame.image.load("Assets/WorldMap/Objects/10.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_12: pygame.image.load("Assets/WorldMap/Objects/11.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_13: pygame.image.load("Assets/WorldMap/Objects/12.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_14: pygame.image.load("Assets/WorldMap/Objects/13.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_15: pygame.image.load("Assets/WorldMap/Objects/14.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_16: pygame.image.load("Assets/WorldMap/Objects/15.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_17: pygame.image.load("Assets/WorldMap/Objects/16.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_18: pygame.image.load("Assets/WorldMap/Objects/17.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_19: pygame.image.load("Assets/WorldMap/Objects/18.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_20: pygame.image.load("Assets/WorldMap/Objects/19.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Levels_Sprites_Types.OBJECT_21: pygame.image.load("Assets/WorldMap/Objects/20.png").convert_alpha() } )
        

    @overload
    def GetSprite( self, enum_sprite:Levels_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]

    @overload
    def GetSprite( self, enum_sprite:Player_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    def GetSprite( self, enum_sprite ):
        return self.Sprite_Dictionary[ enum_sprite ]


    

