import pygame
from pygame.locals import *

class Aliens():
    def __init__(self, pos, name, health, damage, speed, imageNormal):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(imageNormal).convert_alpha()
        self.rect = self.image.get_rect(self.pos)

        self.collision = False
        self.attacking = False

    def Movement(self, player):
        #Find distance between enemy and player
        distance = pygame.Vector2((player.rect.x - self.rect.x), (player.rect.y - self.rect.y))

        #Normalize it, so it doesn't move too fast when it's close and too slow when it's far
        distance = distance.normalize()

        #Times the normalization by the enemiy's base speed, in order to improve normalization
        distance = distance.scale_to_length(self.speed)

        #Actually move the enemy towards the player
        self.rect.move_ip(distance)

        #Note: I am using _ip() because of its difference to just plain move(), that difference is that
        #_ip moves the object itself, instead of creating a new object every single time

    def ImageChange(self, ImageAttack):
        if self.attacking == True:
            image = pygame.image.load(ImageAttack).convert_alpha()
            self.rect = image.get_rect(self.pos)
        else:
            image = pygame.image.load(self.image).convert_alpha()
            self.rect = self.image.get_rect(self.pos)

    #This module holds the aliens class, and is focused on everything enemy related, such as images and health
    #The move function is used to move the enemy towards the player automatically, no matter where it is
    #The image change function is used for it's attacks, if it does attack then the attack image shows up
