import pygame
import Game as SKG
import SettingFile as STF
from debug import debug

from Level import Level

class ZeldaGame( SKG.Game ):
    
    def __init__(self):
        super().__init__()
        self.level = Level()



    def __UpdateGameState__( self ):  
    # Fill the display surface to cover old images
        self.display_surface.fill( STF.BLACK )    
                
        # WRITE LOGIC HERE


        self.level.run()
                    
        pygame.display.update()
        self.clockGame.tick( STF.FPS )