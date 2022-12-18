
"""
Created on Sat Feb 26 12:52:55 2022

This file contain the main "in-game" parameters relative to the game

@author: jesus
"""


from enum import unique, IntEnum
from support import *
import SettingFile as STF


@CustomSingleton
class PlayerStats(  ):

    def __init__(self) -> None:
        self.stats = { 
            "health": STF.PLAYER_MAX_HEALTH * 0.5, 
            "energy": STF.PLAYER_MAX_ENERGY * 0.9, 
            "attack": 10, 
            "magic": 4, 
            "speed": 6,
            "exp": 123,
            "weapon_index": 0,
            "magic_index": 0,
            "Switching_Weapon": False,
            "Switching_Magic": False,
            "Player_Position": ( 0, 0 ),
            "PlayerIsVulnerable": True,
            }
    
    def Get_Stats( self ):
        return self.stats
    
    def Get_Health( self ):
        return self.stats[ "health" ]
    
    def Set_Health( self, value ):
        if value <= 0: value = 0
        if value >= STF.PLAYER_MAX_HEALTH: value = STF.PLAYER_MAX_HEALTH
        self.stats[ "health" ] = value

    def Get_Energy( self ):
        return self.stats[ "energy" ]
    
    def Set_Energy( self, value ):
        if value <= 0: value = 0
        if value >= STF.PLAYER_MAX_ENERGY: value = STF.PLAYER_MAX_ENERGY
        self.stats[ "energy" ] = value
    
    def Get_Attack( self ):
        return self.stats[ "attack" ]
    
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
    
    def Set_MagicIndex( self, index ):
        self.stats[ "magic_index" ] = index
    
    def Get_SwitchingMagic( self ):
        return self.stats[ "Switching_Magic" ]
    
    def Set_SwitchingMagic( self, val:bool ):
        self.stats[ "Switching_Magic" ] = val
    
    def GetPlayerPosition( self ):
        return self.stats[ "Player_Position" ]
    
    def SetPlayerPosition( self, position ):
        self.stats[ "Player_Position" ] = position
    
    def GetPlayerVulnerable( self ):
        return self.stats[ "PlayerIsVulnerable" ]

    def SetPlayerVulnerable( self, value ):
        self.stats[ "PlayerIsVulnerable" ] = value



""" ENUMS """
@unique
class GAME_STATES( IntEnum ):
    INIT_SCREEN         = 0
    GAME_OVER_SCREEN    = 1
    NEXT_ROUND_SCREEN   = 2
    GAME_RUNNING        = 3
    GAME_OVER           = 4
    NEXT_ROUND          = 5
    MOVE_2_START        = 6

"""
    Dictionary with main parameters of game
"""
GAME_PARAMETERS = {
    "GameState": GAME_STATES.INIT_SCREEN,
    "DebugMode": False,
    "CanvasGame": None
}
