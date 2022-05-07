import pygame, random

class allErrors(Exception):
    pass
class numErrors(allErrors):
    pass
class boolErrors(allErrors):
    pass
class strErrors(allErrors):
    pass
class objectErrors(allErrors):
    pass
class entryErrors(allErrors):
    pass

class Characters():
    __speed = 0
    __health = 0
    __damage = 0
    __is_alive = False
    __pos_x = 1
    __pos_y = 1
    def __init__(self, health, speed, dmg, is_alive, x, y):
        self.speed = speed
        self.health = health
        self.damage = dmg
        self.is_alive = is_alive
        self.pos_x = x
        self.pos_y = y

    @property
    def speed(self):
        return self.__speed
    
    @property
    def health(self):
        return self.__health

    @property
    def damage(self):
        return self.__damage

    @property
    def is_alive(self):
        return self.__is_alive

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @speed.setter
    def speed(self, value):
        if value > 0:
            self.__movement_speed = value
        else:
            raise numErrors("Movement Speed has to be a positive int")
        
    @health.setter
    def health(self, value):
        if value > 0:
            self.__health = value
        else:
            raise numErrors("Health must be a positive int")
        
    @damage.setter
    def damage(self, value: int):
        if value > 0:
            self.__damage = value
        else:
            raise numErrors("Damage must be a positive int")

    @is_alive.setter
    def is_alive(self, value: bool):
        if value == False or value == True:
            self.__is_alive = value
        else:
            raise boolErrors("is_alive must be a boolean value")

#Add another conditional statement to check whether the value is too large for
#the map once the map size is finalised
#I has to change the vector because it doesn't work in this context.
    @pos_x.setter
    def pos_x(self, value: int):
        if value > 0:
            self.__pos_x = value
        else:
            numErrors("pos_x must be a positive integer")

    @pos_y.setter
    def pos_y(self, value:int):
        if value > 0:
            self.__pos_y = value
        else:
            numErrors("pos_y must be a positive integer")

class Player(Characters):
    __power_up = None
    def __init__(self, health, speed, damage, is_alive, pos_x, pos_y, power_up):
        super().__init__(health, speed, damage, is_alive, pos_x, pos_y)
        self.power_up = power_up  

    @property
    def power_up(self):
        return self.__power_up

    @power_up.setter
    def power_up(self, value: object):
        if value != "":
            self.__power_up = value 
        else:
            raise objectErrors("The power-up must be an object, or 'None'")

    def shoot(self, weapon: object, bullet: object):
        pass

    def delay(self, weapon: object):
        self.delay = 1000 / weapon.fire_rate
        pygame.time.wait(self.delay)

class Weapons:
#I doubt we need the name here considering that the objects will have names  
    __name = None
    __damage = None
    __fire_rate = None

    def __init__(self, name, damage, fire_rate):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate

    @property
    def name(self):
        return self.__name
    @property
    def damage(self):
        return self.__damage
    @property
    def fire_rate(self):
        return self.__fire_rate

    @name.setter
    def name(self, value: str):
        if value == "Pistol" or value == "Shotgun":
            self.__name = value
        elif value == "Sub-machine-gun" or value == "Rifle":
            self.__name = value
        else:
            raise strErrors("You must enter 'Pistol', 'Shotgun', 'Sub-machine-gun', or 'Rifle'")
    @damage.setter
    def damage(self, value: int):
        if value > 0:
            self.__damage = value
        else:
            raise numErrors("You must enter a positive int")
    @fire_rate.setter
    def fire_rate(self, value: int):
        if value > 0 and value < 10:
            self.__fire_rate = value
        else:
            raise numErrors("You must enter an int from 1 to 10")

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
    __speed = 0
    __target = None
    __pos_x = 1
    __pos_y = 1

    def __init__(self, asset, speed, target, pos_x, pos_y):
        self.asset = asset
        self.speed = speed
        self.target = target
        self.pos_x = pos_x
        self.pos_y = pos_y

    @property
    def asset(self):
        return self.__asset

    @property
    def showing(self):
        return self.__showing

    @property
    def speed(self):
        return self.__speed

    @property
    def target(self):
        return self.__target

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.pos_y

    @asset.setter
    def asset(self, value: str):
        if value != "":
            self.__asset = value
        else:
            raise strErrors("You must enter a string")

    @showing.setter
    def showing(self, value: bool):
        if value == True or value == False:
            self.__showing = value
        else:
            raise boolErrors("You must enter a boolean value for 'showing'")

    @speed.setter
    def speed(self, value: int):
        if value > 0:
            self.__speed = value
        else:
            raise numErrors("You must enter an integer that is greater than zero")

    @target.setter
    def target(self, value: object):
        self.__target = value

    @pos_x.setter
    def pos_x(self, value: int):
        if value > 0:
            self.__pos_x = value
        else:
            raise numErrors("You must an integer that is greater than zero")

    @pos_y.setter
    def pos_y(self, value):
        if value > 0:
            self.__pos_y = value
        else:
            raise numErrors("You must an integer that is greater than zero")
        
#bullet = Bullets()
#This variable will be created in the front-end, every single time the key "enter" is pressed, because the
#player has to first interact with the game to spawn a bullet, they are created in the front. - Adam

class Aliens(Characters):
    __target = None
#I have added the spawn rate into the Aliens class because it will be a
#necessary value for each alien.
    __spawn_rate = None

    def __init__(self, health, speed, damage, is_alive, pos_x, pos_y, target, spawn_rate):
        super().__init__(health, speed, damage, is_alive, pos_x, pos_y)
        self.target = target
        self.spawn_rate = spawn_rate

    @property
    def target(self):
        return self.__target

    @property
    def spawn_rate(self):
        return self.__spawn_rate
        
    @target.setter
    def target(self, value: object):
        self.__target = value

    @spawn_rate.setter
    def spawn_rate(self, value):
        self.__spawn_rate = value

#I created this function to convert the int spawn_rate e.g., 10(%) to a range
#so it can be used to spawn the aliens. I have included first_conversion
#because it determines if a starting point is needed. I added the previous
#alien's spawn rate into the parameters because it will be needed to calculate
#the converted spawn rate for the new alien. If you want to do the first
#conversion, you will need to enter a value for the previous alien's spawn rate,
#but you can enter a 0 or "n/a" for readability as it wouldn't be used anyways.
#I have the list function call on range because range returns a sequence, not a
#list.
    def convert_spawn_rate(self, first_conversion: bool, last_aliens_spawn_rate: list):
        if first_conversion == False:
            starting_point = last_aliens_spawn_rate[-1] + 1
            end_point = self.spawn_rate + starting_point
        if first_conversion == True:
            self.spawn_rate = list(range(1, self.spawn_rate + 1))
        else:
            self.spawn_rate = list(range(starting_point, end_point))
        last_aliens_spawn_rate = self.spawn_rate
        return last_aliens_spawn_rate

#I have made this a static method because it does not impact a single object. I
#have added each spawn rate into the parameters because this function determines
#which alien it wants to spawn based on the random integer it provides. The door
#is chosen by another random integer method which goes into the spawn parameters
#because the alien's position must be were the chosen door is when it spawns in.
#I have used the logic "range(alien.spawn_rate[0}, alien.spawn_rate[-1] because
#all the numbers in the list must be used, and this is the quickest, and most
#readable way of doing it.

#Spawn Number = 15
#Rand = randint(0, 99)
# if Rand < 25:
# spawn shield
# if Rand > 24 and Rand < 34
# spawn bomber
#while len(listTotal) <= 100:
 #~~~~~~

#shield 10, turret 20,
#shield list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#15

#    @staticmethod
#    def rando_spawn(shieldSpawn, turretSpawn, wingSpawn, sniperSpawn, bomberSpawn, mosquitoSpawn, total):
#        i = 0
#
#        while i < total:
#            alien = random.randint(0, 100)
#
#            if alien == range(shieldSpawn[0], shieldSpawn[-1]):
#                yield shield
#            elif alien == range(turretSpawn[0], turretSpawn[-1]):
#                yield turret
#            elif alien == range(wingSpawn[0], wingSpawn[-1]):
#                yield wing 
#            elif alien == range(sniperSpawn[0], sniperSpawn[-1]):
#                yield sniper 
#            elif alien == range(bomberSpawn[0], bomberSpawn[-1]):
#                yield bomber 
#            elif alien == range(mosquitoSpawn[0], mosquitoSpawn[-1]):
#                yield mosquito 
#
#            i += 1

    @staticmethod
    def random_spawn():
        alien_choice = random.randint(1, 100)
        print(alien_choice)
        door_choice = random.randint(1, 8)
        if alien_choice >= shield.spawn_rate[0] and alien_choice <= shield.spawn_rate[-1]:
            alien = "Shield"
            shield.spawn(door_choice)
        elif alien_choice >= turret.spawn_rate[0] and alien_choice <= turret.spawn_rate[-1]:
            alien = "Turret"
            turret.spawn(door_choice)
        elif alien_choice >= armoured_wing.spawn_rate[0] and alien_choice <= armoured_wing.spawn_rate[-1]:
            alien = "Armoured wing"
            armoured_wing.spawn(door_choice)
        elif alien_choice >= sniper.spawn_rate[0] and alien_choice <= sniper.spawn_rate[-1]:
            alien = "Sniper"
            sniper.spawn(door_choice)
        elif alien_choice >= bomber.spawn_rate[0] and alien_choice <= bomber.spawn_rate[-1]:
            alien = "Bomber"
            bomber.spawn(door_choice)
        else:
            alien = "Mosquito"
            mosquito.spawn(door_choice)
        return alien

#This function gets the alien's position and the computer's choice of door and
#uses the door to set the alien's new position. After the position is set,
#self.alive is set to true because it will be used to show the alien in the
#frontend.

#Let me know what you think of this alternative Adam. I'd love to hear your
#thoughts on it.

#Note: positions are for testing only. They are not the correct values.
    def spawn(self, door_choice: int):
        if door_choice == 1:
            self.pos_x = 1
            self.pos_y = 800
        elif door_choice == 2:
            self.pos_x = 48
            self.pos_y = 92
        elif door_choice == 3:
            self.pos_x = 442
            self.pos_y = 10
        elif door_choice == 4:
            self.pos_x = 150
            self.pos_y = 232
        elif door_choice == 5:
            self.pos_x = 300
            self.pos_y = 500
        elif door_choice == 6:
            self.pos_x = 11
            self.pos_y = 200
        elif door_choice == 7:
            self.pos_x = 23
            self.pos_y = 62
        else:
            self.pos_x = 1200
            self.pos_y = 600
        self.alive = True

class RangedAliens(Aliens):
    pass

class PhysicalAliens(Aliens):
    pass

#class EnemySpawn():
#    def AlienCreator():
#        ListOfAliens = []
#
#        return ListOfAliens
#
#    def AlienDoorSpawn():
#        Door1 = pygame.Vector2(0, 1200)
#        Door2 = pygame.Vector2(0, 100)
#        Door3 = pygame.Vector2(1200, 50)
#        Door4 = pygame.Vector2(1200, 600)
#        
#        rand = random.randint(0, 3)
#        Location = None
#
#        if rand == 0:
#            return Door4
#        elif rand == 1:
#            return Door2
#        elif rand == 2:
#            return Door1
#        elif rand == 3:
#            return Door3
    #I created this sample class to handle the enemy spawns using the rarity system, as well as handle where
    #the enemies spawn to. I believe we should use door locations in the way that I have

class GameManager():
    __aliens_alive = []
    def __init__(self):
        pass

    @staticmethod
    def start_game():
        game_round = 0
        try:
            shield.convert_spawn_rate(True, None)
            turret.convert_spawn_rate(False, shield.spawn_rate)
            armoured_wing.convert_spawn_rate(False, turret.spawn_rate)
            sniper.convert_spawn_rate(False, armoured_wing.spawn_rate)
            bomber.convert_spawn_rate(False, sniper.spawn_rate)
            mosquito.convert_spawn_rate(False, bomber.spawn_rate)
        except:
            raise entryErrors("The spawn rates are incorrect")
        GameManager.manage_rounds(game_round)
        return game_round

    @staticmethod
    def manage_spawns(game_round: int):
        spawn_rate_total = len(shield.spawn_rate) + len(turret.spawn_rate) + len(armoured_wing.spawn_rate) + len(bomber.spawn_rate) + len(mosquito.spawn_rate) + len(sniper.spawn_rate)
        if spawn_rate_total == 100:
            aliens_needed = game_round * 5
            i = 0
            while(aliens_needed > i):
                alien = Aliens.random_spawn()
                GameManager.__aliens_alive.append(alien)
                i+= 1
            print(GameManager.__aliens_alive)
        else:
            raise numErrors("The spawn rates must add up to 100")

    @staticmethod
    def manage_rounds(game_round: int):
        if len(GameManager.__aliens_alive) == 0:
            game_round+= 1
            GameManager.manage_spawns(game_round)
        return game_round

#parameters - (health, speed, damage, is_alive, pos_x, pos_y, power_up)
player = Player(100, 2, 20, True, 1, 1, None)

#parameters - (health, speed, damage, is_alive, pos_x, pos_y, target, spawn_rate)
shield = Aliens(200, 1, 20, False, 1, 1, player, 25)
turret = Aliens(200, 1, 15, False, 1, 1, player, 10)
armoured_wing = Aliens(150, 2, 30, False, 1, 1, player, 15)
bomber = Aliens(30, 5, 100, False, 1, 1, player, 10)
mosquito = Aliens(50, 3, 50, False, 1, 1, player, 25)
sniper = Aliens(40, 1, 75, False, 1, 1, player, 15)

GameManager.start_game()
