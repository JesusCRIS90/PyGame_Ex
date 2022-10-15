
"""
Created on Sat Feb 26 12:52:55 2022

This file contain the main "in-game" parameters relative to the game

@author: jesus
"""


from enum import unique, IntEnum


""" ENUMS """
@unique
class GAME_STATES( IntEnum ):
    INIT_SCREEN         = 0
    GAME_OVER_SCREEN    = 1
    NEXT_ROUND_SCREEN   = 2
    GAME_RUNNING        = 3
    GAME_OVER           = 4
    NEXT_ROUND          = 5
    MOVE_2_START        = 6

"""
    Dictionary with main parameters of game
"""
GAME_PARAMETERS = {
    "GameState": GAME_STATES.INIT_SCREEN,
    "DebugMode": True,
    "CanvasGame": None
}

"""
    Dictionary with Sprites_Group used in the game
    
"""
GAME_SPRITES_GROUPS = {
    "Tiles_Group": None,
    "Player_Group": None
}