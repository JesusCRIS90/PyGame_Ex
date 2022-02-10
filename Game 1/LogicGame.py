# -*- coding: utf-8 -*-
"""

In this file we make the definition of all Setting for the game

"""

import SettingFile as settings
import pygame
import random

# Init pygame
pygame.init()


# Set display surface
display_surface = pygame.display.set_mode( (settings.WINDOW_WIDTH, settings.WINDOW_HEIGTH) )
pygame.display.set_caption( settings.GAME_NAME )


# Set clock speed
clock = pygame.time.Clock()

# Set game values
score = 0
player_lives = settings.PLAYER_STARTING_LIVES
coin_velocity = settings.COINS_STARTING_VELOCITY

# Set Font
font = pygame.font.Font( settings.FONT_FILE, settings.FONT_SIZE )

# Set Text
score_text = font.render( "Score: " +  str( score ), True, settings.GREEN, settings.BLACK )
score_rect = score_text.get_rect()
score_rect.topleft = ( 10, 10 )

tittle_text = font.render( settings.GAME_NAME, True, settings.GREEN, settings.BLACK )
tittle_rect = tittle_text.get_rect()
tittle_rect.centerx = settings.WINDOW_WIDTH // 2
tittle_rect.y = 10

lives_text = font.render( "Lives: " +  str( player_lives ), True, settings.GREEN, settings.BLACK )
lives_rect = lives_text.get_rect()
lives_rect.topright = ( settings.WINDOW_WIDTH - 10, 10 )

gameover_text = font.render( "GAME OVER", True, settings.GREEN, settings.BLACK )
gameover_rect = gameover_text.get_rect()
gameover_rect.topleft = ( settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGTH // 2 )

continue_text = font.render( "Press any key to play the game", True, settings.GREEN, settings.BLACK )
continue_rect = continue_text.get_rect()
continue_rect.topleft = ( settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGTH // 2 + 32 )


# Set Sounds and Music
coin_sound = pygame.mixer.Sound( settings.COIN_SOUND )
miss_sound = pygame.mixer.Sound( settings.MISS_SOUND ); miss_sound.set_volume(.1)
pygame.mixer.music.load( settings.BACKGROUND_MUSIC )

# Set the images
player_image = pygame.image.load( settings.PLAYER_IMAGE )
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = settings.WINDOW_HEIGTH // 2

coin_image = pygame.image.load( settings.COIN_IMAGE )
coin_rect = coin_image.get_rect()
coin_rect.x = settings.WINDOW_WIDTH + settings.BUFFER_DISTANCE
coin_rect.y = random.randint( 64, settings.WINDOW_HEIGTH - 32 )


# Main Loop Game
running = True
while running:
    
    # Checking user force exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # Fill the display surface to cover old images
    display_surface.fill( settings.BLACK )    
        
    # Blit the HUD to screen
    display_surface.blit( score_text, score_rect )
    display_surface.blit( tittle_text, tittle_rect )
    display_surface.blit( lives_text, lives_rect )
    pygame.draw.line( display_surface, settings.WHITE, (0, 64), ( settings.WINDOW_WIDTH, 64 ), 2 )    
    
    # Blit Asset to screen
    display_surface.blit( player_image, player_rect )
    display_surface.blit( coin_image, coin_rect )
            
    # Update display and tick the clock
    pygame.display.update()
    clock.tick( settings.FPS )
    
    

# End of the game
pygame.quit()

