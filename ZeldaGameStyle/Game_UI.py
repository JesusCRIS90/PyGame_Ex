import pygame
from SettingFile import *
from UI_Components import *
from Player import PlayerStats
from Player import WeaponDict, MagicDict
from ImageRegister import *

# TO-DO: Update Magic_Box Component

class Game_UI:

    def __init__(self) -> None:
        
        self.UI_Components_list = []
        self.display_surface = pygame.display.get_surface()
        
        # Creating UI Components
        self.health_bar = UI_General_Bar( {
            "X_pos": 10, "Y_pos": 10,
            "Width": HEALTH_BAR_WIDTH,
            "Height": BAR_HEIGHT,
            "BG_Color": UI_BG_COLOR,
            "Front_Color": HEALTH_COLOR,
            "Maximun_Value": PLAYER_MAX_HEALTH,
            "Update_Func": Player_Bar_Health_Update
        } )

        self.energy_bar = UI_General_Bar( {
            "X_pos": 10, "Y_pos": 34,
            "Width": ENERGY_BAR_WIDTH,
            "Height": BAR_HEIGHT,
            "BG_Color": UI_BG_COLOR,
            "Front_Color": ENERGY_COLOR,
            "Maximun_Value": PLAYER_MAX_ENERGY,
            "Update_Func": Player_Bar_Energy_Update
        } )

        self.exp_text = UI_General_Text( {
            "X_pos": self.display_surface.get_size()[ 0 ] - 20, 
            "Y_pos": self.display_surface.get_size()[ 1 ] - 20,
            "Font_Type": FONT_NAME,
            "Font_Size": FONT_SIZE,
            "BG_Color": UI_BG_COLOR,
            "AA": False,
            "Text_Color": TEXT_COLOR,
            "Update_Func": Player_Exp_Update
        } )
    
        self.weapon = UI_General_Box( {
            "X_pos": 10, 
            "Y_pos": int( self.display_surface.get_size()[ 1 ] - ( ITEM_BOX_SIZE + 10 + 20 ) ),
            "Width": ITEM_BOX_SIZE,
            "Height": ITEM_BOX_SIZE + 20,
            "BG_Color": UI_BG_COLOR,
            "Update_Func": Player_Weapon_Update
        } )

        self.magic = UI_General_Box( {
            "X_pos": ITEM_BOX_SIZE + 0, 
            "Y_pos": int( self.display_surface.get_size()[ 1 ] - ( ITEM_BOX_SIZE + 35 ) ),
            "Width": ITEM_BOX_SIZE,
            "Height": ITEM_BOX_SIZE + 20,
            "BG_Color": UI_BG_COLOR,
            "Update_Func": Player_Magic_Update
        } )
        
        # Saving UI Components into List
        self.UI_Components_list.append( { "UI_Component_Name": "Health_Bar",    "Component": self.health_bar } )
        self.UI_Components_list.append( { "UI_Component_Name": "Energy_Bar",    "Component": self.energy_bar } )
        self.UI_Components_list.append( { "UI_Component_Name": "Exp_Text",      "Component": self.exp_text } )
        self.UI_Components_list.append( { "UI_Component_Name": "Weapon_Box",    "Component": self.weapon } )
        self.UI_Components_list.append( { "UI_Component_Name": "Magic_Box",     "Component": self.magic } )

    def display( self ):
        
        for ui_comp in self.UI_Components_list:
            ui_comp[ "Component" ].update()




def Player_Bar_Health_Update( ):
    return PlayerStats().Get_Health()

def Player_Bar_Energy_Update( ):
    return PlayerStats().Get_Energy()

def Player_Exp_Update( ):
    exp = PlayerStats().Get_Exp()
    return str( int( exp ) )

def Player_Weapon_Update( ):
    
    res = { "Type_Sprite": 0, "Switching": False }

    index = PlayerStats().Get_WeaponIndex()
    if WeaponDict[ index ] == Weapons_Types.SWORD:
        res[ "Type_Sprite" ] = Weapons_Types.SWORD_FULL
    
    elif WeaponDict[ index ] == Weapons_Types.AXE:
        res[ "Type_Sprite" ] = Weapons_Types.AXE_FULL

    elif WeaponDict[ index ] == Weapons_Types.LANCE:
        res[ "Type_Sprite" ] = Weapons_Types.LANCE_FULL

    elif WeaponDict[ index ] == Weapons_Types.SAI:
        res[ "Type_Sprite" ] = Weapons_Types.SAI_FULL
    
    elif WeaponDict[ index ] == Weapons_Types.RAPIER:
        res[ "Type_Sprite" ] = Weapons_Types.RAPIER_FULL

    res[ "Switching" ] = PlayerStats().Get_SwitchingWeapon()

    return res

def Player_Magic_Update( ):
    
    res = { "Type_Sprite": 0, "Switching": False }

    index = PlayerStats().Get_MagicIndex()
    if MagicDict[ index ] == Magic_Types.FLAME:
        res[ "Type_Sprite" ] = Magic_Types.FLAME
    else:
        res[ "Type_Sprite" ] = Magic_Types.HEAL

    res[ "Switching" ] = PlayerStats().Get_SwitchingMagic()
    return res
    
    
