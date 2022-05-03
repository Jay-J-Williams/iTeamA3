import pygame, random

class Characters():
    __character_x = 0
    __character_y = 0
    __movement_speed = 0
    __health = 0
    __damage = 0
    __alive = False
    __asset = None
    def __init__(self, x, y, health, speed, dmg, alive, asset):
        self.characterX = x
        self.characterY = y
        self.health = health
        self.movement_speed = speed
        self.damage = dmg
        self.alive = alive
        self.asset = asset

    property
    def characterX(self):
        return self.__character_x
    property
    def characterY(self):
        return self.__character_y
    property
    def health(self):
        return self.__health
    property
    def movement_speed(self):
        return self.__movement_speed
    property
    def damage(self):
        return self.__damage
    property
    def alive(self):
        return self.__alive
    property
    def asset(self):
        return self.__asset

    characterX.setter
    def characterX(self, value):
        self.__character_x = value
    characterY.setter
    def characterY(self, value):
        self.__character_y = value
    health.setter
    def health(self, value):
        self.__health = value
    movement_speed.setter
    def movement_speed(self, value):
        self.__movement_speed = value
    damage.setter
    def damage(self, value):
        self.__damage = value
    alive.setter
    def alive(self, value):
        self.__alive = value
    asset.setter
    def asset(self, value):
        self.__asset = value

    @staticmethod
    def move(self, direction, object_x, object_y):
        if direction == "left":
            object_x -= self.movement_speed
        elif direction == "right":
            object_x += self.movement_speed
        elif direction == "up":
            object_y -= self.movement_speed
        elif direction == "down":
            object_y += self.movement_speed

class Player(Characters):
    __weapon = None
    __power_up = None
    def __init__(self, x, y, health, weapon, speed, damage):
        self.weapon = weapon
        self.power_up = None

        if weapon == pistol:
            self.asset = ""
        elif weapon == shotgun:
            self.asset = ""
        elif weapon == rifle:
            self.asset = ""
        elif weapon == smg:
            self.asset = ""

        super().__init__(x, y, health, speed, damage, self.asset)

    property
    def weapon(self):
        return self.__weapon
    property
    def power_up(self):
        return self.__power_up

    weapon.setter
    def weapon(self, value):
        self.__weapon = value
    power_up.setter
    def power_up(self, value):
        self.__power_up = value 

    def shoot(self, weapon, bullets):
        pass

    def delay(self, weapon):
        self.delay = 1000 / weapon.fire_rate
        pygame.time.wait(self.delay)

class Weapons:
    __name = None
    __damage = None
    __fire_rate = None

    def __init__(self, name, damage, fire_rate):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate

    property
    def name(self):
        return self.__name
    property
    def damage(self):
        return self.__damage
    property
    def fire_rate(self):
        return self.__fire_rate

    name.setter
    def name(self, value):
        self.__name = value
    damage.setter
    def damage(self, value):
        self.__damage = value
    fire_rate.setter
    def fire_rate(self, value):
        self.__fire_rate = value

#Only use ints for the fire rate, also positives
pistol = Weapons("Pistol", 30, 2)
shotgun = Weapons("Shotgun", 50, 1)
smg = Weapons("Sub_Machine_Gun", 10, 10)
rifle = Weapons("Rifle", 40, 3)

class Bullets():
    __asset = None
    __showing = False
    __speed = 0
    __target = None
    __bulletX = 0
    __bulletY = 0

    def __init__(self, asset, speed, target, x, y):
        self.asset = asset
        self.speed = speed
        self.target = target
        self.bulletX = x
        self.bulletY = y

    property
    def asset(self):
        return self.__asset

    property
    def showing(self):
        return self.__showing

    property
    def speed(self):
        return self.__speed

    property
    def target(self):
        return self.__target

    property
    def bulletX(self):
        return self.__bulletX

    property
    def bulletY(self):
        return self.__bulletY

    asset.setter
    def asset(self, value):
        self.__asset = value

    showing.setter
    def showing(self, value):
        self.__showing = value

    speed.setter
    def speed(self, value):
        self.__speed = value

    target.setter
    def target(self, value):
        self.__target = value

    bulletX.setter
    def bulletX(self, value):
        self.__bulletX = value

    bulletY.setter
    def bulletY(self, value):
        self.__bulletY = value

bullet = Bullets()

class Aliens(Characters):
    __target = None

    def __init__(self, x, y, health, speed, damage, target):
        super().__init__(x, y, health, speed, damage)
        self.target = target

    property
    def target(self):
        return self.__target
        
    target.setter
    def target(self, value):
        self.__target = value

class RangedAliens(Aliens):
    pass

class PhysicalAliens(Aliens):
    pass