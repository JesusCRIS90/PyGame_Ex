
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

"""
    Dictionary with main parameters of game
"""
GAME_PARAMETERS = {
    "Round": 7,
    "GameState": GAME_STATES.INIT
}