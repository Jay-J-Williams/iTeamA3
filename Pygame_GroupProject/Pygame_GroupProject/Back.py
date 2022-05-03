import pygame, random

class Characters():
    __character_pos = pygame.Vector2(0, 0) 
    #I remembered that pygame uses the vector2() variable to handle positioning, it will help us - Adam 
    __movement_speed = 0
    __health = 0
    __damage = 0
    __alive = False
    __asset = None
    def __init__(self, x, y, health, speed, dmg, alive, asset):
        self.characterPos = pygame.Vector2(x, y)
        self.health = health
        self.movement_speed = speed
        self.damage = dmg
        self.alive = alive
        self.asset = asset

    property
    def characterPos(self):
        return self.__character_pos
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

    characterPos.setter
    def characterX(self, value):
        self.__character_pos = value
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

#Only use positive integers for the fire_rate (final input), not decimals or strings
#pistol = Weapons("Pistol", 30, 2)
#shotgun = Weapons("Shotgun", 50, 1)
#smg = Weapons("Sub_Machine_Gun", 10, 10)
#rifle = Weapons("Rifle", 40, 3)

#The weapons are created in the front-end, because that is where we will put the while loop of a running game
#We don't have to adjust anything here because it will work either way. This is just to make writing the
#front-end easier. I know that the user will not interact with it, and that is partly false because the
#user will be interacting with a specific weapon at a specific time, like walking, which will take the
#front-end of keyboard inputs, the weapons will take the front-end role as objects to change and gain from
#drops - Adam

class Bullets():
    __asset = None
    __showing = False
    __speed = 0
    __target = None
    __bulletPos = pygame.Vector2(0, 0) #Like player, I have changed this to better suit the code of the game 
                                        #- Adam

    def __init__(self, asset, speed, target, x, y):
        self.asset = asset
        self.speed = speed
        self.target = target
        self.bulletPos = pygame.Vector2(x, y)

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
    def bulletPos(self):
        return self.__bulletPos

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

    bulletPos.setter
    def bulletPos(self, value):
        self.__bulletPos = value

#bullet = Bullets()
#This variable will be created in the front-end, every single time the key "enter" is pressed, because the
#player has to first interact with the game to spawn a bullet, they are created in the front. - Adam

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

class EnemySpawn():
    def AlienCreator():
        ListOfAliens = []

        return ListOfAliens

    def AlienDoorSpawn():
        Door1 = pygame.Vector2(0, 1200)
        Door2 = pygame.Vector2(0, 100)
        Door3 = pygame.Vector2(1200, 50)
        Door4 = pygame.Vector2(1200, 600)
        
        rand = random.randint(0, 3)
        Location = None

        if rand == 0:
            return Door4
        elif rand == 1:
            return Door2
        elif rand == 2:
            return Door1
        elif rand == 3:
            return Door3
    #I created this sample class to handle the enemy spawns using the rarity system, as well as handle where
    #the enemies spawn to. I believe we should use door locations in the way that I have