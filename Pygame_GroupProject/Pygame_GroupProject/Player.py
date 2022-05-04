import pygame
from pygame.locals import *

class Player():
    def __init__(self, pos):
        self.health = 100
        self.damage = 20
        self.speed = 5
        self.pos = pygame.Vector2(pos)

        self.image = self.ImageChanger()
        self.image = pygame.image.load(self.image).convert_alpha()
        self.rect = self.image.get_rect(self.pos)

    def ImageChanger(self, weapon):
        image = "placeholder.png"

        if weapon.name == "Pistol":
            image = "Assets/Player/Player_pistol.png"
        elif weapon.name == "Shotgun":
            image = "Assets/Player/Player_shotgun.png"
        elif weapon.name == "Rifle":
            image = "Assets/Player/Player_rifle.png"
        elif weapon.name == "SMG":
            image = "Assets/Player/Player_smg.png"

        return image

    def Movement(self):
        key = pygame.key.get_pressed()

        if key == K_a:
            self.pos.x -= self.speed
        elif key == K_d:
            self.pos.x += self.speed
        elif key == K_w:
            self.pos.y -= self.speed
        elif key == K_s:
            self.pos.y += self.speed

    def Collision(self, wallList, enemiesList):
        hitWall = pygame.sprite.spritecollide(self, wallList, False)
        hitEnemy = pygame.sprite.spritecollide(self, enemiesList, False)

        if hitWall:
            speedBack = 0
            if hitWall[0].rect.top or hitWall[0].rect.bottom or hitWall[0].rect.left or hitWall[0].rect.right:
                speedBack = self.speed
                self.speed == 0
            else:
                self.speed == speedBack

        if hitEnemy:
            if hitEnemy[0].collision == False:
                hitEnemy[0].collision = True

                if hitEnemy[0].attacking == False:
                    hitEnemy[0].attacking = True
                    self.health -= hitEnemy[0].damage

                    pygame.time.wait(750)
                    hitEnemy[0].attacking = False
        else:
            hitEnemy[0].collision = False

#This module holds the player class, and feautres a player's health, image, etc.
#This comes with a movement function that will help the player move, an image function that changes images
#based on the weapon equipt and the collision function that does what it has to if the player hits something

