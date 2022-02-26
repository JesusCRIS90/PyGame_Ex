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
import Apple
import Game_HUD


class SnakeGame( SKG.Game ):
    
    def __init__( self ):
        # Calling the init method from Base Class
        super().__init__()

        self.is_paused = False
        self.score = 0

        self.snake = Snake.Snake( self.display_surface ,( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGTH//2 + 100 ) )
        self.apple = Apple.Apple( self.display_surface )
        self.game_hud = Game_HUD.GameHUD( self.display_surface, self.score )

        
    def __UpdateGameState__( self ):
    
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.WHITE )    
        
    
        self.snake.UpdateBodySnake()
        self.snake.UpdateSnakeHead()
        
        self._GameOverCheck_()
        
        self._ChekingCollission_()
        
        self.game_hud.draw_Score()
        self.snake.DrawSnake()
        self.apple.draw()
        
        
                    
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
            
    def _ChekingCollission_( self ):
        if self.snake.headRect.colliderect( self.apple.coord ):
            # Add Sound Here
            self.score += 1
            self.apple.generateNewApple()
            self.snake.bodyCoord.append( self.snake.headCoord )
            self.game_hud.updateScore( self.score )
            
    def _QuitGame_( self ):
        self.is_paused = False
        self.running = False
    
    def _ResumeGame_( self ):
        self.score = 0
        self.snake.Reset()
        self.is_paused = False
        self.game_hud.updateScore(  )
        # self.game_hud.draw_Score()

    def _GameOver_State_( self ):
        self.is_paused = True
        while self.is_paused:
            # print( "Inside Bucle While" )
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._ResumeGame_()
                if event.type == pygame.QUIT:
                    self._QuitGame_()
                    
    def _GameOverCheck_( self ):
        if self.snake.IsSnakeGameOver():

            # 1- Show here the GameOver Screen --> Add these feature
            self.display_surface.fill( STF.WHITE )
            self.game_hud.draw_GameOver()
            pygame.display.update()
            # 2.- Put Game in GameOverState
            self._GameOver_State_()
    

# snake_game = SKG.Game(); snake_game.RunGame()

snake_game = SnakeGame(); snake_game.RunGame()
