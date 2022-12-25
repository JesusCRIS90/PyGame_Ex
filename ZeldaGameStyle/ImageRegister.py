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
from support import import_folder
from support import CustomSingleton
from random import randint

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
    PLAYER_TEST             = 100
    
    PLAYER_DOWN_ATTACK      = 101
    PLAYER_UP_ATTACK        = 102
    PLAYER_LEFT_ATTACK      = 103
    PLAYER_RIGHT_ATTACK     = 104
    
    PLAYER_DOWN_MOVE        = 105
    PLAYER_UP_MOVE          = 106
    PLAYER_LEFT_MOVE        = 107
    PLAYER_RIGHT_MOVE       = 108
    
    PLAYER_DOWN_IDLE        = 109
    PLAYER_UP_IDLE          = 110
    PLAYER_LEFT_IDLE        = 111
    PLAYER_RIGHT_IDLE       = 112
    
@unique
class Weapons_Types( IntEnum ):
    AXE_FULL              = 200
    AXE_DOWN              = 201
    AXE_UP                = 202
    AXE_RIGHT             = 203
    AXE_LEFT              = 204
    
    LANCE_FULL            = 210
    LANCE_DOWN            = 211
    LANCE_UP              = 212
    LANCE_RIGHT           = 213
    LANCE_LEFT            = 214

    RAPIER_FULL           = 220
    RAPIER_DOWN           = 221
    RAPIER_UP             = 222
    RAPIER_RIGHT          = 223
    RAPIER_LEFT           = 224

    SAI_FULL              = 230
    SAI_DOWN              = 231
    SAI_UP                = 232
    SAI_RIGHT             = 233
    SAI_LEFT              = 234

    SWORD_FULL            = 240
    SWORD_DOWN            = 241
    SWORD_UP              = 242
    SWORD_RIGHT           = 243
    SWORD_LEFT            = 244
    
    AXE                   = 250
    LANCE                 = 251
    RAPIER                = 252
    SAI                   = 253
    SWORD                 = 254

@unique
class Magic_Types( IntEnum ):
    FLAME       = 300
    HEAL        = 301

@unique
class Enemy_Types( IntEnum ):
    BAMBOO      = 400
    RACCOON     = 401
    SPIRIT      = 402
    SQUID       = 403

@unique
class Enemy_Sprites( IntEnum ):

    BAMBOO_ATTACK   = 410
    BAMBOO_MOVE     = 411
    BAMBOO_IDLE     = 412

    RACCOON_ATTACK  = 413
    RACCOON_MOVE    = 414
    RACCOON_IDLE    = 415

    SPIRIT_ATTACK   = 416
    SPIRIT_MOVE     = 417
    SPIRIT_IDLE     = 418

    SQUID_ATTACK    = 419
    SQUID_MOVE      = 420
    SQUID_IDLE      = 421

@unique
class Particle_Sprites( IntEnum ):
    LEAF_BREAK      = 500
    
    CLAW            = 501
    SLASH           = 502
    SPARKLE         = 503
    THUNDER         = 504
    LEAF_ATTACK     = 505

    SQUID_DEATH     = 506
    RACOON_DEATH    = 507
    SPIRIT_DEATH    = 508
    BAMBOO_DEATH    = 509

    AURA_SPELL      = 510
    HEAL_SPELL      = 511
    FLAME_SPELL     = 512


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

Enemy_Dict = {
    "squid"     : Enemy_Types.SQUID,
    "raccoon"   : Enemy_Types.RACCOON,
    "spirit"    : Enemy_Types.SPIRIT,
    "bamboo"    : Enemy_Types.BAMBOO
}

Particles_EnemiesAttack_Dict = {
    "slash"         : Particle_Sprites.SLASH,
    "claw"          : Particle_Sprites.CLAW,
    "thunder"       : Particle_Sprites.THUNDER,
    "leaf_attack"   : Particle_Sprites.LEAF_ATTACK
}

@CustomSingleton
class ImageRegister( ):
    
    def __init__( self ):        
        
        # Sprite Dictionary
        self.Sprite_Dictionary = {}

        self._Load_Levels_Sprites_()
        self._Load_Player_Sprites_()
        self._Load_Weapons_Sprites_()
        self._Load_Magic_Sprites_()
        self._Load_Enemies_Sprites_()
        self._Load_ParticleEffects_Sprites_()

                
    def _Load_Player_Sprites_( self ):
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_TEST: pygame.image.load("Assets/Player/player.png").convert_alpha() } )
        
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_DOWN_ATTACK: import_folder( "Assets/Player/down_attack/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_UP_ATTACK: import_folder( "Assets/Player/up_attack/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_LEFT_ATTACK: import_folder( "Assets/Player/left_attack/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_RIGHT_ATTACK: import_folder( "Assets/Player/right_attack/" ) } )

        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_DOWN_MOVE: import_folder( "Assets/Player/down_move/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_UP_MOVE: import_folder( "Assets/Player/up_move/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_LEFT_MOVE: import_folder( "Assets/Player/left_move/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_RIGHT_MOVE: import_folder( "Assets/Player/right_move/" ) } )

        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_DOWN_IDLE: import_folder( "Assets/Player/down_idle/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_UP_IDLE: import_folder( "Assets/Player/up_idle/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_LEFT_IDLE: import_folder( "Assets/Player/left_idle/" ) } )
        self.Sprite_Dictionary.update( { Player_Sprites_Types.PLAYER_RIGHT_IDLE: import_folder( "Assets/Player/right_idle/" ) } )
  
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
    
    def _Load_Weapons_Sprites_( self ):
        
        self.Sprite_Dictionary.update( { Weapons_Types.AXE_DOWN:    pygame.image.load("Assets/Weapons/axe/down.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.AXE_UP:      pygame.image.load("Assets/Weapons/axe/up.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.AXE_LEFT:    pygame.image.load("Assets/Weapons/axe/left.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.AXE_RIGHT:   pygame.image.load("Assets/Weapons/axe/right.png").convert_alpha() } )    
        self.Sprite_Dictionary.update( { Weapons_Types.AXE_FULL:    pygame.image.load("Assets/Weapons/axe/full.png").convert_alpha() } )

        self.Sprite_Dictionary.update( { Weapons_Types.LANCE_DOWN:    pygame.image.load("Assets/Weapons/lance/down.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.LANCE_UP:      pygame.image.load("Assets/Weapons/lance/up.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.LANCE_LEFT:    pygame.image.load("Assets/Weapons/lance/left.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.LANCE_RIGHT:   pygame.image.load("Assets/Weapons/lance/right.png").convert_alpha() } )    
        self.Sprite_Dictionary.update( { Weapons_Types.LANCE_FULL:    pygame.image.load("Assets/Weapons/lance/full.png").convert_alpha() } )
    
        self.Sprite_Dictionary.update( { Weapons_Types.RAPIER_DOWN:    pygame.image.load("Assets/Weapons/rapier/down.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.RAPIER_UP:      pygame.image.load("Assets/Weapons/rapier/up.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.RAPIER_LEFT:    pygame.image.load("Assets/Weapons/rapier/left.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.RAPIER_RIGHT:   pygame.image.load("Assets/Weapons/rapier/right.png").convert_alpha() } )    
        self.Sprite_Dictionary.update( { Weapons_Types.RAPIER_FULL:    pygame.image.load("Assets/Weapons/rapier/full.png").convert_alpha() } )

        self.Sprite_Dictionary.update( { Weapons_Types.SAI_DOWN:    pygame.image.load("Assets/Weapons/sai/down.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.SAI_UP:      pygame.image.load("Assets/Weapons/sai/up.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.SAI_LEFT:    pygame.image.load("Assets/Weapons/sai/left.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.SAI_RIGHT:   pygame.image.load("Assets/Weapons/sai/right.png").convert_alpha() } )    
        self.Sprite_Dictionary.update( { Weapons_Types.SAI_FULL:    pygame.image.load("Assets/Weapons/sai/full.png").convert_alpha() } )

        self.Sprite_Dictionary.update( { Weapons_Types.SWORD_DOWN:    pygame.image.load("Assets/Weapons/sword/down.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.SWORD_UP:      pygame.image.load("Assets/Weapons/sword/up.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.SWORD_LEFT:    pygame.image.load("Assets/Weapons/sword/left.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Weapons_Types.SWORD_RIGHT:   pygame.image.load("Assets/Weapons/sword/right.png").convert_alpha() } )    
        self.Sprite_Dictionary.update( { Weapons_Types.SWORD_FULL:    pygame.image.load("Assets/Weapons/sword/full.png").convert_alpha() } )

    def _Load_Magic_Sprites_( self ):
        self.Sprite_Dictionary.update( { Magic_Types.FLAME:   pygame.image.load("Assets/Particles/flame/fire.png").convert_alpha() } )
        self.Sprite_Dictionary.update( { Magic_Types.HEAL:    pygame.image.load("Assets/Particles/heal/heal.png").convert_alpha() } )

    def _Load_Enemies_Sprites_( self ):
        self.Sprite_Dictionary.update( { Enemy_Sprites.BAMBOO_ATTACK:   import_folder( "Assets/Monsters/bamboo/attack" ) } )
        
        self.Sprite_Dictionary.update( { Enemy_Sprites.BAMBOO_MOVE:     import_folder( "Assets/Monsters/bamboo/move" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.BAMBOO_IDLE:     import_folder( "Assets/Monsters/bamboo/idle" ) } )

        self.Sprite_Dictionary.update( { Enemy_Sprites.RACCOON_ATTACK:   import_folder( "Assets/Monsters/raccoon/attack" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.RACCOON_MOVE:     import_folder( "Assets/Monsters/raccoon/move" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.RACCOON_IDLE:     import_folder( "Assets/Monsters/raccoon/idle" ) } )

        self.Sprite_Dictionary.update( { Enemy_Sprites.SPIRIT_ATTACK:   import_folder( "Assets/Monsters/spirit/attack" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.SPIRIT_MOVE:     import_folder( "Assets/Monsters/spirit/move" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.SPIRIT_IDLE:     import_folder( "Assets/Monsters/spirit/idle" ) } )

        self.Sprite_Dictionary.update( { Enemy_Sprites.SQUID_ATTACK:   import_folder( "Assets/Monsters/squid/attack" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.SQUID_MOVE:     import_folder( "Assets/Monsters/squid/move" ) } )
        self.Sprite_Dictionary.update( { Enemy_Sprites.SQUID_IDLE:     import_folder( "Assets/Monsters/squid/idle" ) } )
    
    def _Load_ParticleEffects_Sprites_( self ):
        
        # Loading Leaf Breaking Particles
        self.Sprite_Dictionary.update( { Particle_Sprites.LEAF_BREAK: [ 
            import_folder( "Assets/Particles/breakingGrass/leaf1" ),
            import_folder( "Assets/Particles/breakingGrass/leaf2" ),
            import_folder( "Assets/Particles/breakingGrass/leaf3" ),
            import_folder( "Assets/Particles/breakingGrass/leaf4" ),
            import_folder( "Assets/Particles/breakingGrass/leaf5" ),
            import_folder( "Assets/Particles/breakingGrass/leaf6" ),
            reflect_images( import_folder( "Assets/Particles/breakingGrass/leaf1" ) ),
            reflect_images( import_folder( "Assets/Particles/breakingGrass/leaf2" ) ),
            reflect_images( import_folder( "Assets/Particles/breakingGrass/leaf3" ) ),
            reflect_images( import_folder( "Assets/Particles/breakingGrass/leaf4" ) ),
            reflect_images( import_folder( "Assets/Particles/breakingGrass/leaf5" ) ),
            reflect_images( import_folder( "Assets/Particles/breakingGrass/leaf6" ) ) ] 
            } )

        # Loading Enemies Attacking Particles
        self.Sprite_Dictionary.update( { Particle_Sprites.CLAW:         import_folder( "Assets/Particles/enemiesAttack/claw" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.LEAF_ATTACK:  import_folder( "Assets/Particles/enemiesAttack/leaf_attack" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.SLASH:        import_folder( "Assets/Particles/enemiesAttack/slash" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.THUNDER:      import_folder( "Assets/Particles/enemiesAttack/thunder" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.SLASH:        import_folder( "Assets/Particles/enemiesAttack/sparkle" ) } )

        # Loading Enemies Death Particles
        self.Sprite_Dictionary.update( { Particle_Sprites.BAMBOO_DEATH:  import_folder( "Assets/Particles/enemiesDeath/bamboo" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.SPIRIT_DEATH:  import_folder( "Assets/Particles/enemiesDeath/nova" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.RACOON_DEATH:  import_folder( "Assets/Particles/enemiesDeath/raccoon" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.SQUID_DEATH:   import_folder( "Assets/Particles/enemiesDeath/smoke_orange" ) } )

        # Loading Spells Particles
        self.Sprite_Dictionary.update( { Particle_Sprites.AURA_SPELL:  import_folder( "Assets/Particles/aura" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.HEAL_SPELL:  import_folder( "Assets/Particles/heal/frames" ) } )
        self.Sprite_Dictionary.update( { Particle_Sprites.FLAME_SPELL:  import_folder( "Assets/Particles/flame/frames" ) } )

        
    @overload
    def GetSprite( self, enum_sprite:Levels_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]

    @overload
    def GetSprite( self, enum_sprite:Player_Sprites_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    @overload
    def GetSprite( self, enum_sprite:Weapons_Types ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    @overload
    def GetSprite( self, enum_sprite:Enemy_Sprites ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    @overload
    def GetSprite( self, enum_sprite:Particle_Sprites ):
        return self.Sprite_Dictionary[ enum_sprite ]
    
    def GetSprite( self, enum_sprite ):
        return self.Sprite_Dictionary[ enum_sprite ]


def reflect_images( frames ):    
    return [ pygame.transform.flip( frame, True, False ) for frame in frames ]



