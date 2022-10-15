from csv import reader
import json

def import_csv_layout( path ):
    terrain_map = []
    with open( path ) as level_map:
        layout = reader( level_map, delimiter = "," )
        for row in layout:
            terrain_map.append( list( row ) )
    
    return terrain_map

def layer_map_list_2_json( layer_map:list, layerName:str ):

    with open( layerName + ".json", 'w', encoding='utf-8') as f:
        json.dump({ layerName: layer_map }, f, ensure_ascii = False, indent = None )

def load_layers_map( path_lvl:str ):
        try:
            with open( path_lvl ) as f:
                level = json.load( f )
            return level
        except:
            return None



#layer_map_list_2_json( import_csv_layout( "Assets/WorldMap/MapLayers/map_FloorBlocks.csv" ), "boundary" )
Map_Layers = load_layers_map( "Assets/WorldMap/MapLayers/Map_Layers.json" )