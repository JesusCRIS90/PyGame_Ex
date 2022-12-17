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

        self.sprite_type = "No_Grass"
        
        if self._IsGrassSprite_( enum_sprite ) == True:
            self.sprite_type = "grass"

        
        if enum_sprite == Levels_Sprites_Types.NONE_SPRITE:
            self.image = pygame.Surface( ( STF.TILESIZE * 0.90, STF.TILESIZE * 0.9 ) )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, -10 )

        else:
            self.image = ImageRegister().GetSprite( enum_sprite )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( -20, -10 )
        
    def _IsGrassSprite_( self, sprite_type ):
        if sprite_type == Levels_Sprites_Types.GRASS_1:
            return True
        if sprite_type == Levels_Sprites_Types.GRASS_2:
            return True
        if sprite_type == Levels_Sprites_Types.GRASS_3:
            return True
            
        return False

        # if enum_sprite == Levels_Sprites_Types.GRASS_1:
        #     self.image = ImageRegister().GetSprite( Levels_Sprites_Types.GRASS_1 )
        #     self.rect  = self.image.get_rect( topleft = position )
        #     self.hitbox = self.rect.inflate( 0, -10 )
        
        # if enum_sprite == Levels_Sprites_Types.GRASS_2:
        #     self.image = ImageRegister().GetSprite( Levels_Sprites_Types.GRASS_2 )
        #     self.rect  = self.image.get_rect( topleft = position )
        #     self.hitbox = self.rect.inflate( 0, -10 )
        
        # if enum_sprite == Levels_Sprites_Types.GRASS_3:
        #     self.image = ImageRegister().GetSprite( Levels_Sprites_Types.GRASS_3 )
        #     self.rect  = self.image.get_rect( topleft = position )
        #     self.hitbox = self.rect.inflate( 0, -10 )

    # def update( self ):
    #     if IGP.GAME_PARAMETERS["DebugMode"] == True:
    #         pygame.draw.rect( pygame.display.get_surface(), STF.BLUE, self.rect, 1)

