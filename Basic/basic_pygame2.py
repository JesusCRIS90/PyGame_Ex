#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:36:58 2021

@author: jesus
"""

import pygame

"CONSTANTS"  
WINDOW_WIDTH    = 600
WINDOW_HEIGHT   = 600


BLACK       = ( 0, 0, 0 )
WHITE       = ( 255, 255, 255 )
RED         = ( 255, 0, 0 )
GREEN       = ( 0, 255, 0 )
DARKGREEN   = ( 10, 50, 10)
BLUE        = ( 0, 0, 255 )
YELLOW      = ( 255, 255, 0 )
CYAN        = ( 0, 255, 255 )
MAGENTA     = ( 255, 0, 255 )



# Initialize pygame
pygame.init()


dislay_surface = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("Hello World - Images")


# Filling Background with a color
dislay_surface.fill( BLACK )

# Loading Images
dragon_left_image = pygame.image.load( "Assets/dragon_left.png" )
dragon_left_rect  = dragon_left_image.get_rect()
dragon_left_rect.topleft = ( 0, 0 )


dragon_right_image = pygame.image.load( "Assets/dragon_right.png" )
dragon_right_rect  = dragon_right_image.get_rect()
dragon_right_rect.topright = ( WINDOW_WIDTH, 0 )

# Define New font, text and color
custom_font = pygame.font.Font("Assets/AttackGraffiti.ttf", 64)

splash_text = custom_font.render("Dragons Ruls!", True, DARKGREEN)
splash_text_rect = splash_text.get_rect()
splash_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100)

# Load and play Music and Effects
End_sound = pygame.mixer.Sound( "Assets/sound_2.wav" )
End_sound.set_volume(0.1)
Background_Music = pygame.mixer_music.load( "Assets/music.wav" )

pygame.mixer.music.play( -1 )


# The main game loop
running = True
while running:
    # Loop through a list of Event Objects that have occured
    for event in pygame.event.get():
        print( event )
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
            End_sound.play()
            pygame.time.delay( 1000 )
            
            
    # Drawing Images and Text in Surface
    dislay_surface.blit(dragon_left_image, dragon_left_rect )
    dislay_surface.blit(dragon_right_image, dragon_right_rect )
    
    dislay_surface.blit(splash_text, splash_text_rect )
            
    pygame.display.update()

# End the game
pygame.quit()