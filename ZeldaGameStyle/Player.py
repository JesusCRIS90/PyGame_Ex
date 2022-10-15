import pygame
import SettingFile as STF
from pygame.sprite import Group
from ImageRegister import *
import InGame_Parameters as IGP

class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups:Group, enum_sprite, obstacle:Group ) -> None:
        super().__init__( groups )
        self.image = None
        self.rect = None
        self.hitbox = None

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle

        if enum_sprite == Player_Sprites_Types.PLAYER_TEST:
            self.image = ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_TEST )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, -26 )

    def input( self ):
        keys = pygame.key.get_pressed()
        
        if keys[ pygame.K_UP ]:
            self.direction.y = -1
        elif keys[ pygame.K_DOWN ]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[ pygame.K_RIGHT ]:
            self.direction.x = 1
        elif keys[ pygame.K_LEFT ]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
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

    def update( self ):
        self.input()
        self.move( self.speed )

        # if IGP.GAME_PARAMETERS["DebugMode"] == True:
        #     pygame.draw.rect( pygame.display.get_surface(), STF.GREEN, self.rect, 1)