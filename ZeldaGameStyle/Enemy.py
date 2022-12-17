import pygame
from pygame.math import Vector2

from SettingFile import *
from Entity import Entity
from ImageRegister import *
from Animations import *
from Player import PlayerStats, WeaponDict
from support import PyGameTimer
from CollisionManager import CollissionManager


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
        self.can_attack = True
        self.animation_end = False

        # Invencibility
        self.invencibility_cooldown = 300
        self.hit_timer = PyGameTimer( self.invencibility_cooldown )
        self.vulnerable = True

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
            self.status = Entity_States.ATTACKING
        elif distance <= self.notice_radius:
            self.status = Entity_States.MOVING
        else:
            self.status = Entity_States.IDLE

    def actions( self ):
        
        if self.status == Entity_States.ATTACKING:
            if self.can_attack == True:
                self.attacking_Timer.Start()
                CollissionManager().enemy_attack_logic( self.attack_damage, self.attack_type )
        elif self.status == Entity_States.MOVING:
            self.direction = self.get_player_direction()
        else:
            # Make that the Enemy stop moving when player it is outside of its field of vision
            self.direction = pygame.math.Vector2(  )

    def hit_reaction( self ):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def attackCooldown( self ):
        if self.can_attack == False:
            if self.attacking_Timer.ElapsedTime_Reach():
                self.can_attack = True
    
    def vulerability_cooldown( self ):
        if not self.vulnerable:
            if self.hit_timer.ElapsedTime_Reach():
                self.vulnerable = True
    
    def cooldown( self ):
        self.attackCooldown()
        self.vulerability_cooldown()

    def animate( self ):
        animate_sprite, self.animation_end = self.animation_engine.animate( self.status, self.enemy_type )
        self.image = animate_sprite
        self.rect  = self.image.get_rect( center = self.hitbox.center )

        if self.status == Entity_States.ATTACKING and self.animation_end:
            self.can_attack = False
        
        self.flickering()

    def flickering( self ):
        if not self.vulnerable:
            # flicker
            alpha = self.wave_value()
            self.image.set_alpha( alpha )
        else:
            self.image.set_alpha( 255 )

    def get_damage( self, attack_type ):
        if self.vulnerable:
            self.direction = self.get_player_direction()
            if attack_type == "weapon":
                base_damage = PlayerStats().Get_Attack()
                weapon_damage = weapon_data[ WeaponDict[ PlayerStats().Get_WeaponIndex() ] ][ "damage" ]
                self.health -= ( base_damage + weapon_damage )
            else:
                "Magic Damage"
                pass
            self.hit_timer.Start()
            self.vulnerable = False

    def check_death( self ):
        if self.health <= 0:
            self.kill()

    def update(self):
        self.hit_reaction()
        self.update_status()
        self.move( self.speed )
        self.actions()
        self.animate()
        self.cooldown()
        self.check_death()
        
    # Not needed
    def enemy_update( self ):
        self.update_status()


