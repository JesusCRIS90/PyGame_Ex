"""
Created on Sat Feb 19 12:52:55 2022

This class is the blueprint for the Space Invader HUB representation in the game

@author: jesus
"""

import pygame
import SettingFile as STF
# from enum import Enum, unique, IntEnum
import InGame_Parameters as IGP


# """ ENUMS """
# @unique
# class GAME_STATES( IntEnum ):
#     RUNNING         = 0
#     GAME_OVER       = 1
#     INIT            = 2

# """
#     Dictionary with main parameters of game
# """
# GAME_PARAMETERS = {
#     "Round": 1,
#     "GameState": GAME_STATES.INIT
# }


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



    def update( self ):
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.INIT:
            self.draw_Init_Screen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.GAME_OVER:
            self.draw_GameOver_Screen()
        if IGP.GAME_PARAMETERS["GameState"] == IGP.GAME_STATES.RUNNING:
            self.draw_GameScreen()
            
                
    def draw_GameOver_Screen( self ):
        self.surface_display.blit( self.game_over_text, self.game_over_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )
    
    def draw_Init_Screen( self ):
        self._updateRoundNumber_()
        self.surface_display.blit( self.game_title, self.game_title_rect )
        self.surface_display.blit( self.round_text, self.round_rect )
        self.surface_display.blit( self.continue_text, self.continue_rect )

    def draw_GameScreen( self ):
        "Update the Game HUB Screen"
        pass

    def _updateRoundNumber_( self ):
        self.round_text = self.font.render("Round: " + str( IGP.GAME_PARAMETERS["Round"] ), True, STF.WHITE )
        self.round_rect = self.round_text.get_rect()
        self.round_rect.center = ( STF.WINDOW_WIDTH//2, STF.WINDOW_HEIGHT//2 + 0*STF.FONT_SIZE )


        