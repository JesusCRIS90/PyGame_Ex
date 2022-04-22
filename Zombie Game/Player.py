"""
Created on Sat Feb 26 12:30:00 2022

In this files there are the blueprint classes for Player and Bullet Player

@author: jesus
"""

import pygame
import SettingFile as STF
import InGame_Parameters as IGP
import ImageRegister as IR
from ScenaryObjects import Portal
from ImageRegister import Player_Sprites_Types as PlayerSprite
from ImageRegister import Bullet_Player_Sprites_Types as BulletSprite

#Use 2D vectors
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self, x, y, imag_reg:IR.ImageRegister, platform_group, portal_group, bullet_group):
        """Initialize the player"""
        super().__init__()

        # Save ImageRegister
        self.imageRegister = imag_reg
        #Set constant variables
        self.HORIZONTAL_ACCELERATION    = 2
        self.HORIZONTAL_FRICTION        = 0.18
        self.VERTICAL_ACCELERATION      = 0.8   #Gravity
        self.VERTICAL_JUMP_SPEED        = 18    #Determines how high the player can jump
        self.STARTING_HEALTH            = 100

        # Load image and get rect
        self.current_sprite = 0
        # self.image = self.idle_right_sprites[self.current_sprite]
        temp_sprite_list = self.imageRegister.GetSprite( IR.Player_Sprites_Types.IDLE_RIGTH )
        
        self.image = temp_sprite_list[ self.current_sprite ]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        #Animation booleans
        self.animate_jump = False
        self.animate_fire = False

        #Load sounds
        self.jump_sound = pygame.mixer.Sound("Assets/sounds/jump_sound.wav")
        self.slash_sound = pygame.mixer.Sound("Assets/sounds/slash_sound.wav")
        self.portal_sound = pygame.mixer.Sound("Assets/sounds/portal_sound.wav")
        self.hit_sound = pygame.mixer.Sound("Assets/sounds/player_hit.wav")

        #Kinematics vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        self.direction = ""

        #Set intial player values
        self.health         = self.STARTING_HEALTH
        self.starting_x     = x
        self.starting_y     = y
        
        # Invulnerability period after receive a hit
        self.invulnerability = False
        self.invulnerability_count = 0


    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
        self.check_animations()

        # #Update the players mask
        # self.mask = pygame.mask.from_surface(self.image)
        pass

    def increase_health( self, increase:int ):
        self.health += increase
        if self.health > self.STARTING_HEALTH:
            self.health = self.STARTING_HEALTH
            
    def hit_received( self ):
        self.increase_health( -25 )
        self.invulnerability = True
        self.hit_sound.play()
        pass
    

    def move(self):
        """Move the player"""
        #Set the acceleration vector
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #If the user is pressing a key, set the x-component of the acceleration to be non-zero
        keys = pygame.key.get_pressed()
        
        
        if keys[ pygame.K_LEFT ]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.animate( self.imageRegister.GetSprite( PlayerSprite.RUN_LEFT ), .5)
            self.direction = "left"
        
        elif keys[ pygame.K_RIGHT ]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate( self.imageRegister.GetSprite( PlayerSprite.RUN_RIGTH ), .5)
            self.direction = "rigth"
        
        else:
            if self.velocity.x > 0:
                self.animate( self.imageRegister.GetSprite( PlayerSprite.IDLE_LEFT ), .5)
            else:
                self.animate( self.imageRegister.GetSprite( PlayerSprite.IDLE_RIGTH ), .5)

        #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        self.acceleration.x -= self.velocity.x*self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration
        

        #Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = STF.WINDOW_WIDTH  
        elif self.position.x > STF.WINDOW_WIDTH:
            self.position.x = 0
        
        self.rect.bottomleft = self.position


    def _teleport2position_( self, pos, offset ):
        # print( [ pos, offset ] )
        self.position.x = pos[ 0 ] + offset[ 0 ]
        self.position.y = pos[ 1 ] + offset[ 1 ]
        self.rect.bottomleft = self.position
        pass

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between player and platforms when falling  ; y > 0 --> Falling
        if self.velocity.y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False, pygame.sprite.collide_mask)
            if collided_platforms:
                self.position.y = collided_platforms[ 0 ].rect.top + 5
                self.velocity.y = 0

        #Collision check between player and platform if jumping up  ; y < 0 --> Jumping
        if self.velocity.y < 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False, pygame.sprite.collide_mask)
            if collided_platforms:
                self.velocity.y = 0
                # While player collide with platform move player down
                while pygame.sprite.spritecollide(self, self.platform_group, False):
                    self.position.y += 1
                    self.rect.bottomleft = self.position

        #Collision check for portals
        collision_portal = pygame.sprite.spritecollide(self, self.portal_group, False)
        
        # Determine which portal you are moving to
        if collision_portal:
            self.portal_sound.play()
            for portal in collision_portal:
                pos2move_player = Portal.GetPortal2Teletransport(portal.getUniqueID(), portal.getType() )
                if pos2move_player != None:
                    if self.direction == "left":
                        offset = ( -100, 0 )
                    else:
                        offset = ( 100, 0 )
                    self._teleport2position_( pos2move_player, offset )
        


    def check_animations(self):
        """Check to see if jump/fire animations should run"""
        #Animate the player jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate( self.imageRegister.GetSprite( PlayerSprite.JUMP_RIGHT ), .25)
            else:
                self.animate( self.imageRegister.GetSprite( PlayerSprite.JUMP_LEFT  ), .25)

        #Animate the player attack
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate( self.imageRegister.GetSprite( PlayerSprite.ATTACK_RIGTH ), .20)
            else:
                self.animate( self.imageRegister.GetSprite( PlayerSprite.ATTACK_LEFT  ), .20)


    def jump(self):
        """Jump upwards if on a platform"""
        #Only jump if on a platform
        if pygame.sprite.spritecollide(self, self.platform_group, False):
            self.jump_sound.play()
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
            self.animate_jump = True


    def fire(self):
        """Fire a 'bullet' from a sword"""
        self.slash_sound.play()
        Bullet( self.rect.centerx, self.rect.centery, self.imageRegister, self.bullet_group, self )
        self.animate_fire = True
        pass


    def reset(self):
        """Reset the player's position"""
        self.velocity = vector(0,0)
        self.position = vector(self.starting_x, self.starting_y)
        self.rect.bottomleft = self.position


    def animate(self, sprite_list, speed):
        """Animate the player's actions"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            #End the jump animation
            if self.animate_jump:
                self.animate_jump = False
            #End the attack animation
            if self.animate_fire:
                self.animate_fire = False

        self.image = sprite_list[ int( self.current_sprite ) ]
        
        

class Bullet(pygame.sprite.Sprite):
    """A projectile launched by the player"""

    def __init__(self, x, y, imag_reg:IR.ImageRegister, bullet_group, player ):
        """Initilize the bullet"""
        super().__init__()

        #Set constant variables
        self.VELOCITY = 20
        self.RANGE = 500

        #Load image and get rect
        if player.velocity.x > 0:
            self.image = imag_reg.GetSprite( BulletSprite.BULLET_LEFT )
        else:
            self.image = imag_reg.GetSprite( BulletSprite.BULLET_RIGTH )
            self.VELOCITY = -1*self.VELOCITY
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.starting_x = x

        bullet_group.add( self )

    
    def update(self):
        """Update the bullet"""
        self.rect.x += self.VELOCITY

        #If the bullet has passed the range, kill it
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()
            
        