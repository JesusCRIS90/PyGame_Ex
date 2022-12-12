import pygame
from pygame.math import Vector2

from SettingFile import *
from Entity import Entity
from ImageRegister import *
from Animations import *
from Player import PlayerStats


class Enemy(Entity):

    def __init__(self, position, enemy_type, groups, obstacle_sprites):
        super().__init__(groups)
        monster_info = monster_data[enemy_type]

        # General Stats
        self.sprite_type = "enemy"
        self.status = Entity_States.IDLE
        self.enemy_type = Enemy_Dict[enemy_type]
        self.health         = monster_info["health"]
        self.exp            = monster_info['exp']
        self.speed          = monster_info['speed']
        self.attack_damage  = monster_info['damage']
        self.resistance     = monster_info['resistance']
        self.attack_radius  = monster_info['attack_radius']
        self.notice_radius  = monster_info['notice_radius']
        self.attack_type    = monster_info['attack_type']

        # Graphics Setup
        self.image = ImageRegister().GetSprite(
            Translate2EnemySprite(self.enemy_type, self.status))[self.frame_index]
        
        self.animation_engine = EnemyAnimations()

        self.rect = self.image.get_rect(topleft=position)

        # Movement
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

    def get_player_direction( self ):
        enemy_vector = pygame.math.Vector2( self.rect.center )
        player_vector = PlayerStats().GetPlayerPosition()

        distance = ( player_vector - enemy_vector ).magnitude()
        if distance > 0:
           direction = ( player_vector - enemy_vector ).normalize()
        else:
            # In the case that Player and Enemy have the same position, set direction to Vec2( 0, 0 )
            direction = pygame.math.Vector2(  )

        return direction

    def get_player_distance( self ):
        enemy_vector = pygame.math.Vector2( self.rect.center )
        player_vector = PlayerStats().GetPlayerPosition()
    
        return ( player_vector - enemy_vector ).magnitude()
        

    def update_status( self ):
        distance = self.get_player_distance()

        if distance <= self.attack_radius:
            self.status = Entity_States.ATTACKING
        elif distance <= self.notice_radius:
            self.status = Entity_States.MOVING
        else:
            self.status = Entity_States.IDLE

    def actions( self ):
        
        if self.status == Entity_States.ATTACKING:
            print( "attack" )
        elif self.status == Entity_States.MOVING:
            self.direction = self.get_player_direction()
        else:
            # Make that the Enemy stop moving when player it is outside of its field of vision
            self.direction = pygame.math.Vector2(  )

    def animate( self ):
        self.image = self.animation_engine.animate( self.status, self.enemy_type )
        self.rect  = self.image.get_rect( center = self.hitbox.center )

    def update(self):
        self.update_status()
        self.actions()
        self.move( self.speed )
        self.animate()
        
    # Not needed
    def enemy_update( self ):
        self.update_status()


