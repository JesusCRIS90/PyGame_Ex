import pygame
import Game as SKG
import SettingFile as STF
from debug import debug

from Level import Level
from GameSoundManager import *

class ZeldaGame( SKG.Game ):
    
    def __init__(self):
        super().__init__()
        self.level = Level()

        self.main_sound = GameSoundManager().GetSound( SoundEffects_Types.MAIN_SOUND )
        self.main_sound.play( loops = -1 )



    def __UpdateGameState__( self ):  
    # Fill the display surface to cover old images
        self.display_surface.fill( STF.WATER_COLOR ) 
                
        # WRITE LOGIC HERE


        self.level.run()
                    
        pygame.display.update()
        self.clockGame.tick( STF.FPS )