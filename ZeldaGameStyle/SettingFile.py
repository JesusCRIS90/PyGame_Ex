"""
Created on Sat Feb 19 12:52:55 2022

In this file we make the definition of all Setting for the game

@author: jesus
"""

from ImageRegister import Weapons_Types

# Game Name
GAME_NAME = "Custom Zelda Game"

# Setting for Display
# WINDOW_WIDTH = 1280 ; WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1920 ; WINDOW_HEIGHT = 1080

# Setting FPS
FPS = 60

ELAPSED_PLAYER_ATTACK_TIME = 400

# TileSize
TILESIZE = 64


# Settings Colors
BLACK       = ( 0, 0, 0 )
WHITE       = ( 255, 255, 255 )
RED         = ( 255, 0, 0 )
DARKRED     = (150, 0, 0)
GREEN       = ( 0, 255, 0 )
DARKGREEN   = ( 10, 50, 10 )
BLUE        = ( 0, 0, 255 )
YELLOW      = ( 255, 255, 0 )
CYAN        = ( 0, 255, 255 )
MAGENTA     = ( 255, 0, 255 )

# Level File
PATH_LEVEL_JSON = "Assets/levels/level_1.json"



# UI COLORS
WATER_COLOR             = '#71DDEE'
UI_BG_COLOR             = '#222222'
UI_BORDER_COLOR         = '#111111'
TEXT_COLOR              = '#EEEEEE'
HEALTH_COLOR            = "red"
ENERGY_COLOR            = "blue"
UI_BORDER_COLOR_ACTIVE  = 'gold'

# UI SIZES
BAR_HEIGHT          = 20
HEALTH_BAR_WIDTH    = 200
ENERGY_BAR_WIDTH    = 140
ITEM_BOX_SIZE       = 80

# PLAYER SETTINGS
PLAYER_MAX_HEALTH = HEALTH_BAR_WIDTH
PLAYER_MAX_ENERGY = ENERGY_BAR_WIDTH
PLAYER_RECOVERY_ENERGY = 0.05

# Setting Font
FONT_NAME = "Assets/Font/joystix.ttf"
FONT_SIZE = 18


# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20},
	'heal' : {'strength': 20,'cost': 10}
    }

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 
               'attack_sound':'../audio/attack/slash.wav', "attack_cooldown": 400,
               'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360,},
	
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',
                'attack_sound':'../audio/attack/claw.wav', "attack_cooldown": 750,
                'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	
    'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder',
               'attack_sound':'../audio/attack/fireball.wav', "attack_cooldown": 400,
               'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	
    'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 
               'attack_sound':'../audio/attack/slash.wav', "attack_cooldown": 400,
               'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
    }

# weapons 
weapon_data = {
	Weapons_Types.SWORD:    {'cooldown': 100, 'damage': 15 },
	Weapons_Types.LANCE:    {'cooldown': 400, 'damage': 30},
	Weapons_Types.AXE:      {'cooldown': 300, 'damage': 20},
	Weapons_Types.RAPIER:   {'cooldown': 50,  'damage': 8},
	Weapons_Types.SAI:      {'cooldown': 80,  'damage': 10}
    }
