import pygame
from support import CustomSingleton
from InGame_Parameters import PlayerStats
from ParticleEffects import ParticleEffect
from ImageRegister import *
from random import randint

@CustomSingleton
class CollissionManager:

    def __init__(self) -> None:
        
        self.attack_sprites     = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.visible_sprites    = pygame.sprite.Group()

    def get_attackSpriteGroup( self ):
        return self.attack_sprites
    
    def get_attackableSpriteGroup( self ):
        return self.attackable_sprites
    
    def set_VisibleSprite( self, visible_sprites ):
        self.visible_sprites = visible_sprites
    
    def player_attack_logic( self ):
        
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprite = pygame.sprite.spritecollide( attack_sprite, self.attackable_sprites, False )
                if collision_sprite:
                    for target_sprite in collision_sprite:
                        if target_sprite.sprite_type == "grass":
                            
                            pos = target_sprite.rect.center
                            for leaf in range( randint( 3,6 ) ):
                                ParticleEffect( [ self.visible_sprites ], pos, Particle_Sprites.LEAF_BREAK )

                            target_sprite.kill()
                        else:
                            target_sprite.get_damage( attack_sprite.sprite_type )
    
    # Called -> "damage_player"
    def enemy_attack_logic( self, damage_amount, attack_type ):
        if PlayerStats().GetPlayerVulnerable():
            
            # Calculate New Player Life
            player_health = PlayerStats().Get_Health()
            player_health -= damage_amount
            PlayerStats().Set_Health( player_health )
            
            # Making Player Invulnerable
            PlayerStats().SetPlayerVulnerable( False )

            # Spawn Particles
            pos = PlayerStats().GetPlayerPosition()
            particle_attack_type = Particles_EnemiesAttack_Dict[ attack_type ]
            ParticleEffect( [ self.visible_sprites ], pos, particle_attack_type )

