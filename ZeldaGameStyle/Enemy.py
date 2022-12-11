import pygame
from pygame.math import Vector2

from SettingFile import *
from Entity import Entity
from ImageRegister import *
from Animations import *

class Enemy( Entity ):

    def __init__(self, position, enemy_type, groups):
        super().__init__(groups)

        # General Stats
        self.sprite_type = "enemy"
        self.status = Entity_States.IDLE
        self.enemy_type = Enemy_Dict[ enemy_type ]
        

        # Graphics Setup
        # self.image = pygame.Surface( (64,64) )
        self.image = ImageRegister().GetSprite( 
            Translate2EnemySprite( self.enemy_type, self.status ) )[ self.frame_index ]
        self.rect = self.image.get_rect( topleft = position )
        

def Translate2EnemySprite( enemy_type:Enemy_Types, state:Entity_States ):
    
    if state == Entity_States.IDLE:
        
        if enemy_type == Enemy_Types.BAMBOO:
            return Enemy_Sprites.BAMBOO_IDLE
        
        if enemy_type == Enemy_Types.RACCOON:
            return Enemy_Sprites.RACCOON_IDLE
        
        if enemy_type == Enemy_Types.SPIRIT:
            return Enemy_Sprites.SPIRIT_IDLE

        if enemy_type == Enemy_Types.SQUID:
            return Enemy_Sprites.SQUID_IDLE

    if state == Entity_States.ATTACKING:
        
        if enemy_type == Enemy_Types.BAMBOO:
            return Enemy_Sprites.BAMBOO_ATTACK
        
        if enemy_type == Enemy_Types.RACCOON:
            return Enemy_Sprites.RACCOON_ATTACK
        
        if enemy_type == Enemy_Types.SPIRIT:
            return Enemy_Sprites.SPIRIT_ATTACK

        if enemy_type == Enemy_Types.SQUID:
            return Enemy_Sprites.SQUID_ATTACK

    if state == Entity_States.MOVING:
        
        if enemy_type == Enemy_Types.BAMBOO:
            return Enemy_Sprites.BAMBOO_MOVE
        
        if enemy_type == Enemy_Types.RACCOON:
            return Enemy_Sprites.RACCOON_MOVE
        
        if enemy_type == Enemy_Types.SPIRIT:
            return Enemy_Sprites.SPIRIT_MOVE

        if enemy_type == Enemy_Types.SQUID:
            return Enemy_Sprites.SQUID_MOVE