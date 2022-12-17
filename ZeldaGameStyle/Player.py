import pygame
import SettingFile as STF
from pygame.sprite import Group
from ImageRegister import *
from pygame.math import Vector2
from debug import *
from enum import unique, IntEnum

from Weapon import PlayerWeapon
from Animations import *
from support import PyGameTimer
from Entity import Entity
from CollisionManager import CollissionManager
from InGame_Parameters import PlayerStats


WeaponDict = {
    0   : Weapons_Types.SWORD,
    1   : Weapons_Types.LANCE,
    2   : Weapons_Types.SAI,
    3   : Weapons_Types.RAPIER,
    4   : Weapons_Types.AXE,
}

MagicDict = {
    0   : Magic_Types.FLAME,
    1   : Magic_Types.HEAL
}


class Player( Entity ):

    def __init__(self, position, groups:Group, enum_sprite, obstacle:Group ) -> None:
        super().__init__( groups )
        # self.image = None
        # self.rect = None
        # self.hitbox = None

        self.Timer = PyGameTimer( STF.ELAPSED_PLAYER_ATTACK_TIME )
        self.Weapon_Timer = PyGameTimer( STF.ELAPSED_PLAYER_ATTACK_TIME )
        self.Magic_Timer = PyGameTimer( STF.ELAPSED_PLAYER_ATTACK_TIME )

        # self.direction = pygame.math.Vector2()
        self.speed = 6

        self.attacking = False
        
        self.switching_weapon = False
        self.weapon = None
        self.weapon_index = 0

        self.switching_magic = False
        self.magic = None
        self.magic_index = 0

        self.obstacle_sprites = obstacle

        self.inputType = Entity_States.IDLE
        self.animations = PlayerAnimations()

        self.visible_sprite = groups

        # Invencibility
        self.invencibility_cooldown = 500
        self.hurt_timer = PyGameTimer( self.invencibility_cooldown )
        self.vulnerable = True

        if enum_sprite == Player_Sprites_Types.PLAYER_TEST:
            self.image = ImageRegister().GetSprite( Player_Sprites_Types.PLAYER_TEST )
            self.rect  = self.image.get_rect( topleft = position )
            self.hitbox = self.rect.inflate( 0, -26 )

    def input( self ):
        
        self.inputType = Entity_States.IDLE
        keys = pygame.key.get_pressed()
        
        if self.attacking:
            self.inputType = Entity_States.ATTACKING
            self.direction.y = 0; self.direction.x = 0
            return

        "Moving Inputs"
        if keys[ pygame.K_UP ]:
            self.direction.y = -1;  self.inputType = Entity_States.MOVING
        elif keys[ pygame.K_DOWN ]:
            self.direction.y = 1;   self.inputType = Entity_States.MOVING
        else:
            self.direction.y = 0

        if keys[ pygame.K_RIGHT ]:
            self.direction.x = 1;   self.inputType = Entity_States.MOVING
        elif keys[ pygame.K_LEFT ]:
            self.direction.x = -1;  self.inputType = Entity_States.MOVING
        else:
            self.direction.x = 0

        """" Attacking Inputs """
        
        """ Weapon Attack """
        if keys[ pygame.K_SPACE ] and not self.attacking:
            self.attacking = True
            self.inputType = Entity_States.ATTACKING
            self.Timer.Start()
            self.weapon = PlayerWeapon( self, [self.visible_sprite, 
                CollissionManager().get_attackSpriteGroup()],
                self.GetWeaponSprite( self.weapon_index, self.animations.Get_SeeDirection() ) )

        """ Magic Attack - UDER DEVELOPMENT """
        if keys[ pygame.K_LCTRL ] and not self.attacking:
            self.attacking = True
            self.inputType = Entity_States.ATTACKING
            self.Timer.Start()
            print("Magic")

        """ Switching Weapon """
        if keys[ pygame.K_q ] and not self.switching_weapon:
            
            self.weapon_index += 1
            if self.weapon_index > 4:
                self.weapon_index = 0

            self.switching_weapon = True
            self.Weapon_Timer.Start()
            print("Switching Weapon")

        
        """ Switching Weapon """
        if keys[ pygame.K_e ] and not self.switching_magic:
            
            self.magic_index += 1
            if self.magic_index > 1:
                self.magic_index = 0

            self.switching_magic = True
            self.Magic_Timer.Start()
            print("Switching Magic")
    
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
        
        if self.switching_magic:
            if self.Magic_Timer.ElapsedTime_Reach() == True:
                self.switching_magic = False
        
        self.vulnerability_cooldown()

    def vulnerability_cooldown( self ):
        if self.vulnerable == False:
            if self.hurt_timer.ElapsedTime_Reach():
                self.vulnerable = True
                PlayerStats().SetPlayerVulnerable( True )

    def animate( self ):
        animation = self.animations.animate( self.direction, self.inputType )
        self.image = animation
        self.rect  = self.image.get_rect( center = self.hitbox.center )
        self.hitbox = self.rect.inflate( 0, -26 )

        # Flickering
        self.flickering()

    def flickering( self ):
        if not self.vulnerable:
            # flicker
            alpha = self.wave_value()
            self.image.set_alpha( alpha )
        else:
            self.image.set_alpha( 255 )

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
        PlayerStats().Set_MagicIndex( self.magic_index )
        PlayerStats().Set_SwitchingMagic( self.switching_magic )
        PlayerStats().SetPlayerPosition( self.rect.center )
        
        # The player has been damage, so activate vulnerability timer
        if PlayerStats().GetPlayerVulnerable() == False:
            self.vulnerable = False
        else:
            self.hurt_timer.Start()


    def update( self ):
        self.input()
        self.cooldowns()
        self.animate()
        self.move( self.speed )
        self.Update_Player_Stats()

        # if IGP.GAME_PARAMETERS["DebugMode"] == True:
        #     pygame.draw.rect( pygame.display.get_surface(), STF.GREEN, self.rect, 1)
