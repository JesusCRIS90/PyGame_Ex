#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:15:49 2022

This class is a specialization of the class Base Game.

@author: jesus
"""
import pygame
import Game as SKG
import SettingFile as STF
import Snake



class SnakeGame( SKG.Game ):
    
    def __init__( self ):
        # Calling the init method from Base Class
        super().__init__()
        self.snake = Snake.Snake( self.display_surface ,( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGTH//2 + 100 ) )
        
    def __UpdateGameState__( self ):
    
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.WHITE )    
        
        self.snake.update()
        
                    
        pygame.display.update()
        self.clockGame.tick( STF.FPS )
        
    def _CheckingEvents_( self ):
        
        # Loop through a list of Event Objects that have occured
        for event in pygame.event.get():
            # print( event )
            if event.type == pygame.QUIT:
                self.running = False
            # Particular Events Management
            self.snake.MoveSnake( event )






# snake_game = SKG.Game(); snake_game.RunGame()

snake_game = SnakeGame(); snake_game.RunGame()
