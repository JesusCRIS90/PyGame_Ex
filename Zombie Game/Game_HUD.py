"""
Created on Sat Feb 19 12:52:55 2022

This class is the blueprint for the ZombieGame HUB representation in the game

@author: jesus
"""

import pygame
import SettingFile as STF
import InGame_Parameters as IGP


class GameHUD():
    
    def __init__( self, surf_disp:pygame.display ):
        
        self.surface_display = surf_disp        
        
        #Set fonts
        self.title_font = pygame.font.Font("Assets/fonts/Poultrygeist.ttf", 60)
        self.HUD_font = pygame.font.Font("Assets/fonts/Pixel.ttf", 30)
        
        
        # Fixed Messages
        self.game_title = self.title_font.render( STF.GAME_NAME , True, STF.GREEN )
        self.game_title_rect = self.game_title.get_rect()
        self.game_title_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 - 1*STF.FONT_SIZE )

        self.continue_text = self.HUD_font.render("Press 'Enter' key to play", True, STF.WHITE )
        self.continue_rect = self.continue_text.get_rect()
        self.continue_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 + 1*STF.FONT_SIZE )
        
        # Text for GameOver and Reset Screen
        self.game_over_text = self.HUD_font.render("GAME OVER", True, STF.WHITE )
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 - 1*STF.FONT_SIZE )
        
        self.round_completed_text = self.HUD_font.render("You have survived", True, STF.WHITE )
        self.round_completed_text_rect = self.round_completed_text.get_rect()
        self.round_completed_text_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 - 1*STF.FONT_SIZE )



    def update( self, health:int = 100, time_remain:int = 0 ):
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.INIT:
            self.draw_Init_Screen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.GAME_OVER:
            self.draw_GameOver_Screen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.RUNNING:
            self.draw_GameScreen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.LOAD_NEW_ROUND:
            self.draw_New_Round_Screen()
                
    def draw_GameOver_Screen( self ):
        self._updateFinalScore_()
        self.surface_display.blit( self.game_over_text, self.game_over_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )
        self.surface_display.blit( self.final_score, self.final_score_rect )


    def draw_Init_Screen( self ):
        # self._updateRoundNumber_()
        self.surface_display.blit( self.game_title, self.game_title_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )


    def draw_New_Round_Screen( self ):
        self.surface_display.blit( self.round_completed_text, self.round_completed_text_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )


    def draw_HUB_GameScreen( self, health:int, time_remain:int ):
        "Update the Game HUB Screen"
        self._updateScore_()
        self._updateLives_( health )
        self._updateRoundNumber_()
        self._update_RoundTime_( time_remain )
        self.surface_display.blit( self.score_text, self.score_rect )
        self.surface_display.blit( self.lives_text, self.lives_rect )
        self.surface_display.blit( self.round_text, self.round_rect )
        self.surface_display.blit( self.round_time_text, self.round_time_text_rect )
        


    def _updateScore_( self ):
        self.score_text = self.HUD_font.render("Score: " + str( IGP.GAME_PARAMETERS["Score"] ), True, STF.WHITE)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = ( STF.WINDOW_WIDTH - 150, STF.WINDOW_HEIGHT - 20 )
        
    def _updateLives_( self, health:int ):
        self.lives_text = self.HUD_font.render("Health: " + str( health ), True, STF.WHITE)
        self.lives_rect = self.lives_text.get_rect()
        self.lives_rect.center = ( 150, STF.WINDOW_HEIGHT - 20 )
        
    def _updateRoundNumber_( self ):
        self.round_text = self.HUD_font.render("Round: " + str( IGP.GAME_PARAMETERS["Round"] ), True, STF.WHITE )
        self.round_rect = self.round_text.get_rect()
        self.round_rect.center = ( STF.WINDOW_WIDTH//2, 30 )

    def _update_RoundTime_( self, time_remain ):
        self.round_time_text = self.HUD_font.render("Round End: " + str( time_remain ), True, STF.WHITE)
        self.round_time_text_rect = self.round_time_text.get_rect()
        self.round_time_text_rect.centerx = STF.WINDOW_WIDTH//2
        self.round_time_text_rect.top = 50
        

    def _updateFinalScore_( self ):
        self.final_score = self.HUD_font.render("Your Score: " + str( IGP.GAME_PARAMETERS["Score"] ), True, STF.WHITE)
        self.final_score_rect = self.final_score.get_rect()
        self.final_score_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 + 3*STF.FONT_SIZE )
        