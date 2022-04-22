"""
Created on Sat Feb 19 12:52:55 2022

In this file we make the definition of all Setting for the game

@author: jesus
"""

# Game Name
GAME_NAME = "Zombie Nightmare"

# Setting for Display
WINDOW_WIDTH = 1280 ; WINDOW_HEIGHT = 720

# Setting FPS
FPS = 60

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


# Setting Font
FONT_NAME = "Assets/Facon.ttf"
FONT_SIZE = 32

# Maximun Number of Player Bullet
MAX_PLAYER_BULLETS = 2; MAX_ENEMIES_BULLETS = 3

# Speed Enemies and Player
ENEMIES_SPEED   = 3;  ENEMIES_BULLET_SPEED    = 10
PLAYER_SPEED    = 6;  PLAYER_BULLET_SPEED     = 12

# Rubies
MAX_RUBIES_ALLOWED = 5; STANDAR_RUBY_TIME_CREATION = 10000 # Miliseconds

# Zombies
MAX_ZOMBIES_ALLOWED = 10; STANDAR_ZOMBI_TIME_CREATION = 5000 # Miliseconds

INITIAL_ROUND_TIME = 30