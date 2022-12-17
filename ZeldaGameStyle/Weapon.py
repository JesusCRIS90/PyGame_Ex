import pygame
from Animations import Player_See_Directions
from ImageRegister import *

class PlayerWeapon( pygame.sprite.Sprite ):

    def __init__(self, player, groups, weapon_type:Weapons_Types ):
        super().__init__( groups )

        self.sprite_type = 'weapon'

        # self.image = pygame.Surface( (40,40) )
        self.image = ImageRegister().GetSprite( weapon_type )
        
        if player.animations.Get_SeeDirection() == Player_See_Directions.DOWN:
            self.rect = self.image.get_rect( midtop = player.rect.midbottom + pygame.math.Vector2(10,-2) )
        
        elif player.animations.Get_SeeDirection() == Player_See_Directions.UP:
            self.rect = self.image.get_rect( midbottom = player.rect.midtop + pygame.math.Vector2(10,16) )
        
        elif player.animations.Get_SeeDirection() == Player_See_Directions.RIGHT:
            self.rect = self.image.get_rect( midleft = player.rect.midright + pygame.math.Vector2(0,16) )
        
        elif player.animations.Get_SeeDirection() == Player_See_Directions.LEFT:
            self.rect = self.image.get_rect( midright = player.rect.midleft + pygame.math.Vector2(0,16) )
    
        else:
            self.rect = self.image.get_rect( center = player.rect.center )
    

    def destroy( self ):
        self.kill()