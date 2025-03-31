"""
Created on Sat Feb 19 12:52:55 2022

This class is the blueprint for the snake representation in the game

@author: jesus
"""

import pygame
import SettingFile as STF

#Set Snakes Values
SNAKE_SIZE = 20


class Snake( pygame.sprite.Sprite ):
    
    def __init__( self, surf_disp:pygame.display, head_init = (0, 0) ):
        """Initialize the snake Class"""
        self.surface_display = surf_disp
        self.dx = 0
        self.dy = 0
        self.bodyCoord = []
        self.headCoord = ( head_init[ 0 ], head_init[ 1 ], SNAKE_SIZE, SNAKE_SIZE )
        self.headRect = pygame.draw.rect( self.surface_display, STF.GREEN, self.headCoord )
    
        
    # # Este metodo no sirve
    # def update( self ):
    #     """Update the snake Class"""
    #     # self.MoveSnake( event )
    #     self.UpdateBodySnake()
    #     self.UpdateSnakeHead()
    #     self.DrawSnake()

    
    def MoveSnake( self, event:pygame.event ):
        """Update the snake move direction Snake"""
                #Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -1*SNAKE_SIZE
                self.dy = 0
            if event.key == pygame.K_RIGHT:
                self.dx = SNAKE_SIZE
                self.dy = 0
            if event.key == pygame.K_UP:
                self.dx = 0
                self.dy = -1*SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                self.dx = 0
                self.dy = SNAKE_SIZE
                
    
    def UpdateBodySnake( self ):
        """Update differents part of snake body"""
        self.bodyCoord.insert(0, self.headCoord)
        self.bodyCoord.pop()
        
    
    def UpdateSnakeHead( self ):
        """Update the x,y position of the snakes head and make a new coordinate"""
        head_x = self.headCoord[ 0 ] + self.dx
        head_y = self.headCoord[ 1 ] + self.dy
        self.headCoord = ( head_x, head_y, SNAKE_SIZE, SNAKE_SIZE )
        
    def DrawSnake( self ):
        #Blit assets
        for body in self.bodyCoord:
            # pygame.draw.rect(display_surface, DARKGREEN, body)
            pygame.draw.rect( self.surface_display, STF.GREEN, body )
        self.headRect = pygame.draw.rect( self.surface_display, STF.GREEN, self.headCoord )
        
    def Reset( self ):
        self.dx = 0
        self.dy = 0
        self.bodyCoord = []
        self.headCoord = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGTH//2 + 100 , SNAKE_SIZE, SNAKE_SIZE )
        
    def IsSnakeGameOver( self ):
        if self.__Is_SnakeCollide_ItSelf__():
            return True
        if self.__Is_Snake_OutScreen__():
            return True
        return False
    
    def __Is_SnakeCollide_ItSelf__( self ):
        if self.headCoord in self.bodyCoord:
            return True      
        return False

    def __Is_Snake_OutScreen__( self ):
        if self.headRect.left < 0:
            return True
        if self.headRect.right > STF.WINDOW_WIDTH:
            return True
        if self.headRect.top < 0:
            return True
        if self.headRect.bottom > STF.WINDOW_HEIGTH:
            return True
        return False
        
   
    
    