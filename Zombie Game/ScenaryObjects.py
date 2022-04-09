"""
Created on Sat Feb 26 12:30:00 2022

In this files there are the blueprint classes for Player and Bullet Player

@author: jesus
"""

import pygame
import random
import uuid
# import SettingFile as STF
# import InGame_Parameters as IGP
import ImageRegister as IR
from ImageRegister import Levels_Sprites_Types as LST


#Use 2D vectors
# vector = pygame.math.Vector2

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