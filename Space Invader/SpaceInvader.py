"""
Created on Sat Feb 19 13:15:49 2022

This class is a specialization of the class Base Game.

@author: jesus
"""

import pygame
import Game as SKG
import SettingFile as STF
import Game_HUD


class SpaceInvader( SKG.Game ):

    def __init__( self ):
    # Calling the init method from Base Class
        super().__init__()
        self.game_hud = Game_HUD.GameHUD( self.display_surface )

    def __UpdateGameState__( self ):
        
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.BLACK )   

        # WRITE HERE LOGIC GAME
        self.game_hud.update()

        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )


    def _CheckingEvents_( self ):
        # Loop through a list of Event Objects that have occured
        for event in pygame.event.get():
            # print( event )
            if event.type == pygame.QUIT:
                self.running = False
    


my_game = SpaceInvader(); my_game.RunGame()