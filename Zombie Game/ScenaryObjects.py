"""
Created on Sat Feb 26 12:30:00 2022

In this files there are the blueprint classes for Player and Bullet Player

@author: jesus
"""

import pygame
import random
import uuid
import SettingFile as STF
# import InGame_Parameters as IGP
import ImageRegister as IR
from ImageRegister import Levels_Sprites_Types as LST


#Use 2D vectors
vector = pygame.math.Vector2

class Portal( pygame.sprite.Sprite ):
    """A class that if collided with will transport you"""
    
    # Static Variable for the class
    list_portals = []
    
    # I need to create a static method that given a uniqueID and PortalType, give me another
    # portal with the same type but with different UiniqueID. Otherwise, the output portal to teletransport
    def GetPortal2Teletransport( uniID:str, Type:LST ):
        # print( [ uniID, Type ] )
        for portal in Portal.list_portals:
            # print( portal )
            # Checking uniqueID 
            if portal[ 0 ] == uniID:
                continue
            # Checking Portal Type
            if portal[ 2 ] == Type:
                return portal[ 1 ]


    def __init__(self, x, y, imag_reg:IR.ImageRegister, color:LST, portal_group):
        """Initialize the portal"""
        super().__init__()

        self.uniqueID = uuid.uuid4().hex
        self.position = ( x, y )
        self.type = color
        # Save ImageRegister
        self.imageRegister = imag_reg
        
        if color == LST.GREEN_PORTAL:
            self.portal_sprites = self.imageRegister.GetSprite( LST.GREEN_PORTAL )
        else:
            self.portal_sprites = self.imageRegister.GetSprite( LST.PURPLE_PORTAL )
            
        #Load an image and get a rect
        self.current_sprite = random.randint(0, len( self.portal_sprites ) - 1 )

        self.image = self.portal_sprites[ self.current_sprite ]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #Add to the portal group
        portal_group.add( self )
        
        # Append Element to Static Variable
        Portal.list_portals.append( [ self.uniqueID, (x, y), color ] )

    def getUniqueID( self ):
        return self.uniqueID
    
    def getPosition( self ):
        return self.position
    
    def getType( self ):
        return self.type

    def update(self):
        """Update the portal"""
        self.animate(self.portal_sprites, .2)


    def animate(self, sprite_list, speed):
        """Animate the portal"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]
        
        

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self, imag_reg:IR.ImageRegister, platform_group, portal_group):
        """Initialize the ruby"""
        super().__init__()

        #Set constant variables
        self.VERTICAL_ACCELERATION = 3 #Gravity
        self.HORIZONTAL_VELOCITY = 8


        self.ruby_sprites = imag_reg.GetSprite( LST.RUBY )

        self.teleportActivate = False
        self.desactivate_teleport_count = 0

        #Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[ self.current_sprite ]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ( STF.WINDOW_WIDTH//2, 100 )

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        #Load sounds
        # self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

        #Kinematic vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(random.choice([-1*self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        self.previous_pos = self.position

    def update(self):
        """Update the ruby"""
        self.animate(self.ruby_sprites, .25)
        self.move()
        self.check_collisions()


    def move(self):
        """Move the ruby"""
        #We don't need to update the accelreation vector because it never changes here

        #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        self.previous_pos = self.position
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

        # Updating the movement direction of the ruby
        if( ( self.position.x - self.previous_pos.x ) > 0 ):
            self.direction = "right"
        else:
            self.direction = "left"

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
        
        self.teleportActivate = True

    def check_collisions_with_portals( self ):
        collision_ruby_portal = pygame.sprite.spritecollide(self, self.portal_group, False)
        # Determine which portal you are moving to
        if collision_ruby_portal:
            for portal in collision_ruby_portal:
                pos2move = Portal.GetPortal2Teletransport(portal.getUniqueID(), portal.getType() )
                if pos2move != None:
                    if self.direction == "left":
                        offset = ( -0, -10 )
                    else:
                        offset = ( 0, -10 )
                    self._teleport2position_( pos2move, offset )
            

            self.rect.bottomleft = self.position


    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between ruby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 3
            self.velocity.y = 0

        #   During 60 frames, desactivate portals collisions
        if self.teleportActivate == False:
            self.check_collisions_with_portals()
        else:
            self.desactivate_teleport_count += 1
            
        if self.desactivate_teleport_count >= 15:
            self.desactivate_teleport_count = 0
            self.teleportActivate = False
        

    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]