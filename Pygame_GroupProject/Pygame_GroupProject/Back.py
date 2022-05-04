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
    def __init__(self, health, speed, dmg):
        self.speed = speed
        self.health = health
        self.damage = dmg

    @property
    def speed(self):
        return self.__speed
    @property
    def health(self):
        return self.__health
    @property
    def damage(self):
        return self.__damage

    @speed.setter
    def speed(self, value):
        try:
            if type(value) == "int":
                if value > 0:
                    self.__movement_speed = value
        except:
            raise numErrors("Movement Speed has to be whole numbers, and above 0")
    @health.setter
    def health(self, value):
        try:
            if type(value) == "int":
                if value > 0:
                    self.__health = value
        except:
            raise numErrors("Health has to be whole numbers, and above 0")
    @damage.setter
    def damage(self, value):
        try:
            if type(value) == "int":
                if value > 0:
                    self.__damage = value
        except:
            raise numErrors("Damage has to be whole numbers, and above 0")

class Player(Characters):
    __power_up = None
    def __init__(self, health, speed, damage):
        super().__init__(health, speed, damage)
        self.power_up = None      

    @property
    def power_up(self):
        return self.__power_up
    @power_up.setter
    def power_up(self, value):
        try:
            if type(value) == "str":
                self.__power_up = value 
        except:
            raise strErrors("You must enter a string")

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
    def name(self, value):
        try:
            if value == "Pistol" or value == "Shotgun":
                self.__name = value
            elif value == "Sub-machine-gun" or value == "Rifle":
                self.__name = value
        except:
            raise strErrors("You must enter 'Pistol', 'Shotgun', 'Sub-machine-gun', or 'Rifle'")
    @damage.setter
    def damage(self, value):
        try:
            if type(value) == "int":
                if type(value) > 0:
                    self.__damage = value
        except:
            raise numErrors("Damage must be an integer, positive number")
    @fire_rate.setter
    def fire_rate(self, value):
        try:
            if type(value) == "int":
                if value > 0 and value < 10:
                    self.__fire_rate = value
        except:
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
    __bulletPos = pygame.Vector2(0, 0) #Like player, I have changed this to better suit the code of the game 
                                        #- Adam

    def __init__(self, asset, speed, target, x, y):
        self.asset = asset
        self.speed = speed
        self.target = target
        self.bulletPos = pygame.Vector2(x, y)

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
    def bulletPos(self):
        return self.__bulletPos

    @asset.setter
    def asset(self, value):
        try:
            if type(value) == "str":
                self.__asset = value
        except:
            raise strErrors("You must enter a string")

    @showing.setter
    def showing(self, value):
        try:
            if type(value) == "bool":
                self.__showing = value
        except:
            raise boolErrors("You must enter a boolean value")

    @speed.setter
    def speed(self, value):
        try:
            if type(value) == "int":
                if value > 0:
                    self.__speed = value
        except:
            raise numErrors("You must enter an integer that is greater than zero")

    @target.setter
    def target(self, value):
        try:
            if type(value) == "str":
                self.__target = value
        except:
            raise strErrors("You must enter a string")

    @bulletPos.setter
    def bulletPos(self, x, y):
        try:
            if type(x) == "int" and type(y) == "int":
                if x > 0 and y > 0:
                    self.__bulletPos = (x, y)
        except:
            raise numErrors("You must enter two integers that are greater than zero")

#bullet = Bullets()
#This variable will be created in the front-end, every single time the key "enter" is pressed, because the
#player has to first interact with the game to spawn a bullet, they are created in the front. - Adam

class Aliens(Characters):
    __target = None
#I have added the spawn rate into the Aliens class because it will be a
#necessary value for each alien.
    __spawn_rate = None

    def __init__(self, x, y, health, speed, damage, target, spawn_rate):
        super().__init__(x, y, health, speed, damage)
        self.target = target
        self.spawn_rate = spawn_rate

    @property
    def target(self):
        return self.__target

    @property
    def spawn_rate(self):
        return self.__spawn_rate
        
    @target.setter
    def target(self, value):
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
            self.spawn_rate = list(range(1, self.spawn_rate))
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

    @staticmethod
    def rando_spawn(shieldSpawn, turretSpawn, wingSpawn, sniperSpawn, bomberSpawn, mosquitoSpawn, total):
        i = 0

        while i < total:
            alien = random.randint(0, 100)

            if alien == range(shieldSpawn[0], shieldSpawn[-1]):
                yield shield
            elif alien == range(turretSpawn[0], turretSpawn[-1]):
                yield turret
            elif alien == range(wingSpawn[0], wingSpawn[-1]):
                yield wing 
            elif alien == range(sniperSpawn[0], sniperSpawn[-1]):
                yield sniper 
            elif alien == range(bomberSpawn[0], bomberSpawn[-1]):
                yield bomber 
            elif alien == range(mosquitoSpawn[0], mosquitoSpawn[-1]):
                yield mosquito 

            i += 1

    @staticmethod
    def random_spawn(shield.spawn_rate, turret.spawn_rate, armoured_wing.spawn_rate, sniper.spawn_rate, bomber.spawn_rate, mosquito.spawn_rate):
        alien_choice = random.randint(1, 100)
        door_choice = random.randint(1, 8)
        if alien_choice == range(shield.spawn_rate[0], shield.spawn_rate[-1]):
            shield.spawn(door_choice)
        elif alien_choice == range(turret.spawn_rate[0], turret.spawn_rate[-1]):
            turret.spawn(door_choice)
        elif alien_choice == range(armoured_wing.spawn_rate[0], armoured_wing.spawn_rate[-1]):
            armoured_wing.spawn(door_choice)
        elif alien_choice == range(sniper.spawn_rate[0], sniper.spawn_rate[-1]):
            sniper.spawn(door_choice)
        elif alien_choice == range(bomber.spawn_rate[0], bomber.spawn_rate[-1]):
            bomber.spawn(door_choice)
        else:
            mosquito.spawn(door_choice)

#This function gets the alien's position and the computer's choice of door and
#uses the door to set the alien's new position. After the position is set,
#self.alive is set to true because it will be used to show the alien in the
#frontend.

#Let me know what you think of this alternative Adam. I'd love to hear your
#thoughts on it.
    def spawn(self, door):
        if door == 1:
            self.character_pos = (0, 1200)
        elif door == 2:
            self.character_pos = (0, 100)
        elif door == 3:
            self.character_pos = (1200, 50)
        elif door == 4:
            self.character_pos = (20, 22)
        elif door == 5:
            self.character_pos = (20, 22)
        elif door == 6:
            self.character_pos = (20, 22)
        elif door == 7:
            self.character_pos = (20, 22)
        else:
            self.character_pos = (1200, 600)
        self.alive = True

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

class GameManager():
    aliens_alive = []
    def __init__(self):
        pass

    @staticmethod
    def start_game():
        round = 1
        player = Player()
        try:
            shield.convert_spawn_rate(True, 0)
            turret.convert_spawn_rate(False, shield.spawn_rate)
            armoured_wing.convert_spawn_rate(False, armoured_wing.spawn_rate)
            sniper.convert_spawn_rate(False, sniper.spawn_rate)
            bomber.convert_spawn_rate(False, bomber.spawn_rate)
            mosquito.convert_spawn_rate(False, mosquito.spawn_rate)
        except:
            raise entryErrors("The spawn rates are incorrect")
        manage_spawns(round)
        return round

    @staticmethod
    def manage_spawns(round):
        aliens_needed = round * 5
        i = 0
        while(aliens_needed > i):
            Aliens.random_spawn(shield.spawn_rate, turret.spawn_rate, armoured_wing.spawn_rate, sniper.spawn_rate, bomber.spawn_rate, mosquito.spawn_rate)
            i+= 1

    @staticmethod
    def manage_rounds(round):
        if len(aliens_alive) = 0:
            round+= 1
            manage_spawns(round)
        return round

    @staticmethod
    def manage_aliens():
        
