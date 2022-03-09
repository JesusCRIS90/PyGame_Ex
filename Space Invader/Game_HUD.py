"""
Created on Sat Feb 19 12:52:55 2022

This class is the blueprint for the Space Invader HUB representation in the game

@author: jesus
"""

import pygame
import SettingFile as STF
import InGame_Parameters as IGP


class GameHUD():
    
    def __init__( self, surf_disp:pygame.display ):
        
        self.surface_display = surf_disp
        self.font = pygame.font.Font( STF.FONT_NAME, STF.FONT_SIZE )
        
        # Text for Init and Reset Screen
        self.game_title = self.font.render( STF.GAME_NAME , True, STF.WHITE )
        self.game_title_rect = self.game_title.get_rect()
        self.game_title_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 - 1.5*STF.FONT_SIZE )
        
        self.round_text = self.font.render("Round: " + str( IGP.GAME_PARAMETERS["Round"] ), True, STF.WHITE )
        self.round_rect = self.round_text.get_rect()
        self.round_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 + 0*STF.FONT_SIZE )

        self.continue_text = self.font.render("Press any key to play again", True, STF.WHITE )
        self.continue_rect = self.continue_text.get_rect()
        self.continue_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 + 1.5*STF.FONT_SIZE )
        
        # Text for GameOver and Reset Screen
        self.game_over_text = self.font.render("GAME OVER", True, STF.WHITE )
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 - 1*STF.FONT_SIZE )

       # Text for GameOver and Reset Screen
        self._updateScore_()
        self._updateLives_()


    def update( self ):
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.INIT:
            self.draw_Init_Screen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.GAME_OVER:
            self.draw_GameOver_Screen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.RUNNING:
            self.draw_GameScreen()
            
                
    def draw_GameOver_Screen( self ):
        self._updateFinalScore_()
        self.surface_display.blit( self.game_over_text, self.game_over_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )
        self.surface_display.blit( self.final_score, self.final_score_rect )


    def draw_Init_Screen( self ):
        self._updateRoundNumber_()
        self.surface_display.blit( self.game_title, self.game_title_rect )
        self.surface_display.blit( self.round_text, self.round_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )

    def draw_GameScreen( self ):
        "Update the Game HUB Screen"
        self._updateScore_()
        self._updateLives_()
        self._updateRoundNumber_()
        self.surface_display.blit( self.score_text, self.score_rect )
        self.surface_display.blit( self.lives_text, self.lives_rect )
        self.surface_display.blit( self.round_text, self.round_rect )
        pygame.draw.line(self.surface_display, STF.WHITE, (0, STF.FONT_SIZE + 10 ), ( STF.WINDOW_WIDTH, STF.FONT_SIZE + 10 ), 4)
        pygame.draw.line(self.surface_display, STF.WHITE, (0, STF.WINDOW_HEIGHT - 100), (STF.WINDOW_WIDTH, STF.WINDOW_HEIGHT - 100), 4)

    def _updateRoundNumber_( self ):
        self.round_text = self.font.render("Round: " + str( IGP.GAME_PARAMETERS["Round"] ), True, STF.WHITE )
        self.round_rect = self.round_text.get_rect()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.INIT:
            self.round_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 + 0*STF.FONT_SIZE )
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.RUNNING:
            self.round_rect.topleft = (20, 10)

    def _updateScore_( self ):
        self.score_text = self.font.render("Score: " + str( IGP.GAME_PARAMETERS["Score"] ), True, STF.WHITE)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.centerx = STF.WINDOW_WIDTH//2
        self.score_rect.top = 10

    def _updateLives_( self ):
        self.lives_text = self.font.render("Lives: " + str( IGP.GAME_PARAMETERS["Lives"] ), True, STF.WHITE)
        self.lives_rect = self.lives_text.get_rect()
        self.lives_rect.topright = (STF.WINDOW_WIDTH - 20, 10)
    
    def _updateFinalScore_( self ):
        self.final_score = self.font.render("Your Score: " + str( IGP.GAME_PARAMETERS["Score"] ), True, STF.WHITE)
        self.final_score_rect = self.final_score.get_rect()
        self.final_score_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 - (-0.25)*STF.FONT_SIZE )
        