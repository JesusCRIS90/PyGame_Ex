import pygame
from ImageRegister import *
from enum import unique, IntEnum
from SettingFile import *
from random import randint

class ParticleEffect( pygame.sprite.Sprite ):
    
    def __init__(self, groups, position, type:Particle_Sprites ):
        super().__init__( groups )
        self.frame_index = 0
        self.animation_speed = 0.15
        self.particle_type = type
        self.sprite_type = "magic"

        self.animation_frames = self.Get_AnimationList()
        self.image = self.animation_frames[ int( self.frame_index ) ]
        self.rect = self.image.get_rect( center = position )
        

    def animate( self ):
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len( self.animation_frames ):
            self.kill()
        else:
            self.image = self.animation_frames[ int( self.frame_index ) ]

    def Get_AnimationList( self ):
        if self.particle_type == Particle_Sprites.LEAF_BREAK:
            list_of_list_of_sprites = ImageRegister().GetSprite( self.particle_type )
            return list_of_list_of_sprites[ randint( 0, len( list_of_list_of_sprites ) - 1 ) ]
        else:
            return ImageRegister().GetSprite( self.particle_type )

    def update( self ):
        self.animate()
        