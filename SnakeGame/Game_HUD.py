"""
Created on Sat Feb 19 12:52:55 2022

This class is the blueprint for the snake representation in the game

@author: jesus
"""

import pygame
import SettingFile as STF





class GameHUD():
    
    def __init__( self, surf_disp:pygame.display, score = 0 ):
        
        self.surface_display = surf_disp
        self.font = pygame.font.SysFont( STF.FONT_NAME ,STF.FONT_SIZE )
        
        #Set text
        self.title_text = self.font.render("~~Snake~~", True, STF.GREEN, STF.DARKRED)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGTH//2)
        
        self.score_text = self.font.render("Score: " + str(score), True, STF.GREEN, STF.DARKRED)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topleft = (10, 10)
        
        self.game_over_text = self.font.render("GAMEOVER", True, STF.RED, STF.DARKGREEN )
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGTH//2)
        
        self.continue_text = self.font.render("Press any key to play again", True, STF.RED, STF.DARKGREEN)
        self.continue_rect = self.continue_text.get_rect()
        self.continue_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGTH//2 + 32)
        
    def updateScore( self, score = 0 ):
        self.score_text = self.font.render("Score: " + str(score), True, STF.GREEN, STF.DARKRED)
        
    def draw_GameOver( self ):
        self.surface_display.blit( self.game_over_text, self.game_over_rect)
        self.surface_display.blit( self.continue_text, self.continue_rect)
    
    def draw_Score( self ):
        self.surface_display.blit( self.score_text, self.score_rect )

        