
"""

In this file we make the definition of all Setting for the game

"""

import SettingFile as STS
import pygame
import random
    
def moveUp( rect2move ):
    rect2move.y -= STS.PLAYER_VELOCITY
    
def moveDown( rect2move ):
    rect2move.y += STS.PLAYER_VELOCITY
    
def Move_Player( rect2move, key_event:pygame.event = None, press_button:pygame.key = None ):

    # if key_event != None:
    #     if ( key_event.key == pygame.K_LEFT ) and rect2move.left > 0:
    #         moveLeft( rect2move, moveInverse )
        
    #     if key_event.key == pygame.K_RIGHT and rect2move.right < WINDOW_WIDTH:
    #         moveRigth( rect2move, moveInverse )
            
    #     if key_event.key == pygame.K_UP and rect2move.top > 0:
    #         moveUp( rect2move )
            
    #     if key_event.key == pygame.K_DOWN and rect2move.bottom < WINDOW_HEIGHT:
    #         moveDown( rect2move )
        
    #     return
    
    if press_button != None:
        
        if press_button[ pygame.K_UP ] and rect2move.top > 64:
            moveUp( rect2move )
            
        if press_button[ pygame.K_DOWN ] and rect2move.bottom < STS.WINDOW_HEIGTH:
            moveDown( rect2move )
        
        return
    
def Move_Coin( coin_rect:pygame.rect.Rect,  player_lives, coin_velocity, coin_sound:pygame.mixer.Sound = None ):
    
    # Player miss the coin
    if coin_rect.x < 0:
        player_lives -= 1
        if player_lives <= 0:
            player_lives = 0
        coin_sound.play()
        Reset_Coin_Position( coin_rect )
    else:
        coin_rect.x -= coin_velocity
    
    return player_lives

def Reset_Coin_Position( coin_rect:pygame.rect.Rect ):
    coin_rect.x = STS.WINDOW_WIDTH + STS.BUFFER_DISTANCE
    coin_rect.y = random.randint( 64, STS.WINDOW_HEIGTH - 32 )

def Update_HUD( score, player_lives ):

    pass









