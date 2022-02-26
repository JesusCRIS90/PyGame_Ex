"""
Created on Sat Feb 19 13:15:49 2022

This class is a specialization of the class Base Game.

@author: jesus
"""

import pygame
import Game as SKG
import SettingFile as STF
import Game_HUD
import InGame_Parameters as IGP
import Player

class SpaceInvader( SKG.Game ):

    def __init__( self ):
    # Calling the init method from Base Class
        super().__init__()
        self.game_hud = Game_HUD.GameHUD( self.display_surface )
        self.__CreatePlayer__()
        

    def __CreatePlayer__( self ):
        self.player_bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group( )
        self.player = Player.Player( self.player_bullet_group )
        self.player_group.add( self.player )


    def __UpdateGameState__( self ):
        
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.BLACK )   

        # WRITE HERE LOGIC GAME
        gamestate = IGP.GAME_PARAMETERS["GameState"]
        if gamestate == IGP.GAME_STATES.RUNNING:
            self._UpdatePlayer_()
            self._UpdatePlayerBullet_()


        self.game_hud.update()

        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )

    def _UpdatePlayer_( self ):
        self.player_group.update()
        self.player_group.draw( self.display_surface )
    
    def _UpdatePlayerBullet_( self ):
        self.player_bullet_group.update()
        self.player_bullet_group.draw( self.display_surface )


    def _CheckingEvents_( self ):
        # Loop through a list of Event Objects that have occured
        for event in pygame.event.get():
            # print( event )
            if event.type == pygame.QUIT:
                self.running = False
            
            # Change GameState
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RETURN:
                gamestate = IGP.GAME_PARAMETERS["GameState"]
                if ( gamestate == IGP.GAME_STATES.GAME_OVER ) or ( gamestate == IGP.GAME_STATES.INIT ):
                    IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.RUNNING
            
            #The player wants to fire
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamestate = IGP.GAME_PARAMETERS["GameState"]
                    if gamestate == IGP.GAME_STATES.RUNNING:
                        self.player.fire()
    


my_game = SpaceInvader(); my_game.RunGame()