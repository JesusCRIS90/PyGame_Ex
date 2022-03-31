"""
Created on Sat Feb 26 12:30:00 2022

In this files there are the blueprint classes for Player and Bullet Player

@author: jesus
"""

import pygame
import SettingFile as STF
import InGame_Parameters as IGP
import ImageRegister as IR

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
        self.HORIZONTAL_FRICTION        = 0.15
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
        # self.jump_sound = pygame.mixer.Sound("sounds/jump_sound.wav")
        # self.slash_sound = pygame.mixer.Sound("sounds/slash_sound.wav")
        # self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")
        # self.hit_sound = pygame.mixer.Sound("sounds/player_hit.wav")

        #Kinematics vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #Set intial player values
        self.health         = self.STARTING_HEALTH
        self.starting_x     = x
        self.starting_y     = y


    def update(self):
        """Update the player"""
        # self.move()
        # self.check_collisions()
        # self.check_animations()

        # #Update the players mask
        # self.mask = pygame.mask.from_surface(self.image)
        pass


    # def move(self):
    #     """Move the player"""
    #     #Set the acceleration vector
    #     self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

    #     #If the user is pressing a key, set the x-component of the acceleration to be non-zero
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
    #         self.animate(self.move_left_sprites, .5)
    #     elif keys[pygame.K_RIGHT]:
    #         self.acceleration.x = self.HORIZONTAL_ACCELERATION
    #         self.animate(self.move_right_sprites, .5)
    #     else:
    #         if self.velocity.x > 0:
    #             self.animate(self.idle_right_sprites, .5)
    #         else:
    #             self.animate(self.idle_left_sprites, .5)

    #     #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
    #     self.acceleration.x -= self.velocity.x*self.HORIZONTAL_FRICTION
    #     self.velocity += self.acceleration
    #     self.position += self.velocity + 0.5*self.acceleration

    #     #Update rect based on kinematic calculations and add wrap around movement
    #     if self.position.x < 0:
    #         self.position.x = WINDOW_WIDTH
    #     elif self.position.x > WINDOW_WIDTH:
    #         self.position.x = 0
        
    #     self.rect.bottomleft = self.position


    # def check_collisions(self):
    #     """Check for collisions with platforms and portals"""
    #     #Collision check between player and platforms when falling
    #     if self.velocity.y > 0:
    #         collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False, pygame.sprite.collide_mask)
    #         if collided_platforms:
    #             self.position.y = collided_platforms[0].rect.top + 5
    #             self.velocity.y = 0

    #     #Collision check between player and platform if jumping up
    #     if self.velocity.y < 0:
    #         collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False, pygame.sprite.collide_mask)
    #         if collided_platforms:
    #             self.velocity.y = 0
    #             while pygame.sprite.spritecollide(self, self.platform_group, False):
    #                 self.position.y += 1
    #                 self.rect.bottomleft = self.position

    #     #Collision check for portals
    #     if pygame.sprite.spritecollide(self, self.portal_group, False):
    #         self.portal_sound.play()
    #         #Determine which portal you are moving to
    #         #Left and right
    #         if self.position.x > WINDOW_WIDTH//2:
    #             self.position.x = 86
    #         else:
    #             self.position.x = WINDOW_WIDTH - 150
    #         #Top and bottom
    #         if self.position.y > WINDOW_HEIGHT//2:
    #             self.position.y = 64
    #         else:
    #             self.position.y = WINDOW_HEIGHT - 132

    #         self.rect.bottomleft = self.position


    # def check_animations(self):
    #     """Check to see if jump/fire animations should run"""
    #     #Animate the player jump
    #     if self.animate_jump:
    #         if self.velocity.x > 0:
    #             self.animate(self.jump_right_sprites, .1)
    #         else:
    #             self.animate(self.jump_left_sprites, .1)

    #     #Animate the player attack
    #     if self.animate_fire:
    #         if self.velocity.x > 0:
    #             self.animate(self.attack_right_sprites, .25)
    #         else:
    #             self.animate(self.attack_left_sprites, .25)


    # def jump(self):
    #     """Jump upwards if on a platform"""
    #     #Only jump if on a platform
    #     if pygame.sprite.spritecollide(self, self.platform_group, False):
    #         self.jump_sound.play()
    #         self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
    #         self.animate_jump = True


    # def fire(self):
    #     """Fire a 'bullet' from a sword"""
    #     self.slash_sound.play()
    #     Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
    #     self.animate_fire = True


    # def reset(self):
    #     """Reset the player's position"""
    #     self.velocity = vector(0,0)
    #     self.position = vector(self.starting_x, self.starting_y)
    #     self.rect.bottomleft = self.position


    # def animate(self, sprite_list, speed):
    #     """Animate the player's actions"""
    #     if self.current_sprite < len(sprite_list) -1:
    #         self.current_sprite += speed
    #     else:
    #         self.current_sprite = 0
    #         #End the jump animation
    #         if self.animate_jump:
    #             self.animate_jump = False
    #         #End the attack animation
    #         if self.animate_fire:
    #             self.animate_fire = False

    #     self.image = sprite_list[int(self.current_sprite)]