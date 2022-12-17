import pygame
from SettingFile import *
from Tile import Tile
from Player import Player
from Enemy import Enemy
from ImageRegister import *
from debug import *
import InGame_Parameters as IGP
from support import *

from Game_UI import Game_UI
from CollisionManager import CollissionManager

class Level:

    def __init__(self) -> None:
        
        self.display_surface = pygame.display.get_surface()
        #Sprite group setup
        #self.visible_sprites    = pygame.sprite.Group()
        self.visible_sprites    = YSortCameraGroup()
        self.obstacle_sprites  = pygame.sprite.Group()

        self.player = None

        self.create_map()

        # User Interface Create
        self.ui = Game_UI()


    def create_map( self ):
        
        layouts = load_layers_map( "Assets/WorldMap/MapLayers/MapLayers.json" )
        
        for style, layout in layouts.items():
            self.create_layer( style, layout )
        
        CollissionManager().set_VisibleSprite( self.visible_sprites )

        
    def create_layer( self, layerName:str, layer:list ):
        for row_index,row in enumerate( layer ):
                for col_index, col in enumerate( row ):
                    if col != '-1':
                        x = col_index * TILESIZE;   y = row_index * TILESIZE
                        if layerName == 'boundary':
                            Tile( (x, y), [ self.obstacle_sprites], Levels_Sprites_Types.NONE_SPRITE )
                        if layerName == 'grass':
                            Tile( (x, y), [ self.obstacle_sprites, 
                                            self.visible_sprites, 
                                            CollissionManager().get_attackableSpriteGroup()], 
                                            Grass_Dict[ int( col ) ] )
                        if layerName == 'object':
                            Tile( ( x, y - TILESIZE ), [ self.obstacle_sprites, self.visible_sprites], Object_Dict[ int( col ) ] )
                        if layerName == 'entities':
                            if col == '394':
                                self.create_player( ( x, y ) )
                            else:
                                Enemy( ( x, y ), self.Get_Monster_Type_Name( col ), 
                                    [ self.visible_sprites,
                                      CollissionManager().get_attackableSpriteGroup()],
                                      self.obstacle_sprites )
    
    def create_player( self, pos ):
        self.player = Player( pos, [ self.visible_sprites ], Player_Sprites_Types.PLAYER_TEST, self.obstacle_sprites )

    def Get_Monster_Type_Name( self, col_pos ):
        if col_pos      == "390":  return "bamboo"
        elif col_pos    == "391":  return "spirit"
        elif col_pos    == "392":  return "raccoon"
        else:                      return "squid"


    def run( self ):
        #self.visible_sprites.draw( self.display_surface )
        self.visible_sprites.custom_draw( self.player )
        self.visible_sprites.update()
        # self.visible_sprites.enemy_update()
        CollissionManager().player_attack_logic()
        self.ui.display()


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
    
    def enemy_update( self ):
        enemy_sprites = [ sprite for sprite in self.sprites() if sprite.sprite_type == "enemy" ]
        for enemy in enemy_sprites:
            enemy.enemy_update()