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
        self.sprite_type = enum_sprite

        
        if enum_sprite == Levels_Sprites_Types.NONE_SPRITE:
            self.image = pygame.Surface( ( STF.TILESIZE * 0.90, STF.TILESIZE * 0.9 ) )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, -10 )

        else:
            self.image = ImageRegister().GetSprite( enum_sprite )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( -20, -10 )

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



    # def __init__(self, x, y, image_number, imag_reg:IR.ImageRegister ,all_tiles_group:Group, platform_group = None ):
    #     """Initialize the tile"""
    #     super().__init__()
        
    #     """Load in the correct image and add it to the correct sub group"""
    #     #Dirt tiles
    #     if image_number == 1:
    #         self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.DIRT_PLATFORM ) , (32,32) )
    #     #Platform tiles
    #     elif image_number == 2:
    #         self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.BIG_CENTRAL_PLATFORM ), (32,32))
    #         platform_group.add(self)
    #     elif image_number == 3:
    #         self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.LEFT_PLATFORM ), (32,32))
    #         platform_group.add(self)
    #     elif image_number == 4:
    #         self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.LITTLE_CENTRAL_PLATFORM ) , (32,32))
    #         platform_group.add(self)
    #     elif image_number == 5:
    #         self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.RIGTH_PLATFORM ), (32,32))
    #         platform_group.add(self)

    #     #Add every tile to the main group
    #     all_tiles_group.add(self)

    #     #Get the rect of the image and position within the grid
    #     self.rect = self.image.get_rect()
    #     self.rect.topleft = (x, y)

    #     #Create a mask for better player collisions
    #     self.mask = pygame.mask.from_surface(self.image)
    
    # def update( self ):
    #     if IGP.GAME_PARAMETERS["DebugMode"] == True:
    #         pygame.draw.rect( IGP.GAME_PARAMETERS["CanvasGame"], STF.BLUE, self.rect, 1)