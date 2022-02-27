
"""
Created on Sat Feb 26 12:52:55 2022

This file contain the main "in-game" parameters relative to the game

@author: jesus
"""


from enum import unique, IntEnum


""" ENUMS """
@unique
class GAME_STATES( IntEnum ):
    RUNNING         = 0
    GAME_OVER       = 1
    INIT            = 2
    MOVE2RUNNING    = 3
    MOVE2GAMEOVER   = 4

"""
    Dictionary with main parameters of game
"""
GAME_PARAMETERS = {
    "Round": 50,
    "Score": 0,
    "Lives": 5,
    "GameState": GAME_STATES.INIT
}