"""
Created on Sat Feb 26 12:30:00 2022

In this files there are the blueprint class for Enemy

@author: jesus
"""

import pygame, random
import SettingFile as STF
import InGame_Parameters as IGP
import ImageRegister as IR
from ScenaryObjects import Portal
from ImageRegister import Enemy_Sprites_Types as EnemySprite
# from ImageRegister import Bullet_Player_Sprites_Types as BulletSprite

#Use 2D vectors
vector = pygame.math.Vector2


class Zombie(pygame.sprite.Sprite):
    """An enemy class that moves across the screen"""

    def __init__(self, imag_reg:IR.ImageRegister, platform_group, portal_group, min_speed, max_speed):
        """Initialize the zombie"""
        super().__init__()

        #Set constant variables
        self.VERTICAL_ACCELERATION = 4 #Gravity
        self.RISE_TIME = 2

        #Animation frames
        self.walk_right_sprites     = []
        self.walk_left_sprites      = []
        self.die_right_sprites      = []
        self.die_left_sprites       = []
        self.rise_right_sprites     = []
        self.rise_left_sprites      = []

        gender = random.randint(0,1)
        if gender == 0:

            self.walk_right_sprites     = imag_reg.GetSprite( EnemySprite.MALE_ZOMBIE_WALK_RIGTH )
            self.walk_left_sprites      = imag_reg.GetSprite( EnemySprite.MALE_ZOMBIE_WALK_LEFT )

            self.die_right_sprites      = imag_reg.GetSprite( EnemySprite.MALE_ZOMBIE_DIE_RIGTH )
            self.die_left_sprites       = imag_reg.GetSprite( EnemySprite.MALE_ZOMBIE_DIE_LEFT )

        else:
            
            self.walk_right_sprites     = imag_reg.GetSprite( EnemySprite.FEMALE_ZOMBIE_WALK_RIGTH )
            self.walk_left_sprites      = imag_reg.GetSprite( EnemySprite.FEMALE_ZOMBIE_WALK_LEFT )

            self.die_right_sprites      = imag_reg.GetSprite( EnemySprite.FEMALE_ZOMBIE_DIE_RIGTH )
            self.die_left_sprites       = imag_reg.GetSprite( EnemySprite.FEMALE_ZOMBIE_DIE_LEFT )
            
            
        # self.rise_right_sprites     = self.die_right_sprites.reverse()
        # self.rise_left_sprites      = self.die_left_sprites.reverse()
        
            
        #Load an image and get rect
        self.direction = random.choice( [-1, 1] )

        self.current_sprite = 0
        if self.direction == -1:
            self.image = self.walk_left_sprites[ self.current_sprite ]
        else:
            self.image = self.walk_right_sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (random.randint( 100, STF.WINDOW_WIDTH - 100 ), -100 )

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        # Control variables to manage des/activation teleport actions
        self.teleportActivate = False
        self.desactivate_teleport_count = 0

        #Animation booleans
        self.animate_death = False
        self.animate_rise = False

        # #Load sounds
        self.hit_sound = pygame.mixer.Sound("Assets/sounds/zombie_hit.wav")
        self.kick_sound = pygame.mixer.Sound("Assets/sounds/zombie_kick.wav")
        self.portal_sound = pygame.mixer.Sound("Assets/sounds/portal_sound.wav")

        #Kinematics vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(self.direction*random.randint(min_speed, max_speed), 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #Intial zombie values
        self.is_dead = False
        self.round_time = 0
        self.frame_count = 0


    def update(self):
        """Update the zombie"""
        self.move()
        self.check_collisions()
        self.check_animations()

        # #Determine when the zombie should rise from the dead
        # if self.is_dead:
        #     self.frame_count += 1
        #     if self.frame_count % STF.FPS == 0:
        #         self.round_time += 1
        #         if self.round_time == self.RISE_TIME:
        #             self.animate_rise = True
        #             #When the zombie died, the image was kept as the last image
        #             #When it rises, we want to start at index 0 of our rise_sprite lists
        #             self.current_sprite = 0


    def _teleport2position_( self, pos, offset ):
        # print( [ pos, offset ] )
        self.position.x = pos[ 0 ] + offset[ 0 ]
        self.position.y = pos[ 1 ] + offset[ 1 ]
        self.rect.bottomleft = self.position
        
        self.teleportActivate = True

    def move(self):
        """Move the zombie"""
        if not self.is_dead:
            if self.direction == -1:
                self.animate(self.walk_left_sprites, .5)
            else:
                self.animate(self.walk_right_sprites, .5)

            #We don't need to update the accelreation vector because it never changes here

            #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
            self.velocity += self.acceleration
            self.position += self.velocity + 0.5*self.acceleration

            #Update rect based on kinematic calculations and add wrap around movement
            if self.position.x < 0:
                self.position.x = STF.WINDOW_WIDTH
            elif self.position.x > STF.WINDOW_WIDTH:
                self.position.x = 0
            
            self.rect.bottomleft = self.position


    def check_collisions_with_portals( self ):
        collision_enemy_portal = pygame.sprite.spritecollide(self, self.portal_group, False)
        # Determine which portal you are moving to
        if collision_enemy_portal:
            self.portal_sound.play()
            for portal in collision_enemy_portal:
                pos2move = Portal.GetPortal2Teletransport(portal.getUniqueID(), portal.getType() )
                if pos2move != None:
                    if self.direction == -1:
                        offset = ( -0, -10 )
                    else:
                        offset = ( 0, -10 )
                    self._teleport2position_( pos2move, offset )
            

            self.rect.bottomleft = self.position

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between zombie and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 3
            self.velocity.y = 0
            
        #   During 30 frames, desactivate portals collisions
        if self.teleportActivate == False:
            self.check_collisions_with_portals()
        else:
            self.desactivate_teleport_count += 1
            
        if self.desactivate_teleport_count >= 30:
            self.desactivate_teleport_count = 0
            self.teleportActivate = False

        # #Collision check for portals
        # if pygame.sprite.spritecollide(self, self.portal_group, False):
        #     self.portal_sound.play()
        #     #Determine which portal you are moving to
        #     #Left and right
        #     if self.position.x > STF.WINDOW_WIDTH//2:
        #         self.position.x = 86
        #     else:
        #         self.position.x = STF.WINDOW_WIDTH - 150
        #     #Top and bottom
        #     if self.position.y > STF.WINDOW_HEIGHT//2:
        #         self.position.y = 64
        #     else:
        #         self.position.y = STF.WINDOW_HEIGHT - 132

        #     self.rect.bottomleft = self.position


    def check_animations(self):
        """Check to see if death/rise animations should run"""
        #Animate the zombie death
        if self.animate_death:
            if self.direction == 1:
                self.animate(self.die_right_sprites, 1 )
            else:
                self.animate(self.die_left_sprites, .1 )

        #Animate the zombie rise
        if self.animate_rise:
            if self.direction == 1:
                self.animate(self.rise_right_sprites, .095)
            else:
                self.animate(self.rise_left_sprites, .095)


    def animate(self, sprite_list, speed):
        """Animate the zombie's actions"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            #End the death animation
            if self.animate_death:
                self.current_sprite = len(sprite_list) - 1
                self.animate_death = False
            #End the rise animation
            if self.animate_rise:
                self.animate_rise = False
                self.is_dead = False
                self.frame_count = 0
                self.round_time = 0

        self.image = sprite_list[int(self.current_sprite)]