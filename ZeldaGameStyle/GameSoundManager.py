import pygame
from enum import unique, IntEnum
from support import CustomSingleton



@unique
class SoundEffects_Types( IntEnum ):
    PLAYER_ATTACK            = 600
    PLAYER_HEAL_SPELL        = 601
    PLAYER_FLAME_SPELL       = 602
    DEATH                    = 603
    ENEMY_HIT                = 604

    SLASH                    = 605
    FIREBALL                 = 606
    CLAW                     = 607

    MAIN_SOUND               = 666





@CustomSingleton
class GameSoundManager:

    def __init__(self) -> None:
        
        
        # Sounds Dictionary
        self.Sound_Dictionary = {}

        self._Load_SoundEffects_()
        self._Load_Tracks_()

    def _Load_SoundEffects_( self ):
        
        self.Sound_Dictionary.update( { SoundEffects_Types.PLAYER_ATTACK: pygame.mixer.Sound( 'Assets/audio/sword.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.PLAYER_ATTACK ].set_volume( 0.4 )

        self.Sound_Dictionary.update( { SoundEffects_Types.PLAYER_FLAME_SPELL: pygame.mixer.Sound( 'Assets/audio/Fire.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.PLAYER_FLAME_SPELL ].set_volume( 0.4 )

        self.Sound_Dictionary.update( { SoundEffects_Types.PLAYER_HEAL_SPELL: pygame.mixer.Sound( 'Assets/audio/heal.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.PLAYER_HEAL_SPELL ].set_volume( 0.6 )

        self.Sound_Dictionary.update( { SoundEffects_Types.DEATH: pygame.mixer.Sound( 'Assets/audio/death.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.DEATH ].set_volume( 0.4 )
    
        self.Sound_Dictionary.update( { SoundEffects_Types.ENEMY_HIT: pygame.mixer.Sound( 'Assets/audio/hit.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.ENEMY_HIT ].set_volume( 0.4 )

        self.Sound_Dictionary.update( { SoundEffects_Types.SLASH: pygame.mixer.Sound( 'Assets/audio/attack/slash.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.SLASH ].set_volume( 0.3 )

        self.Sound_Dictionary.update( { SoundEffects_Types.FIREBALL: pygame.mixer.Sound( 'Assets/audio/attack/fireball.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.FIREBALL ].set_volume( 0.3 )

        self.Sound_Dictionary.update( { SoundEffects_Types.CLAW: pygame.mixer.Sound( 'Assets/audio/attack/claw.wav' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.CLAW ].set_volume( 0.3 )


    def _Load_Tracks_( self ):
        self.Sound_Dictionary.update( { SoundEffects_Types.MAIN_SOUND: pygame.mixer.Sound( 'Assets/audio/main.ogg' ) } )
        self.Sound_Dictionary[ SoundEffects_Types.MAIN_SOUND ].set_volume( 0.5 )
    
    def GetSound( self, sound_type:SoundEffects_Types ):
        return self.Sound_Dictionary[ sound_type ]

