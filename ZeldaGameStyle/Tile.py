import pygame
import SettingFile as STF
from pygame.sprite import Group
from ImageRegister import *
import InGame_Parameters as IGP

class Tile(pygame.sprite.Sprite):

    def __init__(self, position, groups:Group, enum_sprite ) -> None:
        super().__init__( groups )
        self.image = None
        self.rect = None
        self.hitbox = None
        
        self.sprite_type = "object"
        
        if self._IsGrassSprite_( enum_sprite ) == True:
            self.sprite_type = "grass"
        
        if enum_sprite == Levels_Sprites_Types.NONE_SPRITE:
            self.sprite_type = "invisible"

        y_offset = STF.HITBOX_OFFSET[ self.sprite_type ]
        
        if enum_sprite == Levels_Sprites_Types.NONE_SPRITE:
            self.image = pygame.Surface( ( STF.TILESIZE * 0.90, STF.TILESIZE * 0.9 ) )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, y_offset )

        else:
            self.image = ImageRegister().GetSprite( enum_sprite )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( -20, y_offset )
        
    def _IsGrassSprite_( self, sprite_type ):
        if sprite_type == Levels_Sprites_Types.GRASS_1:
            return True
        if sprite_type == Levels_Sprites_Types.GRASS_2:
            return True
        if sprite_type == Levels_Sprites_Types.GRASS_3:
            return True
            
        return False


