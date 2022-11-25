import pygame
import SettingFile as STF
from pygame.sprite import Group
from ImageRegister import *
import InGame_Parameters as IGP
from pygame.math import Vector2
from debug import *

from enum import unique, IntEnum


@unique
class Player_Inputs_Types( IntEnum ):
    IDLE            = 1001
    ATTACKING       = 1002
    MOVING          = 1003

@unique
class Player_See_Directions( IntEnum ):
    UP          = 1010
    DOWN        = 1011
    LEFT        = 1012
    RIGHT       = 1013

class PyGameTimer():

    def __init__( self, elapsedTime:int ) -> None:
        self.time_init = None
        self.elapsedTime = 100
        self.Set_elapsedTime( elapsedTime )

    def Set_elapsedTime( self, elapsedTime:int ):
        if elapsedTime > 0:
            self.elapsedTime = elapsedTime
        return self

    def Start( self ):
        self.time_init = pygame.time.get_ticks()
        pass

    def ElapsedTime_Reach( self ):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.time_init >= self.elapsedTime:
            return True
        else:
            return False

class Animations():
    
    def __init__( self ) -> None:
        self.direction = Vector2()
        self.inputType = Player_Inputs_Types.IDLE
        self.SeeDirection = Player_See_Directions.DOWN
        
        self.frame_index = 0
        self.animation_speed = 0.15


    def animate( self, direction:Vector2, inputType:Player_Inputs_Types ):
        
        self.setState( direction, inputType )
        animations_list = self.Get_AnimationList()

        "Loop over animations_list"
        self.frame_index += self.animation_speed
        if self.frame_index >= len( animations_list ):
            self.frame_index = 0

        return animations_list[ int( self.frame_index ) ]
        
        
    def setState( self, direction:Vector2, inputType:Player_Inputs_Types ):
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
        
        if self.inputType == Player_Inputs_Types.IDLE:
            
            if self.SeeDirection == Player_See_Directions.UP:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_UP_IDLE )
                #return "UP_IDLE"
            
            if self.SeeDirection == Player_See_Directions.DOWN:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_DOWN_IDLE )
                #return "DOWN_IDLE"
            
            if self.SeeDirection == Player_See_Directions.LEFT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_LEFT_IDLE )
                #return "LEFT_IDLE"
            
            if self.SeeDirection == Player_See_Directions.RIGHT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_RIGHT_IDLE )
                #return "RIGHT_IDLE"            


        if self.inputType == Player_Inputs_Types.ATTACKING:
            
            if self.SeeDirection == Player_See_Directions.UP:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_UP_ATTACK )
                #return "UP_ATTACK"
            
            if self.SeeDirection == Player_See_Directions.DOWN:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_DOWN_ATTACK )
                #return "DOWN_ATTACK"
            
            if self.SeeDirection == Player_See_Directions.LEFT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_LEFT_ATTACK )
                #return "LEFT_ATTACK"
            
            if self.SeeDirection == Player_See_Directions.RIGHT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_RIGHT_ATTACK )
                #return "RIGHT_ATTACK"


        if self.inputType == Player_Inputs_Types.MOVING:
            
            if self.SeeDirection == Player_See_Directions.UP:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_UP_MOVE )
                #return "UP_MOVE"
            
            if self.SeeDirection == Player_See_Directions.DOWN:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_DOWN_MOVE )
                #return "DOWN_MOVE"
            
            if self.SeeDirection == Player_See_Directions.LEFT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_LEFT_MOVE )
                #return "LEFT_MOVE"
            
            if self.SeeDirection == Player_See_Directions.RIGHT:
                return ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_RIGHT_MOVE )
                #return "RIGHT_MOVE"




class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups:Group, enum_sprite, obstacle:Group ) -> None:
        super().__init__( groups )
        self.image = None
        self.rect = None
        self.hitbox = None

        self.Timer = PyGameTimer( STF.ELAPSED_PLAYER_ATTACK_TIME )

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.attacking = False

        self.obstacle_sprites = obstacle

        self.inputType = Player_Inputs_Types.IDLE
        self.animations = Animations()

        if enum_sprite == Player_Sprites_Types.PLAYER_TEST:
            self.image = ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_TEST )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, -26 )

    def input( self ):
        
        self.inputType = Player_Inputs_Types.IDLE
        keys = pygame.key.get_pressed()
        
        if self.attacking:
            self.inputType = Player_Inputs_Types.ATTACKING
            self.direction.y = 0; self.direction.x = 0
            return

        "Moving Inputs"
        if keys[ pygame.K_UP ]:
            self.direction.y = -1;  self.inputType = Player_Inputs_Types.MOVING
        elif keys[ pygame.K_DOWN ]:
            self.direction.y = 1;   self.inputType = Player_Inputs_Types.MOVING
        else:
            self.direction.y = 0

        if keys[ pygame.K_RIGHT ]:
            self.direction.x = 1;   self.inputType = Player_Inputs_Types.MOVING
        elif keys[ pygame.K_LEFT ]:
            self.direction.x = -1;  self.inputType = Player_Inputs_Types.MOVING
        else:
            self.direction.x = 0

        """" Attacking Inputs """
        if keys[ pygame.K_SPACE ] and not self.attacking:
            self.attacking = True
            self.inputType = Player_Inputs_Types.ATTACKING
            self.Timer.Start()
            print("Attack")

        if keys[ pygame.K_LCTRL ] and not self.attacking:
            self.attacking = True
            self.inputType = Player_Inputs_Types.ATTACKING
            self.Timer.Start()
            print("Magic")

    def move( self, speed ):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision( 'horizontal' )
        self.hitbox.y += self.direction.y * speed
        self.collision( 'vertical' )
        self.rect.center = self.hitbox.center
        
    
    def collision( self, direction ):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect( self.hitbox ):
                    if self.direction.x > 0:        # Moving Right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:        # Moving Left
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect( self.hitbox ):
                    if self.direction.y > 0:        # Moving Down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:        # Moving Up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns( self ):
        if self.attacking:
            if self.Timer.ElapsedTime_Reach() == True:
                self.attacking = False

    def animate( self ):
        animation = self.animations.animate( self.direction, self.inputType )
        # print( animation )
        self.image = animation
        self.rect  = self.image.get_rect( center = self.hitbox.center )
        self.hitbox = self.rect.inflate( 0, -26 )
        # debug( animation )



    def update( self ):
        self.input()
        self.cooldowns()
        self.animate()
        self.move( self.speed )

        # if IGP.GAME_PARAMETERS["DebugMode"] == True:
        #     pygame.draw.rect( pygame.display.get_surface(), STF.GREEN, self.rect, 1)
