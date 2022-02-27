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

        #Set sounds and music
        self.new_round_sound = pygame.mixer.Sound("Assets/new_round.wav")
        self.breach_sound = pygame.mixer.Sound("Assets/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("Assets/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("Assets/player_hit.wav")
        
    # Create SpriteGroup
        self.player_bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group( )        

        self.alien_bullet_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()


    def __CreatePlayer__( self ):
        # self.player_bullet_group = pygame.sprite.Group()
        # self.player_group = pygame.sprite.Group( )
        self.player = Player.Player( self.player_bullet_group )
        self.player_group.add( self.player )

    def __CreateEnemies__( self ):
        # self.alien_bullet_group = pygame.sprite.Group()
        # self.alien_group = pygame.sprite.Group()
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
        self._ShiftAliens_()
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
            self._InitilizeGame_()
        if game_state == IGP.GAME_STATES.MOVE2GAMEOVER:
            self._FinalizeGame_()

    def _InitilizeGame_( self ):
        self._Reset_Game_()
        self.__CreatePlayer__()
        self.__CreateEnemies__()
        IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.RUNNING
    
    def CreateNewRound_( self ):
        pass

    def _ShiftAliens_( self ):
        """Shift a wave of aliens down the screen and reverse direction"""
        #Determine if alien group has hit an edge
        shift = False
        for alien in ( self.alien_group.sprites() ):
            if alien.rect.left <= 0 or alien.rect.right >= STF.WINDOW_WIDTH:
                shift = True
        #Shift every alien down, change direction, and check for a breach
        if shift:
            breach = False
            for alien in ( self.alien_group.sprites() ):
                #Shift down
                alien.rect.y += 10 * IGP.GAME_PARAMETERS["Round"]
                #Reverse the direction and move the alien off the edge so 'shift' doesn't trigger
                alien.direction = -1*alien.direction
                alien.rect.x += alien.direction*alien.velocity
                #Check if an alien reached the ship
                if alien.rect.bottom >= STF.WINDOW_HEIGHT - 100:
                    breach = True
            
            #Aliens breached the line
            if breach:
                self.breach_sound.play()
                # self.player.lives = 0
                IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.GAME_OVER
                # self.check_game_status("Aliens breached the line!", "Press 'Enter' to continue")

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
        
        # Reset game values
        IGP.GAME_PARAMETERS["Score"] = 0
        IGP.GAME_PARAMETERS["Round"] = 1
        IGP.GAME_PARAMETERS["Lives"] = 5

        # Empty groups
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.player_group.empty()

        # Move GameState to MOVE2RUNNING
        IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.MOVE2RUNNING
        

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