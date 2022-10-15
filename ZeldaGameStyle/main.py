# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 18:43:55 2022

ZELDA-STYLE GAME USING PYGAME LIBRARY

@author: Jesus
"""

from CustomZeldaGame import *

from ImageRegister import ImageRegister

if __name__ == '__main__':
    game = ZeldaGame()
    game.RunGame()


# if __name__ == "__main__":
#     # The client code.

#     s1 = ImageRegister
#     s2 = ImageRegister()

#     if id(s1) == id(s2):
#         print("Singleton works, both variables contain the same instance.")
#     else:
#         print("Singleton failed, variables contain different instances.")