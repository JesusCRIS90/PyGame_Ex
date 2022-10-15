import pygame
from SettingFile import *
from Tile import Tile
from Player import Player
from ImageRegister import *
from debug import *
import InGame_Parameters as IGP
from support import * 

class Level:

    def __init__(self) -> None:
        
        self.display_surface = pygame.display.get_surface()
        #Sprite group setup
        #self.visible_sprites    = pygame.sprite.Group()
        self.visible_sprites    = YSortCameraGroup()
        self.obstacle_sprites  = pygame.sprite.Group()

        self.player = None

        self.create_map()

    def create_map( self ):
        
        layouts = load_layers_map( "Assets/WorldMap/MapLayers/Map_Layers.json" )
        
        for style, layout in layouts.items():
            for row_index,row in enumerate( layout ):
                for col_index, col in enumerate( row ):
                    if col != '-1':
                        x = col_index * TILESIZE;   y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile( (x, y), [ self.obstacle_sprites], Levels_Sprites_Types.NONE_SPITE )

        self.player = Player( ( 2000, 1430 ), [ self.visible_sprites ], Player_Sprites_Types.PLAYER_TEST, self.obstacle_sprites )
        
    def run( self ):
        #self.visible_sprites.draw( self.display_surface )
        self.visible_sprites.custom_draw( self.player )
        self.visible_sprites.update()
        #debug( self.player.direction )
        debug( self.player.rect.center )


class YSortCameraGroup( pygame.sprite.Group ):

    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width  = self.display_surface.get_size()[ 0 ] // 2
        self.half_height = self.display_surface.get_size()[ 1 ] // 2
        self.offset = pygame.math.Vector2()

        # Background Image ( floor )
        self.floor_rect = ImageRegister().GetSprite( Levels_Sprites_Types.BACKGROUND_IMAGE ).get_rect( topleft = (0,0) )

    def custom_draw( self, player ):

        # Get the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit( ImageRegister().GetSprite( Levels_Sprites_Types.BACKGROUND_IMAGE ), floor_offset_pos )

        # Draw the entire Game
        #for sprite in self.sprites():
        for sprite in sorted( self.sprites(), key = lambda sprite: sprite.rect.centery ):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit( sprite.image, offset_pos )
            if IGP.GAME_PARAMETERS["DebugMode"] == True:
                pygame.draw.rect( self.display_surface, STF.BLUE, pygame.Rect( (offset_pos), (sprite.rect.width, sprite.rect.height) ), 1)