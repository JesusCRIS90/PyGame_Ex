import pygame
import SettingFile as STF
from pygame.sprite import Group
from ImageRegister import *
import InGame_Parameters as IGP
from pygame.math import Vector2
from debug import *
from enum import unique, IntEnum

from Weapon import PlayerWeapon
from Animations import *
from support import PyGameTimer


WeaponDict = {
    0   : Weapons_Types.SWORD,
    1   : Weapons_Types.LANCE,
    2   : Weapons_Types.SAI,
    3   : Weapons_Types.RAPIER,
    4   : Weapons_Types.AXE,
}

@CustomSingleton
class PlayerStats(  ):

    def __init__(self) -> None:
        self.stats = { 
            "health": 100, 
            "energy": 100, 
            "attack": 10, 
            "magic": 4, 
            "speed": 6,
            "exp": 123,
            "weapon_index": 0,
            "magic_index": 0,
            "Switching_Weapon": False,
            "Switching_Magic": False
            }
    
    def Get_Stats( self ):
        return self.stats
    
    def Get_Health( self ):
        return self.stats[ "health" ]

    def Get_Energy( self ):
        return self.stats[ "energy" ]
    
    def Get_Exp( self ):
        return self.stats[ "exp" ]
    
    def Get_WeaponIndex( self ):
        return self.stats[ "weapon_index" ]
    
    def Set_WeaponIndex( self, index ):
        self.stats[ "weapon_index" ] = index
    
    def Get_SwitchingWeapon( self ):
        return self.stats[ "Switching_Weapon" ]
    
    def Set_SwitchingWeapon( self, val:bool ):
        self.stats[ "Switching_Weapon" ] = val
    
    def Get_MagicIndex( self ):
        return self.stats[ "magic_index" ]


class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups:Group, enum_sprite, obstacle:Group ) -> None:
        super().__init__( groups )
        self.image = None
        self.rect = None
        self.hitbox = None

        self.Timer = PyGameTimer( STF.ELAPSED_PLAYER_ATTACK_TIME )
        self.Weapon_Timer = PyGameTimer( STF.ELAPSED_PLAYER_ATTACK_TIME )

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.attacking = False
        self.switching_weapon = False

        self.obstacle_sprites = obstacle

        self.inputType = Player_Inputs_Types.IDLE
        self.animations = Animations()
        self.weapon = None
        self.weapon_index = 0
        self.visible_sprite = groups

        if enum_sprite == Player_Sprites_Types.PLAYER_TEST:
            self.image = ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_TEST )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, -26 )

    def input( self ):
        
        self.inputType = Player_Inputs_Types.IDLE
        keys = pygame.key.get_pressed()
        
        if self.attacking:
            self.inputType = Player_Inputs_Types.ATTACKING
            self.direction.y = 0; self.direction.x = 0
            return

        "Moving Inputs"
        if keys[ pygame.K_UP ]:
            self.direction.y = -1;  self.inputType = Player_Inputs_Types.MOVING
        elif keys[ pygame.K_DOWN ]:
            self.direction.y = 1;   self.inputType = Player_Inputs_Types.MOVING
        else:
            self.direction.y = 0

        if keys[ pygame.K_RIGHT ]:
            self.direction.x = 1;   self.inputType = Player_Inputs_Types.MOVING
        elif keys[ pygame.K_LEFT ]:
            self.direction.x = -1;  self.inputType = Player_Inputs_Types.MOVING
        else:
            self.direction.x = 0

        """" Attacking Inputs """
        if keys[ pygame.K_SPACE ] and not self.attacking:
            self.attacking = True
            self.inputType = Player_Inputs_Types.ATTACKING
            self.Timer.Start()
            print("Attack")
            self.weapon = PlayerWeapon( self, self.visible_sprite, 
                self.GetWeaponSprite( self.weapon_index, self.animations.Get_SeeDirection() ) )

        if keys[ pygame.K_LCTRL ] and not self.attacking:
            self.attacking = True
            self.inputType = Player_Inputs_Types.ATTACKING
            self.Timer.Start()
            print("Magic")

        if keys[ pygame.K_q ] and not self.switching_weapon:
            
            self.weapon_index += 1
            if self.weapon_index > 4:
                self.weapon_index = 0

            self.switching_weapon = True
            self.Weapon_Timer.Start()
            print("Switching Weapon")

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

    
    def destroy_weapon( self ):
        if self.weapon != None:
            self.weapon.destroy()
            self.weapon = None
                        
    def cooldowns( self ):
        
        if self.attacking:
            if self.Timer.ElapsedTime_Reach() == True:
                self.attacking = False
                self.destroy_weapon()
        
        if self.switching_weapon:
            if self.Weapon_Timer.ElapsedTime_Reach() == True:
                self.switching_weapon = False
                

    def animate( self ):
        animation = self.animations.animate( self.direction, self.inputType )
        # print( animation )
        self.image = animation
        self.rect  = self.image.get_rect( center = self.hitbox.center )
        self.hitbox = self.rect.inflate( 0, -26 )
        # debug( animation )

    def GetWeaponSprite( self, weapon_index, playerSeeDirection:Player_See_Directions ):
        
        # DOWN
        if playerSeeDirection == Player_See_Directions.DOWN:
            
            if WeaponDict[ weapon_index ] == Weapons_Types.SWORD:
                return Weapons_Types.SWORD_DOWN
            
            if WeaponDict[ weapon_index ] == Weapons_Types.AXE:
                return Weapons_Types.AXE_DOWN
            
            if WeaponDict[ weapon_index ] == Weapons_Types.LANCE:
                return Weapons_Types.LANCE_DOWN
            
            if WeaponDict[ weapon_index ] == Weapons_Types.SAI:
                return Weapons_Types.SAI_DOWN
            
            if WeaponDict[ weapon_index ] == Weapons_Types.RAPIER:
                return Weapons_Types.RAPIER_DOWN
            
        # UP   
        if playerSeeDirection == Player_See_Directions.UP:
                
            if WeaponDict[ weapon_index ] == Weapons_Types.SWORD:
                return Weapons_Types.SWORD_UP
            
            if WeaponDict[ weapon_index ] == Weapons_Types.AXE:
                return Weapons_Types.AXE_UP
            
            if WeaponDict[ weapon_index ] == Weapons_Types.LANCE:
                return Weapons_Types.LANCE_UP
            
            if WeaponDict[ weapon_index ] == Weapons_Types.SAI:
                return Weapons_Types.SAI_UP
            
            if WeaponDict[ weapon_index ] == Weapons_Types.RAPIER:
                return Weapons_Types.RAPIER_UP
        
        # LEFT  
        if playerSeeDirection == Player_See_Directions.LEFT:
                
            if WeaponDict[ weapon_index ] == Weapons_Types.SWORD:
                return Weapons_Types.SWORD_LEFT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.AXE:
                return Weapons_Types.AXE_LEFT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.LANCE:
                return Weapons_Types.LANCE_LEFT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.SAI:
                return Weapons_Types.SAI_LEFT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.RAPIER:
                return Weapons_Types.RAPIER_LEFT
        
        # RIGHT  
        if playerSeeDirection == Player_See_Directions.RIGHT:
                
            if WeaponDict[ weapon_index ] == Weapons_Types.SWORD:
                return Weapons_Types.SWORD_RIGHT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.AXE:
                return Weapons_Types.AXE_RIGHT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.LANCE:
                return Weapons_Types.LANCE_RIGHT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.SAI:
                return Weapons_Types.SAI_RIGHT
            
            if WeaponDict[ weapon_index ] == Weapons_Types.RAPIER:
                return Weapons_Types.RAPIER_RIGHT

    def Update_Player_Stats( self ):
        PlayerStats().Set_WeaponIndex( self.weapon_index )
        PlayerStats().Set_SwitchingWeapon( self.switching_weapon )

    def update( self ):
        self.input()
        self.cooldowns()
        self.animate()
        self.move( self.speed )
        self.Update_Player_Stats()

        # if IGP.GAME_PARAMETERS["DebugMode"] == True:
        #     pygame.draw.rect( pygame.display.get_surface(), STF.GREEN, self.rect, 1)
