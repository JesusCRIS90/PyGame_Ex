import pygame
from support import CustomSingleton


@CustomSingleton
class CollissionManager:

    def __init__(self) -> None:
        
        self.attack_sprites     = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

    def get_attackSpriteGroup( self ):
        return self.attack_sprites
    
    def get_attackableSpriteGroup( self ):
        return self.attackable_sprites
    
    
    def player_attack_logic( self ):
        
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprite = pygame.sprite.spritecollide( attack_sprite, self.attackable_sprites, False )
                if collision_sprite:
                    for target_sprite in collision_sprite:
                        if target_sprite.sprite_type == "grass":
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage( attack_sprite.sprite_type )