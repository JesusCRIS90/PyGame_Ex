"""
Created on Sat Feb 26 12:31:00 2022

In this files there are the blueprint classes for Enemies and Enemies Bullet

@author: jesus
"""

import pygame
import SettingFile as STF
import random

class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""
    
    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("Assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = 1
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("Assets/alien_fire.wav")

    def update(self):
        """Update the alien"""
        self.rect.x += self.direction*self.velocity

        #Randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        """Fire a bullet"""
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

    def reset(self):
        """Reset the alien position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1



class AlienBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("Assets/red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        self.rect.y += self.velocity

        #If the bullet is off the screen, kill it
        if self.rect.top > STF.WINDOW_HEIGHT:
            self.kill()
