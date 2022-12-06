import pygame
from SettingFile import *
from Player import PlayerStats
from ImageRegister import *


class UI_General_Component:

    def __init__(self) -> None:
        
        # general
        self.display_surface = pygame.display.get_surface()

    def display( self ):
        pass

    def update( self ):
        pass

class UI_General_Bar( UI_General_Component ):

    def __init__(self, info_bar:dict ) -> None:
        super().__init__()


        self.info_bar = info_bar
        self.current_bar_size = 100  # Percentage
        self.updating_state_bar = info_bar[ "Update_Func" ]

         # bar setup
        self.BG_bar_rect = pygame.Rect( self.info_bar[ "X_pos" ], self.info_bar[ "Y_pos" ], 
                                     self.info_bar[ "Width" ], self.info_bar[ "Height" ] )

        self.FRONT_bar_rect = self.BG_bar_rect.copy()
    
    
    def display( self ):
        # Draw bg bar
        pygame.draw.rect( self.display_surface, self.info_bar[ "BG_Color" ], self.BG_bar_rect )

        # Drawing the bar
        pygame.draw.rect( self.display_surface, self.info_bar[ "Front_Color" ], self.FRONT_bar_rect )
        pygame.draw.rect( self.display_surface, UI_BORDER_COLOR, self.FRONT_bar_rect, 3 )

    def update(self):
        
        self.current_bar_size = self.updating_state_bar( )
        self.FRONT_bar_rect.width = int( ( self.current_bar_size / 100 ) * self.info_bar[ "Width" ] )

        self.display()

class UI_General_Text( UI_General_Component ):

    def __init__(self, info_text:dict ) -> None:
        super().__init__()

        self.info_text = info_text
        self.updating_fun = info_text[ "Update_Func" ]
        self.text = ""

        self.font = pygame.font.Font( self.info_text[ "Font_Type" ], self.info_text[ "Font_Size" ] )

    def display(self):

        text_surface = self.font.render( self.text, self.info_text[ "AA" ],  self.info_text[ "Text_Color" ] )
        text_rect = text_surface.get_rect( bottomright = ( self.info_text[ "X_pos" ], self.info_text[ "Y_pos" ] ) )

        pygame.draw.rect( self.display_surface, self.info_text[ "BG_Color" ], text_rect.inflate( 20, 20 ) )
        self.display_surface.blit( text_surface, text_rect )
        pygame.draw.rect( self.display_surface, UI_BORDER_COLOR, text_rect.inflate( 20, 20 ), 3 )

    def update(self):
        
        self.text = self.updating_fun()
        self.display()

class UI_General_Box( UI_General_Component ):

    def __init__(self, info_box:dict ) -> None:
        super().__init__()

        self.info_box = info_box
        self.updating_fun = info_box[ "Update_Func" ]
        self.index = 0
        self.switch = 0

    def display(self):

        bg_rect = pygame.Rect( self.info_box["X_pos"], self.info_box["Y_pos"], 
                                self.info_box["Width"], self.info_box["Height"] )

        # Draw Background
        pygame.draw.rect( self.display_surface, self.info_box[ "BG_Color" ], bg_rect )
        
        # Draw BG_frame
        if self.switch:
            pygame.draw.rect( self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3 )
        else:
            pygame.draw.rect( self.display_surface, UI_BORDER_COLOR, bg_rect, 3 )

        # Drawing Image inside Box
        image_surf = ImageRegister().GetSprite( self.index )
        image_rect = image_surf.get_rect( center = bg_rect.center )
        
        self.display_surface.blit( image_surf, image_rect )

    def update(self):
        
        res = self.updating_fun()

        self.index      = res[ "Type_Sprite" ]
        self.switch     = res[ "Switching" ]
        
        self.display()