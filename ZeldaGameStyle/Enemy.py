import pygame
from pygame.math import Vector2

from SettingFile import *
from Entity import Entity
from ImageRegister import *
from Animations import *
from Player import PlayerStats
from support import PyGameTimer


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

        # Others
        self.attacking_Timer = PyGameTimer( monster_info['attack_cooldown'] )
        # self.attacking_Timer = PyGameTimer( 400 )
        self.can_attack = True
        self.animation_end = False

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

        if distance <= self.attack_radius and self.can_attack:
            if self.status != Entity_States.ATTACKING:
                self.animation_engine.Reset_FrameIndex() # Check the reason for this
                pass
            self.status = Entity_States.ATTACKING
        elif distance <= self.notice_radius:
            self.status = Entity_States.MOVING
        else:
            self.status = Entity_States.IDLE

    def actions( self ):
        
        if self.status == Entity_States.ATTACKING:
            if self.can_attack == True:
                self.attacking_Timer.Start()
        elif self.status == Entity_States.MOVING:
            self.direction = self.get_player_direction()
        else:
            # Make that the Enemy stop moving when player it is outside of its field of vision
            self.direction = pygame.math.Vector2(  )

    def attackCooldown( self ):
        if self.can_attack == False:
            if self.attacking_Timer.ElapsedTime_Reach():
                self.can_attack = True

    def animate( self ):
        animate_sprite, self.animation_end = self.animation_engine.animate( self.status, self.enemy_type )
        self.image = animate_sprite
        self.rect  = self.image.get_rect( center = self.hitbox.center )

        if self.status == Entity_States.ATTACKING and self.animation_end:
            self.can_attack = False
            


    def update(self):
        self.update_status()
        self.move( self.speed )
        self.actions()
        self.animate()
        self.attackCooldown()
        
    # Not needed
    def enemy_update( self ):
        self.update_status()


