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
import Enemies

class SpaceInvader( SKG.Game ):

    def __init__( self ):
    # Calling the init method from Base Class
        super().__init__()
        self.game_hud = Game_HUD.GameHUD( self.display_surface )
        # self.__CreatePlayer__()
        

    def __CreatePlayer__( self ):
        self.player_bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group( )
        self.player = Player.Player( self.player_bullet_group )
        self.player_group.add( self.player )

    def __CreateEnemies__( self ):
        self.alien_bullet_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        #Create a grid of Aliens 11 columns and 5 rows.  
        for i in range(11):
            for j in range(5):
                alien = Enemies.Alien( 64 + i*64, 64 + j*64, 
                                      IGP.GAME_PARAMETERS["Round"],
                                      self.alien_bullet_group )
                self.alien_group.add( alien )

    def __UpdateGameState__( self ):
        
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.BLACK )   

        # WRITE HERE LOGIC GAME
        gamestate = IGP.GAME_PARAMETERS["GameState"]
        # if gamestate == IGP.GAME_STATES.RUNNING:
        #     self._UpdatePlayer_()
        #     self._UpdatePlayerBullet_()


        # self.game_hud.update()

        self._UpdateGame_InFunctionGameSate_( gamestate )

        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )

    def _UpdatePlayer_( self ):
        self.player_group.update()
        self.player_group.draw( self.display_surface )
    
    def _UpdatePlayerBullet_( self ):
        self.player_bullet_group.update()
        self.player_bullet_group.draw( self.display_surface )
    
    def _UpdateEnemies_( self ):
        """Update the Enemies"""
        # self.shift_aliens()
        self.alien_group.update()
        self.alien_group.draw( self.display_surface )
    
    def _UpdateEnemiesBullet_( self ):
        self.alien_bullet_group.update()
        self.alien_bullet_group.draw( self.display_surface )
    

    def _UpdateGame_InFunctionGameSate_( self, game_state ):
        if game_state == IGP.GAME_STATES.INIT:
            self.game_hud.draw_Init_Screen()
        if game_state == IGP.GAME_STATES.RUNNING:
            self._UpdateGame_()
        if game_state == IGP.GAME_STATES.GAME_OVER:
            self.game_hud.draw_GameOver_Screen()
        if game_state == IGP.GAME_STATES.MOVE2RUNNING:
            self._CreateNewRound_()
        if game_state == IGP.GAME_STATES.MOVE2GAMEOVER:
            self._FinalizeGame_()

    def _CreateNewRound_( self ):
        self._Reset_Game_()
        self.__CreatePlayer__()
        self.__CreateEnemies__()
        IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.RUNNING


    def _FinalizeGame_( self ):
        pass
    
    def _UpdateGame_( self ):
        # Update Player
        self._UpdatePlayer_()
        self._UpdatePlayerBullet_()
        # Update Enemies
        self._UpdateEnemies_()
        self._UpdateEnemiesBullet_()

        # Update Game HUD
        self.game_hud.update()

    def _Reset_Game_( self ):
        pass

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
                if gamestate == IGP.GAME_STATES.INIT:
                    IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.MOVE2RUNNING
                if gamestate == IGP.GAME_STATES.GAME_OVER:
                    IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.INIT
            
            #The player wants to fire
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamestate = IGP.GAME_PARAMETERS["GameState"]
                    if gamestate == IGP.GAME_STATES.RUNNING:
                        self.player.fire()
    


my_game = SpaceInvader(); my_game.RunGame()