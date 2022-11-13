from csv import reader
import json
from os import walk
import pygame

boundary_csv_path   = "Assets/WorldMap/MapLayers/map_FloorBlocks.csv"
grass_csv_path      = "Assets/WorldMap/MapLayers/map_Grass.csv"
object_csv_path   = "Assets/WorldMap/MapLayers/map_Objects.csv"

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

# dict_layer_map_2_json( "MapLayers", { 
#     "boundary": import_csv_layout( boundary_csv_path ),
#     "grass": import_csv_layout( grass_csv_path ),
#     "object": import_csv_layout( object_csv_path )
# } )

# Map_Layers = load_layers_map( "Assets/WorldMap/MapLayers/MapLayers.json" )
