"""
Created on Wed Mar 9 05:34:00 2022

In this file it will build the main clase of the game

@author: jesus
"""

import pygame
import Game as SKG
import SettingFile as STF
import ImageRegister as IR
import InGame_Parameters as IGP
import LevelMaker
from Player import Player
from Enemy import Zombie
import ScenaryObjects as SCN_OBJ
import Game_HUD


# Custom Events
RUBY_TIMEOUT        = pygame.event.custom_type()
ZOMBI_TIMEOUT       = pygame.event.custom_type()
ONE_SECOND_TIMEOUT  = pygame.event.custom_type() 


class ZombieGame( SKG.Game ):
    
    def __init__( self ):
        # Calling the init method from Base Class
        super().__init__()
        self.game_hud = Game_HUD.GameHUD( self.display_surface )
        
        # Setting Canvas Display to Game Dictionary
        IGP.GAME_PARAMETERS["CanvasGame"] = self.display_surface
        
        # Dictionary with Images
        self.sprite_dictionary = IR.ImageRegister()
        
        # Main Sprites groups for Game
        self.platforms_group    = pygame.sprite.Group()
        self.all_tiles_group    = pygame.sprite.Group()
        self.player_gruop       = pygame.sprite.Group()
        self.enemies_group      = pygame.sprite.Group()
        self.portals_group      = pygame.sprite.Group()
        self.rubi_groups        = pygame.sprite.Group()
        self.bullet_group       = pygame.sprite.Group()
        
        # Assign these sprites to the GroupSprite Dictionary
        IGP.GAME_SPRITES_GROUPS["Tiles_Group"]          = self.all_tiles_group
        IGP.GAME_SPRITES_GROUPS["Platform_Group"]       = self.platforms_group 
        IGP.GAME_SPRITES_GROUPS["Player_Group"]         = self.player_gruop
        IGP.GAME_SPRITES_GROUPS["Enemies_Group"]        = self.enemies_group
        IGP.GAME_SPRITES_GROUPS["Portals_Group"]        = self.portals_group
        IGP.GAME_SPRITES_GROUPS["Rubies_Group"]         = self.rubi_groups
        IGP.GAME_SPRITES_GROUPS["PlayerBullet_Group"]   = self.bullet_group
        
        #Set sounds
        self.lost_ruby_sound = pygame.mixer.Sound("Assets/sounds/lost_ruby.wav")
        self.ruby_pickup_sound = pygame.mixer.Sound("Assets/sounds/ruby_pickup.wav")
        pygame.mixer.music.load("Assets/sounds/level_music.wav")
        
        self.round_time_duration_count = STF.INITIAL_ROUND_TIME
        self.game_over_active = False
        

    def _StartGame_( self ):
        # Create Level        
        self.background_rect = self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ).get_rect()
        self.background_rect.topleft = ( 0, 0 )
    
        level_builder = LevelMaker.LevelMaker(STF.PATH_LEVEL_JSON, self.all_tiles_group, self.platforms_group, self.portals_group, self.sprite_dictionary )
        self.isMapBult = level_builder.IsMapBuilded()
        

        # Create Player
        player_pos = level_builder.GetPlayerPosition()
        player = Player( player_pos[ 0 ]*32 - 32, 
                         player_pos[ 1 ]*32 + 32, 
                         self.sprite_dictionary, 
                         IGP.GAME_SPRITES_GROUPS["Platform_Group"], 
                         IGP.GAME_SPRITES_GROUPS["Portals_Group"],
                         IGP.GAME_SPRITES_GROUPS["PlayerBullet_Group"] )
        self.player = player       
        IGP.GAME_SPRITES_GROUPS["Player_Group"].add( player )
        
        IGP.GAME_PARAMETERS["Rubies_Count"] = 0  
        IGP.GAME_PARAMETERS["Zombies_Count"] = 0 
        
        pygame.time.set_timer( RUBY_TIMEOUT, STF.STANDAR_RUBY_TIME_CREATION )
        pygame.time.set_timer( ZOMBI_TIMEOUT, STF.STANDAR_ZOMBI_TIME_CREATION )
        pygame.time.set_timer( ONE_SECOND_TIMEOUT, 1000 )
        
        self.game_over_active = False
        pygame.mixer.music.play(-1, 0.0)
        
        
    def addRuby( self ):
        
        if IGP.GAME_PARAMETERS["Rubies_Count"] < STF.MAX_RUBIES_ALLOWED:
            ruby = SCN_OBJ.Ruby( self.sprite_dictionary, 
                                    IGP.GAME_SPRITES_GROUPS["Platform_Group"], 
                                    IGP.GAME_SPRITES_GROUPS["Portals_Group"] )
            self.rubi_groups.add( ruby )
            IGP.GAME_PARAMETERS["Rubies_Count"] += 1
        
            
    def addZombie( self ):

        round_number = IGP.GAME_PARAMETERS["Round"] + 3
        if IGP.GAME_PARAMETERS["Zombies_Count"] <= STF.MAX_ZOMBIES_ALLOWED:
            zombi = Zombie( self.sprite_dictionary, 
                           IGP.GAME_SPRITES_GROUPS["Platform_Group"], 
                           IGP.GAME_SPRITES_GROUPS["Portals_Group"],
                           round_number, round_number + 5 )
            self.enemies_group.add( zombi )
            IGP.GAME_PARAMETERS["Zombies_Count"] += 1        
  
        
    def resetGame( self ):
        
        IGP.GAME_PARAMETERS["Score"] = 0
        IGP.GAME_PARAMETERS["Round"] = 1
        
        self.round_time_duration_count = STF.INITIAL_ROUND_TIME


        #Empty sprite groups
        self.player_gruop.empty()
        self.enemies_group.empty()
        self.rubi_groups.empty()
        self.bullet_group.empty()
        self.portals_group.empty()
        self.platforms_group.empty() 
  
    
    def start_new_round( self ):
        
        IGP.GAME_PARAMETERS["Round"] += 1
        self.round_time_duration_count = STF.INITIAL_ROUND_TIME + ( IGP.GAME_PARAMETERS["Round"] - 1 ) * 10

        IGP.GAME_PARAMETERS["Rubies_Count"] = 0  
        IGP.GAME_PARAMETERS["Zombies_Count"] = 0 

        self.enemies_group.empty()
        self.rubi_groups.empty()
        self.bullet_group.empty()

        self.player.reset()
        
        pygame.mixer.music.play(-1, 0.0)
        
    
    def check_GameOver( self ):
        if self.player.health <= 0:
            pygame.mixer.music.stop()
            IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.GAME_OVER_SCREEN
            self.game_over_active = True

    
    def check_RoundCompleted( self ):
        if self.round_time_duration_count <= 0:
            pygame.mixer.music.stop()
            IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.NEXT_ROUND_SCREEN    



    def __UpdateGameState__( self ):
        """
            Update Logic Game each Frame Game. This is the function that the base clase
            Game is executation countinously inside the loop game
        """
        # Fill the display surface to cover old images
        self.display_surface.fill( STF.BLACK )   

        # WRITE HERE LOGIC GAME
        gamestate = IGP.GAME_PARAMETERS["GameState"]
        # Update the game in function of the GameState Current
        self._UpdateGame_InFunctionGameSate_( gamestate )

        # Update Clock Game
        pygame.display.update()
        self.clockGame.tick( STF.FPS )


    def _UpdateGame_InFunctionGameSate_( self, game_state ):
        """Update the game in function of the current state of the game"""
        
        if game_state == IGP.GAME_STATES.INIT_SCREEN:
            self.game_hud.draw_Init_Screen()
        
        if game_state == IGP.GAME_STATES.GAME_OVER_SCREEN:
            self.game_hud.draw_GameOver_Screen()
        
        if game_state == IGP.GAME_STATES.NEXT_ROUND_SCREEN:
            self.game_hud.draw_New_Round_Screen()
            
        if game_state == IGP.GAME_STATES.GAME_RUNNING:
            self._UpdateGame_()
        
        if game_state == IGP.GAME_STATES.GAME_OVER:
            self.resetGame()
            IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.INIT_SCREEN
            
        if game_state == IGP.GAME_STATES.NEXT_ROUND:
            self.start_new_round()
            IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.GAME_RUNNING
        
        if game_state == IGP.GAME_STATES.MOVE_2_START:
            self._StartGame_()
            IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.GAME_RUNNING
        

    
    def _UpdateGame_( self ):
        """Update the Game Logic when the state is RUNNING"""

        # Fill the display surface to cover old images
        self.display_surface.blit( self.sprite_dictionary.GetSprite( IR.Levels_Sprites_Types.BACKGROUND_IMAGE ), self.background_rect )           

        #Draw tiles and Update Tiles
        self.all_tiles_group.draw( self.display_surface )
        self.all_tiles_group.update()

        # Draw and Update Player
        self.player_gruop.update()
        self.player_gruop.draw( self.display_surface )
        
        # Draw and Update Bullet Player
        self.bullet_group.update()
        self.bullet_group.draw( self.display_surface )
        
        # Draw and Update Rubies
        self.enemies_group.update()
        self.enemies_group.draw( self.display_surface )
        
        # Draw and Update Portals
        self.portals_group.update()
        self.portals_group.draw( self.display_surface )

        # Draw and Update Rubies
        self.rubi_groups.update()
        self.rubi_groups.draw( self.display_surface )
        
        # CheckCollision
        self._CheckCollisions_()
        
        
        self.check_GameOver()
        
        # Update Game HUD
        self.game_hud.draw_HUB_GameScreen( self.player.health, self.round_time_duration_count )
        
    
    
    def _CheckCollision_Player_Ruby_( self ):
        
        #See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.player, self.rubi_groups, True):
            self.ruby_pickup_sound.play()
            IGP.GAME_PARAMETERS["Score"] += 100
            IGP.GAME_PARAMETERS["Rubies_Count"] -= 1
            self.player.increase_health( 10 )
            
    
    def _CheckCollision_Enemy_Ruby_( self ):
        #See if a living zombie collided with a ruby
        for zombie in self.enemies_group:
            if zombie.is_dead == True:
                if pygame.sprite.spritecollide(zombie, self.rubi_groups, True):
                    self.lost_ruby_sound.play()
                    # zombie = Zombie(self.platform_group, self.portal_group, self.round_number, 5 + self.round_number)
                    # self.zombie_group.add(zombie)
                    IGP.GAME_PARAMETERS["Rubies_Count"] -= 1
                    zombie.rise_zombie()
    
    
    def _CheckCollision_Bullet_Zombie_( self ):
        #See if any bullet in the bullet group hit a zombie in the zombie group
        collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.enemies_group, True, False)
        if collision_dict:
            for zombies in collision_dict.values():
                for zombie in zombies:
                    zombie.hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True
                    
    
    def _CheckCollision_Player_Zombie_( self ):
        #See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        if self.player.invulnerability == False:
            collision_list = pygame.sprite.spritecollide(self.player, self.enemies_group, False)
            if collision_list:
                for zombie in collision_list:
                    
                    #The zombie is dead; stomp it
                    if zombie.is_dead == True:
                        # zombie.kick_sound.play()
                        zombie.kill(); IGP.GAME_PARAMETERS["Zombies_Count"] -= 1
                        IGP.GAME_PARAMETERS["Score"] += 25
                        self.addRuby()
                    #The zombie isn't dead, so take damage
                    else:
                        self.player.hit_received()
                        
        else:    
        # About 30 Frames the player will not received any damage --> Avoid Instant kill multiple collision
            self.player.invulnerability_count += 1
            if( self.player.invulnerability_count > 30 ):
                self.player.invulnerability_count = 0
                self.player.invulnerability = False
            
    
    def _CheckCollisions_( self ):
        
        self._CheckCollision_Bullet_Zombie_()
        self._CheckCollision_Player_Zombie_()
        self._CheckCollision_Player_Ruby_()
        self._CheckCollision_Enemy_Ruby_()
        
    def _Checking_Rising_Zombie_( self ):
        for zombie in self.enemies_group:
            zombie.check_rise_timeout()
        
    
    def _CheckingEvents_( self ):
        """Checking Player Events"""
        # Loop through a list of Event Objects that have occured
        for event in pygame.event.get():
            # print( event )
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                #Player wants to jump
                if event.key == pygame.K_SPACE:
                    self.player.fire() 
                #Player wants to fire
                if event.key == pygame.K_UP:
                    self.player.jump()
        
                # Moving from Screen State to other Game State
                if event.key == pygame.K_RETURN:                    
                    gamestate = IGP.GAME_PARAMETERS["GameState"]                    
                    if gamestate == IGP.GAME_STATES.INIT_SCREEN:
                        IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.MOVE_2_START
                        
                    if gamestate == IGP.GAME_STATES.GAME_OVER_SCREEN:
                        IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.GAME_OVER
                        
                    if gamestate == IGP.GAME_STATES.NEXT_ROUND_SCREEN:
                        IGP.GAME_PARAMETERS["GameState"] = IGP.GAME_STATES.NEXT_ROUND
                
            if event.type == RUBY_TIMEOUT:
                self.addRuby()
            
            if event.type == ZOMBI_TIMEOUT:
                    self.addZombie()
            
            if event.type == ONE_SECOND_TIMEOUT:
                    self.round_time_duration_count -= 1
                    if self.game_over_active == False:
                        self.check_RoundCompleted()
                    self._Checking_Rising_Zombie_()
                    
                        
   
my_game = ZombieGame();     my_game.RunGame()



