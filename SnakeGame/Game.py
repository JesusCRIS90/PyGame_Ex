"""
Created on Sat Feb 19 12:47:29 2022

    Base Class to control the game initialization and game loop.
    Each New Game must inherit from this class and override the methods:
        
        __UpdateGameState__()
        __init__()

@author: jesus
"""

import pygame
import SettingFile as STF


class Game():
    
    def __init__( self ):
        
        pygame.init()
        
        self.display_surface = pygame.display.set_mode( (STF.WINDOW_WIDTH, STF.WINDOW_HEIGTH) )
        self.clockGame = None
        self.running = False
    
        self.__SetGameName__()
        self.__Init_Clock_Game__()
        
    
    def __SetGameName__( self ):
        pygame.display.set_caption( STF.GAME_NAME )
        
        
    def __Init_Clock_Game__( self ):
        self.clockGame = pygame.time.Clock()
        
        
    def __UpdateGameState__( self ):
       
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.BLACK )    
                
                    
        pygame.display.update()
        self.clockGame.tick( STF.FPS )

    def _CheckingEvents_( self ):
        # Loop through a list of Event Objects that have occured
        for event in pygame.event.get():
            # print( event )
            if event.type == pygame.QUIT:
                self.running = False
        
    def RunGame( self ):
        
        # The main game loop
        self.running = True
        while self.running:

            self._CheckingEvents_( )
            self.__UpdateGameState__( )

        
        #End the game
        pygame.quit()    

