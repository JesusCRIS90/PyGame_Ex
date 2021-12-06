#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:20:32 2021

@author: jesus
"""

import pygame
import math 

"CONSTANTS"  
WINDOW_WIDTH    = 600
WINDOW_HEIGHT   = 600

CENTER_WINDOW = ( WINDOW_WIDTH//2, WINDOW_HEIGHT//2 )

ANGLE = math.pi/6; CIRCLE_RADIOUS = 200
END_POINT_LINE = ( CENTER_WINDOW[ 0 ] + CIRCLE_RADIOUS*math.cos( ANGLE ), 
                   CENTER_WINDOW[ 1 ] + CIRCLE_RADIOUS*math.sin( ANGLE ) )


BLACK       = ( 0, 0, 0 )
WHITE       = ( 255, 255, 255 )
RED         = ( 255, 0, 0 )
GREEN       = ( 0, 255, 0 )
BLUE        = ( 0, 0, 255 )
YELLOW      = ( 255, 255, 0 )
CYAN        = ( 0, 255, 255 )
MAGENTA     = ( 255, 0, 255 )



# Initialize pygame
pygame.init()


dislay_surface = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("Hello World")


# Filling Background with a color
dislay_surface.fill( WHITE )


# Drawing basic shapes
pygame.draw.line(dislay_surface, RED, CENTER_WINDOW, END_POINT_LINE, 5)
pygame.draw.circle(dislay_surface, BLUE, CENTER_WINDOW, CIRCLE_RADIOUS, 6)
# pygame.draw.rect(dislay_surface, GREEN, ( 500, 150, 50, 100 ) )


# The main game loop
running = True
while running:
    # Loop through a list of Event Objects that have occured
    for event in pygame.event.get():
        print( event )
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()

# End the game
pygame.quit()