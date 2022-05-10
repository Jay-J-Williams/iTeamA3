import pygame, sys, random

visible_sprites = pygame.sprite.Group()
obstacle_sprites = pygame.sprite.Group()
#----------------------------------------------------------------------------------------------------
#FRONT-END
class Settings:
    Width = 672
    Height = 672
    FPS = 60
    Tilesize = 32

    MAP = [
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c'], #1 | [0]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #2 | [1]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #3 | [2]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #4 | [3]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #5 | [4]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #6 | [5]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #7 | [6]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #8 | [7]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #9 | [8]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #10 | [9]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #11 | [10]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #12 | [11]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #13 | [12]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #14 | [13]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #15 | [14]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #16 | [15]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #17 | [16]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #18 | [17]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #19 | [18]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','fp','w'],#20 | [19]
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c']  #21 | [20]
    ]
#----------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        S = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode((S.Width, S.Height))
        pygame.display.set_caption("Solus Miles")

        self.clock = pygame.time.Clock()
        self.map = Map()
        self.FPS = S.FPS

    def run(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("black")
        self.map.run()
        pygame.display.update()
        self.clock.tick(self.FPS)
#----------------------------------------------------------------------------------------------------
class Map():
    def __init__(self):
        S = Settings()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.MAP = S.MAP
        self.TILESIZE = S.Tilesize
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE
                self.y = y
                self.x = x
                col = col.lower()
                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png"
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png"
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites])       

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites])
                #--------------------------------------------------------------------------------
                #Doors
                elif col == "d" and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png"
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])

                elif col == "d" and (row_index == 6 or row_index == 14) and col_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])

                elif col == "d" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])

                elif col == "d" and (row_index == 6 or row_index == 14) and col_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [visible_sprites, obstacle_sprites])
                #--------------------------------------------------------------------------------
                #Floor
                elif "f" in col:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image, [visible_sprites])      
                #--------------------------------------------------------------------------------
                #Player
                if "p" in col:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"
                    self.player = Player((x, y), image, visible_sprites, obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
#----------------------------------------------------------------------------------------------------
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)

class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)

    def ReturnImage(self):
        return self.image
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------#
#BACK-END

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
    __speed = None
    __health = None
    __damage = None
    __is_alive = None
    __pos_x = None
    __pos_y = None
    __image = None
    def __init__(self, health, speed, damage, is_alive, x, y, image):
        self.speed = speed
        self.health = health
        self.damage = damage
        self.is_alive = is_alive
        self.pos_x = x
        self.pos_y = y
        self.image =  image

        AreaSprite((self.pos_x, self.pos_y), image, [visible_sprites])

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

    @property
    def image(self):
        return self.__image

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

    @pos_x.setter
    def pos_x(self, value: int):
        if value > 0:
            self.__pos_x = value
        else:
            raise numErrors("pos_x must be a positive integer")

    @pos_y.setter
    def pos_y(self, value:int):
        if value > 0:
            self.__pos_y = value
        else:
            raise numErrors("pos_y must be a positive integer")

    @image.setter
    def image(self, value):
        if value != "":
            self.__image = value
        else:
            raise strErrors("Image must be a string of the path of the image")

class Player(Characters):
    __power_up = None
    __weapon = None
    def __init__(self, health, speed, damage, is_alive, pos_x, pos_y, image, power_up, weapon):
        super().__init__(health, speed, damage, is_alive, pos_x, pos_y, image)
        self.power_up = power_up
        self.weapon = weapon

    @property
    def power_up(self):
        return self.__power_up

    @property
    def weapon(self):
        return self.__weapon

    @power_up.setter
    def power_up(self, value: object):
        if value != "":
            self.__power_up = value 
        else:
            raise objectErrors("The power-up must be an object, or 'None'")

    @weapon.setter
    def weapon(self, value: object):
        if value != None and value != "":
            self.__weapon = value
        else:
            raise objectErrors("The weapon must be an object")

    def pickup_weapon(self):
        self.damage = self.weapon.damage

    def shoot(self, weapon: object, bullet: object):
        pass

    def delay(self, weapon: object):
        self.delay = 1000 / self.weapon.fire_rate
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
        if value > 0 and value <= 10:
            self.__fire_rate = value
        else:
            raise numErrors("You must enter an int from 1 to 10")

class Bullets():
    __speed = None
    __target = None
    __pos_x = None
    __pos_y = None

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
        return self.__pos_y

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

class Aliens(Characters):
    __target = None
    __spawn_rate = None
    __name = None

    def __init__(self, name, health, speed, damage, is_alive, pos_x, pos_y, target, spawn_rate):
        super().__init__(health, speed, damage, is_alive, pos_x, pos_y)
        self.target = target
        self.spawn_rate = spawn_rate
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def target(self):
        return self.__target

    @property
    def spawn_rate(self):
        return self.__spawn_rate

    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value
        else:
            raise strErrors("You must enter a name of an alien")
        
    @target.setter
    def target(self, value: object):
        self.__target = value

    @spawn_rate.setter
    def spawn_rate(self, value):
        self.__spawn_rate = value
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

    @staticmethod
    def random_spawn():
        alien_choice = random.randint(1, 100)
        door_choice = random.randint(1, 8)
        if alien_choice >= shield.spawn_rate[0] and alien_choice <= shield.spawn_rate[-1]:
            alien = GameManager.create_shield()
            shield.spawn(door_choice)
        elif alien_choice >= turret.spawn_rate[0] and alien_choice <= turret.spawn_rate[-1]:
            alien = GameManager.create_turret()
            turret.spawn(door_choice)
        elif alien_choice >= armoured_wing.spawn_rate[0] and alien_choice <= armoured_wing.spawn_rate[-1]:
            alien = GameManager.create_armoured_wing()
            armoured_wing.spawn(door_choice)
        elif alien_choice >= sniper.spawn_rate[0] and alien_choice <= sniper.spawn_rate[-1]:
            alien = GameManager.create_sniper()
            sniper.spawn(door_choice)
        elif alien_choice >= bomber.spawn_rate[0] and alien_choice <= bomber.spawn_rate[-1]:
            alien = GameManager.create_bomber()
            bomber.spawn(door_choice)
        else:
            alien = GameManager.create_mosquito()
            mosquito.spawn(door_choice)
        return alien

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
    def find_aliens(alien, lst, number):
        i = 0
        duplicate_aliens = 0
        while(i < len(lst)):
            if lst[i] == alien.name or lst[i] = alien.name+" "+str(number):
                duplicate_aliens+= 1
            i+= 1
        print(duplicate_aliens)
        return duplicate_aliens

    @staticmethod
    def remove_alien(alien, lst, number):
        lst.remove(alien+" "+number)
        alien.is_alive = False

    @staticmethod
    def manage_spawns(game_round: int):
        spawn_rate_total = len(shield.spawn_rate) + len(turret.spawn_rate) + len(armoured_wing.spawn_rate) + len(bomber.spawn_rate) + len(mosquito.spawn_rate) + len(sniper.spawn_rate)
        if spawn_rate_total == 100:
            aliens_needed = game_round * 5
            i = 1
            aliens_needed+= i
            while(aliens_needed > i):
                alien = Aliens.random_spawn()
                duplicate_aliens = GameManager.find_aliens(alien, GameManager.__aliens_alive, i)
                if duplicate_aliens > 0:
                    alien.name += str(duplicate_aliens + 1)
                GameManager.__aliens_alive.append(alien.name)
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

#parameters - (health, speed, damage, is_alive, pos_x, pos_y, target, spawn_rate)
    @staticmethod
    def create_shield():
        shield = Aliens("Shield", 200, 1, 20, False, 1, 1, player, 25)
        return shield

    @staticmethod
    def create_turret():
        turret = Aliens("Turret", 200, 1, 15, False, 1, 1, player, 10)
        return turret
    
    @staticmethod
    def create_armoured_wing():
        armoured_wing = Aliens("Armoured-wing", 150, 2, 30, False, 1, 1, player, 15)
        return armoured_wing
    
    @staticmethod
    def create_bomber():
        bomber = Aliens("Bomber", 30, 5, 100, False, 1, 1, player, 10)
        return bomber
    
    @staticmethod
    def create_mosquito():
        mosquito = Aliens("Mosquito", 50, 3, 50, False, 1, 1, player, 25)
        return mosquito
    
    @staticmethod
    def create_sniper():
        sniper = Aliens("Sniper", 40, 1, 75, False, 1, 1, player, 15)
        return sniper

#parameters - (name, damage, fire_rate(shots per second))
pistol = Weapons("Pistol", 20, 3)
shotgun = Weapons("Shotgun", 100, 1)
smg = Weapons("Sub-machine-gun", 10, 10)
rifle = Weapons("Rifle", 20, 5)

#parameters - (health, speed, damage, is_alive, pos_x, pos_y, power_up, weapon)
player = Player(100, 2, 20, True, 1, 1, "Assets\Player\Player_pistol.png", None, pistol)

shield = GameManager.create_shield()
turret = GameManager.create_turret()
armoured_wing = GameManager.create_armoured_wing()
bomber = GameManager.create_bomber()
mosquito = GameManager.create_mosquito()
sniper = GameManager.create_sniper()

GameManager.start_game()
class Character(pygame.sprite.Sprite):
    pass

class Player(Characters):
    def __init__(self, pos, image, groups, obstacles):
        super().__init__(groups)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacles = obstacles
        self.direction = pygame.math.Vector2(pos)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction.x -= 1
        elif keys[pygame.K_d]:
            self.direction.x += 1

        if keys[pygame.K_w]:
            self.direction.y -= 1
        elif keys[pygame.K_s]:
            self.direction.y += 1

    def update(self):
        Player.movement(self)
        self.rect = self.image.get_rect(topleft = self.direction)
#----------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------#
running = True
game = Game()

while running:
    game.run()