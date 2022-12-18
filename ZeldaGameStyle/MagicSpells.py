import pygame
from SettingFile import *
from InGame_Parameters import PlayerStats
from ImageRegister import *
from ParticleEffects import ParticleEffect

class MagicSpells:
    
    def __init__(self) -> None:
        pass

    def heal( self, groups, position, spell_stats ):
        offset = ( 0, 25 )
        new_pos = ( position[ 0 ] + offset[ 0 ], position[ 1 ] - offset[ 1 ] )
        if PlayerStats().Get_Energy() >= spell_stats["cost"]:
            
            #  Upadating Stats
            player_health = PlayerStats().Get_Health()
            player_health += spell_stats["strength"]
            PlayerStats().Set_Health( player_health )
            self._reduceEnergy_( spell_stats["cost"] )
            
            # Creating Particles Animations
            ParticleEffect( groups, position, Particle_Sprites.AURA_SPELL )
            ParticleEffect( groups, new_pos, Particle_Sprites.HEAL_SPELL )

    def flame( self ):
        pass

    def _reduceEnergy_( self, cost ):
        energy = PlayerStats().Get_Energy()
        energy -= cost
        PlayerStats().Set_Energy( energy )