import pygame
from SettingFile import *
from InGame_Parameters import PlayerStats
from ImageRegister import *
from ParticleEffects import ParticleEffect
from Animations import Player_See_Directions
from random import randint


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

    def flame( self, groups, position, spell_stats ):

        if PlayerStats().Get_Energy() >= spell_stats["cost"]:
            direction = self._BuildVectorDirection_( PlayerStats().GetPlayerSeeDirection() )
            x_pos = position[ 0 ]; y_pos = position[ 1 ]

            for idx in range( 1,4 ):
                if direction.x: # Horizontal
                    offset_x = ( direction.x * idx ) * STF.TILESIZE
                    x_pos = position[ 0 ] + offset_x + randint( -( STF.TILESIZE // 4 ), ( STF.TILESIZE // 4 ) )
                    y_pos = position[ 1 ] + randint( -( STF.TILESIZE // 4 ), ( STF.TILESIZE // 4 ) )
                else:       # Vertical
                    offset_y = ( direction.y * idx ) * STF.TILESIZE
                    x_pos = position[ 0 ] + randint( -( STF.TILESIZE // 4 ), ( STF.TILESIZE // 4 ) )
                    y_pos = position[ 1 ] + offset_y + randint( -( STF.TILESIZE // 4 ), ( STF.TILESIZE // 4 ) )

                ParticleEffect( groups, ( x_pos, y_pos ), Particle_Sprites.FLAME_SPELL )

            self._reduceEnergy_( spell_stats["cost"] )

    def _reduceEnergy_( self, cost ):
        energy = PlayerStats().Get_Energy()
        energy -= cost
        PlayerStats().Set_Energy( energy )
    
    def _BuildVectorDirection_( self, playerSeeDirection ):
        
        if playerSeeDirection   == Player_See_Directions.RIGHT:   direction = pygame.math.Vector2( 1,0 )
        elif playerSeeDirection == Player_See_Directions.LEFT:  direction = pygame.math.Vector2( -1,0 )
        elif playerSeeDirection == Player_See_Directions.UP:    direction = pygame.math.Vector2( 0,-1 )
        else:   direction = pygame.math.Vector2( 0,1 )

        return direction