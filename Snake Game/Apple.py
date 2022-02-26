"""
Created on Sat Feb 19 12:52:55 2022

This class is the blueprint for the snake representation in the game

@author: jesus
"""

import pygame
import random
import SettingFile as STF


#Set Snakes Values
SNAKE_SIZE = 20



class Apple( pygame.sprite.Sprite ):
    
    def __init__( self, surf_disp:pygame.display, init_pos = ( 300, 300 )  ):
        """Initialize the snake Class"""
        self.surface_display = surf_disp
        self.coord = ( init_pos[ 0 ], init_pos[ 1 ], SNAKE_SIZE, SNAKE_SIZE )
        self.rect = pygame.draw.rect( self.surface_display, STF.RED, self.coord )
    
        
    # def update( self ):
    #     """Update the Apple Class"""
    #     self.draw()
        
        
    def generateNewApple( self ):
        self.coord = ( random.randint(0, STF.WINDOW_WIDTH - SNAKE_SIZE),
                       random.randint(0, STF.WINDOW_HEIGTH - SNAKE_SIZE),
                       SNAKE_SIZE, SNAKE_SIZE )
        
        # print( self.coord )
    
    def draw( self ):
        self.rect = pygame.draw.rect( self.surface_display, STF.RED, self.coord )
        
        
    
    
    