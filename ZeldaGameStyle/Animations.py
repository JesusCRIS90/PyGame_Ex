
import pygame
from ImageRegister import *
from pygame.math import Vector2
from enum import unique, IntEnum

@unique
class Entity_States( IntEnum ):
    IDLE            = 1001
    ATTACKING       = 1002
    MOVING          = 1003

@unique
class Player_See_Directions( IntEnum ):
    UP          = 1010
    DOWN        = 1011
    LEFT        = 1012
    RIGHT       = 1013

class Animations():
    
    def __init__( self ) -> None:
        self.direction = Vector2()
        self.inputType = Entity_States.IDLE
        self.SeeDirection = Player_See_Directions.DOWN
        
        self.frame_index = 0
        self.animation_speed = 0.15

    def animate( self, direction:Vector2, inputType:Entity_States ):
        
        self.setState( direction, inputType )
        animations_list = self.Get_AnimationList()

        "Loop over animations_list"
        self.frame_index += self.animation_speed
        if self.frame_index >= len( animations_list ):
            self.frame_index = 0

        return animations_list[ int( self.frame_index ) ]
        
    def setState( self, direction:Vector2, inputType:Entity_States ):
        self.direction = direction
        self.inputType = inputType
        self.UpdateSeeDirection()

    def UpdateSeeDirection( self ):
        
        if self.direction.x == 1 and self.direction.y == 0:
            self.SeeDirection = Player_See_Directions.RIGHT  
        
        if self.direction.x == -1 and self.direction.y == 0:
            self.SeeDirection = Player_See_Directions.LEFT  

        if self.direction.x == 0 and self.direction.y == 1:
            self.SeeDirection = Player_See_Directions.DOWN  

        if self.direction.x == 0 and self.direction.y == -1:
            self.SeeDirection = Player_See_Directions.UP  

    def Get_AnimationList( self ):

        
        if self.inputType == Entity_States.IDLE:
            
            if self.SeeDirection == Player_See_Directions.UP:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_UP_IDLE )
            
            if self.SeeDirection == Player_See_Directions.DOWN:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_DOWN_IDLE )
            
            if self.SeeDirection == Player_See_Directions.LEFT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_LEFT_IDLE )
            
            if self.SeeDirection == Player_See_Directions.RIGHT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_RIGHT_IDLE )        

        if self.inputType == Entity_States.ATTACKING:
            
            if self.SeeDirection == Player_See_Directions.UP:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_UP_ATTACK )
            
            if self.SeeDirection == Player_See_Directions.DOWN:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_DOWN_ATTACK )
            
            if self.SeeDirection == Player_See_Directions.LEFT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_LEFT_ATTACK )
            
            if self.SeeDirection == Player_See_Directions.RIGHT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_RIGHT_ATTACK )

        if self.inputType == Entity_States.MOVING:
            
            if self.SeeDirection == Player_See_Directions.UP:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_UP_MOVE )
            
            if self.SeeDirection == Player_See_Directions.DOWN:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_DOWN_MOVE )
            
            if self.SeeDirection == Player_See_Directions.LEFT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_LEFT_MOVE )
            
            if self.SeeDirection == Player_See_Directions.RIGHT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_RIGHT_MOVE )

    def Get_SeeDirection( self ):
        return self.SeeDirection