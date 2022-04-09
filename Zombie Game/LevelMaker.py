"""
Created on Sat Feb 19 12:52:55 2022

In this file we make the definition of all Setting for the game

@author: jesus
"""

import json
import pygame
from pygame.sprite import Group

import ImageRegister as IR
from ImageRegister import Levels_Sprites_Types as LST
import SettingFile as STF
import InGame_Parameters as IGP
from Player import Player
from ScenaryObjects import Portal

class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_number, imag_reg:IR.ImageRegister ,all_tiles_group:Group, platform_group = None ):
        """Initialize the tile"""
        super().__init__()
        
        """Load in the correct image and add it to the correct sub group"""
        #Dirt tiles
        if image_number == 1:
            self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.DIRT_PLATFORM ) , (32,32) )
        #Platform tiles
        elif image_number == 2:
            self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.BIG_CENTRAL_PLATFORM ), (32,32))
            platform_group.add(self)
        elif image_number == 3:
            self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.LEFT_PLATFORM ), (32,32))
            platform_group.add(self)
        elif image_number == 4:
            self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.LITTLE_CENTRAL_PLATFORM ) , (32,32))
            platform_group.add(self)
        elif image_number == 5:
            self.image = pygame.transform.scale( imag_reg.GetSprite( IR.Levels_Sprites_Types.RIGTH_PLATFORM ), (32,32))
            platform_group.add(self)

        #Add every tile to the main group
        all_tiles_group.add(self)

        #Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #Create a mask for better player collisions
        # self.mask = pygame.mask.from_surface(self.image)
    
    def update( self ):
        if IGP.GAME_PARAMETERS["DebugMode"] == True:
            pygame.draw.rect( IGP.GAME_PARAMETERS["CanvasGame"], STF.BLUE, self.rect, 1)



class LevelMaker():
    """A class to build a level from a json file"""
    
    def __init__( self, path_lvl:str, all_tiles_group:Group, platforms_group:Group, portals_groups:Group, imag_reg:IR.ImageRegister ):
        self.level_map = self._load_level_map_( path_lvl )
        self.isMapBuilded = False
        if self.level_map != None:
            self._Build_Map_(self.level_map, all_tiles_group, platforms_group, portals_groups, imag_reg)

    
    def _load_level_map_( self, path_lvl:str ):
        try:
            f = open( path_lvl )
            level = json.load( f )
            f.close()
            return level["level"]
        except:
            return None
    
    def GetPlayerPosition( self ):
        return self.player_position
        # pass

    
    def _Build_Map_( self, tile_map:list, all_tiles_group:Group, platforms_group:Group, portals_groups:Group, imag_reg:IR.ImageRegister ):
        
        for y in range( len( tile_map ) ):
        #Loop through the 40 elements in a given list (cols) (j moves us across the map)
            for x in range( len( tile_map[ y ] ) ):
     
                #Dirt tiles
                if tile_map[ y ][ x ] == 1:
                    Tile(x*32, y*32, 1, imag_reg, all_tiles_group )
                
                #Platform tiles
                elif tile_map[ y ][ x ] == 2:
                    Tile(x*32, y*32, 2, imag_reg, all_tiles_group, platforms_group )
                elif tile_map[ y ][ x ] == 3:
                    Tile(x*32, y*32, 3, imag_reg, all_tiles_group, platforms_group )
                elif tile_map[ y ][ x ] == 4:
                    Tile(x*32, y*32, 4, imag_reg, all_tiles_group, platforms_group )
                elif tile_map[ y ][ x ] == 5:
                    Tile(x*32, y*32, 5, imag_reg, all_tiles_group, platforms_group )
                
                # #Ruby Maker
                # elif tile_map[i][j] == 6:
                #     RubyMaker(j*32, i*32, my_main_tile_group)
                #Portals
                elif tile_map[ y ][ x ] == 7:
                    Portal(x*32, y*32, imag_reg, LST.GREEN_PORTAL, portals_groups)
                
                elif tile_map[ y ][ x ] == 8:
                    Portal(x*32, y*32, imag_reg, LST.PURPLE_PORTAL, portals_groups)
                
                #Player
                elif tile_map[ y ][ x ] == 9:
                    self.player_position = [ x, y ]

                
        self.isMapBuilded = True
    
    def IsMapBuilded( self ):
        return self.isMapBuilded

