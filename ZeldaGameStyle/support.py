from csv import reader
import json
from os import walk
import pygame

boundary_csv_path   = "Assets/WorldMap/MapLayers/map_FloorBlocks.csv"
grass_csv_path      = "Assets/WorldMap/MapLayers/map_Grass.csv"
object_csv_path   = "Assets/WorldMap/MapLayers/map_Objects.csv"
entities_csv_path   = "Assets/WorldMap/MapLayers/map_Entities.csv"

def CustomSingleton( cls ):

    instances= dict()

    def wrap( *args, **kwargs ):
        if cls not in instances:
            instances[ cls ] = cls( *args, **kwargs )

        return instances[ cls ]

    return wrap


class PyGameTimer():

    def __init__( self, elapsedTime:int ) -> None:
        self.time_init = None
        self.elapsedTime = 100
        self.Set_elapsedTime( elapsedTime )

    def Set_elapsedTime( self, elapsedTime:int ):
        if elapsedTime > 0:
            self.elapsedTime = elapsedTime
        return self

    def Start( self ):
        self.time_init = pygame.time.get_ticks()
        pass

    def ElapsedTime_Reach( self ):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.time_init >= self.elapsedTime:
            return True
        else:
            return False


def import_csv_layout( path ):
    terrain_map = []
    with open( path ) as level_map:
        layout = reader( level_map, delimiter = "," )
        for row in layout:
            terrain_map.append( list( row ) )
    
    return terrain_map

def load_layers_map( path_lvl:str ):
        try:
            with open( path_lvl ) as f:
                level = json.load( f )
            return level
        except:
            return None

def dict_layer_map_2_json( jsonFileName:str, layers:dict ):
    with open( jsonFileName + ".json", 'w', encoding='utf-8') as f:
        json.dump( layers , f, ensure_ascii = False, indent = None )

def import_folder( path ):
    surface_list = []

    for _,__,img_files in walk( path ):
        for image in img_files:
            full_path = path + '/' + image
            surface_list.append( pygame.image.load( full_path ).convert_alpha() )

    return surface_list

def Create_Json_Map_Layers( fileName ):
    
    dict_layer_map_2_json( fileName, {  
     "boundary": import_csv_layout( boundary_csv_path ), 
     "grass": import_csv_layout( grass_csv_path ), 
     "object": import_csv_layout( object_csv_path ),
     "entities": import_csv_layout( entities_csv_path ) 
    } )


""" Uncomment only to create the Json File """
# Create_Json_Map_Layers( "MapLayers" )




