import pygame, sys, random

background = pygame.sprite.Group() #Walls/Corners/Floors
Entities = pygame.sprite.Group() #Player/Aliens

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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #20 | [19]
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c']  #21 | [20]
    ]

    entities = [
    ['','','','','','','','','','','','','','','','','','','','',''], #1 | [0]
    ['','','','','','','','','','','','','','','','','','','','',''], #2 | [1]
    ['','','','','','','','','','','','','','','','','','','','',''], #3 | [2]
    ['','','','','','','','','','','','','','','','','','','','',''], #4 | [3]
    ['','','','','','','','','','','','','','','','','','','','',''], #5 | [4]
    ['','','','','','','','','','','','','','','','','','','','',''], #6 | [5]
    ['','','','','','','','','','','','','','','','','','','','',''], #7 | [6]
    ['','','','','','','','','','','','','','','','','','','','',''], #8 | [7]
    ['','','','','','','','','','','','','','','','','','','','',''], #9 | [8]
    ['','','','','','','','','','','','','','','','','','','','',''], #10 | [9]
    ['','','','','','','','','','','p','','','','','','','','','',''],#11 | [10]
    ['','','','','','','','','','','','','','','','','','','','',''], #12 | [11]
    ['','','','','','','','','','','','','','','','','','','','',''], #13 | [12]
    ['','','','','','','','','','','','','','','','','','','','',''], #14 | [13]
    ['','','','','','','','','','','','','','','','','','','','',''], #15 | [14]
    ['','','','','','','','','','','','','','','','','','','','',''], #16 | [15]
    ['','','','','','','','','','','','','','','','','','','','',''], #17 | [16]
    ['','','','','','','','','','','','','','','','','','','','',''], #18 | [17]
    ['','','','','','','','','','','','','','','','','','','','',''], #19 | [18]
    ['','','','','','','','','','','','','','','','','','','','',''], #20 | [19]
    ['','','','','','','','','','','','','','','','','','','','','']  #21 | [20]
    ]
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        S = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode((S.Width, S.Height))
        pygame.display.set_caption("Solus Miles")

        self.clock = pygame.time.Clock()
        self.map = Map()
        self.FPS = S.FPS
        global player
        player = GameManager.create_player(pistol)
        #global shield
        #shield = GameManager.create_shield()
        #global turret
        #turret = GameManager.create_turret()
        #global armoured_wing
        #armoured_wing = GameManager.create_armoured_wing()
        #global sniper
        #sniper = GameManager.create_sniper()
        #global bomber
        #bomber = GameManager.create_bomber()
        #global mosquito
        #mosquito = GameManager.create_mosquito()

    def run(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("black")
        self.map.run()
        self.clock.tick(self.FPS)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Map():
    def __init__(self):
        S = Settings()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.MAP = S.MAP
        self.Ent = S.entities
        self.TILESIZE = S.Tilesize
        self.create_map()
        #self.animation = Animations()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                col = col.lower()
                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png"
                    AreaSprite((x, y), image, [background])

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 90)
                    image = image.ReturnImage((x, y), [background])

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 180)
                    image = image.ReturnImage((x, y), [background])

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 270)
                    image = image.ReturnImage((x, y), [background])
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png"
                    AreaSprite((x, y), image, [background])

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 90)
                    image = image.ReturnImage((x, y), [background])     

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 180)
                    image = image.ReturnImage((x, y), [background])

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 270)
                    image = image.ReturnImage((x, y), [background])
                #--------------------------------------------------------------------------------
                #Floor
                elif col == "f":
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image, [background])  
                #--------------------------------------------------------------------------------

        for row_index, row in enumerate(self.Ent):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                if col == "p":
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"
                    #global player
                    #player = Player(100, 5, 20, x, y, pistol, image)

    def run(self):
        player.Update()
        #self.animation.Update()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        print(image)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees = 0):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)

    def ReturnImage(self, pos, groups):
        return AreaSprite(pos, self.image, groups)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Characters():
    __speed = None
    __health = None
    __damage = None

    __pos_x = None
    __pos_y =  None
    __image = None

    def __init__(self, health, speed, damage, pos_x, pos_y, image, group):
        self.speed = speed
        self.health = health
        self.damage = damage

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image
        self.groups = group

        self.char = AreaSprite((self.pos_x, self.pos_y), image, group)
        self.rect = self.char.rect

        self.map = Map()
        self.display_surf = self.map.display_surface

    #-------------------------------------------------- Getter
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
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @property
    def image(self):
        return self.__image

    #-------------------------------------------------- Setter

    @speed.setter
    def speed(self, value):
        if type(value) == int and value > 0:
            self.__speed = value
        else:
            raise numErrors("Movement Speed has to be a positive int")
        
    @health.setter
    def health(self, value):
        if type(value) == int and value > 0:
            self.__health = value
        else:
            raise numErrors("Health must be a positive int")
        
    @damage.setter
    def damage(self, value: int):
        if type(value) == int and value > 0:
            self.__damage = value
        else:
            raise numErrors("Damage must be a positive int")

    @pos_x.setter
    def pos_x(self, value: int):
        if type(value) == int and value > 0:
            self.__pos_x = value
        else:
            raise numErrors("pos_x must be a positive integer")

    @pos_y.setter
    def pos_y(self, value:int):
        if type(value) == int and value > 0:
            self.__pos_y = value
        else:
            raise numErrors("pos_y must be a positive integer")

    @image.setter
    def image(self, value):
        if value != "":
            self.__image = value
        else:
            raise strErrors("Image must be a string of the path of the image")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Player(Characters):
    __power_up = None
    __weapon = None
    def __init__(self, health, speed, damage, pos_x, pos_y, weapon, image, group):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
        self.group = group
        self.weapon = weapon
        self.rect = self.char.rect

    @property
    def power_up(self):
        return self.__power_up

    @property
    def weapon(self):
        return self.__weapon

    @power_up.setter
    def power_up(self, value: object):
        if value == None or type(value) == object:
            self.__power_up = value
        else:
            raise objectErrors("The power-up must be an object, or 'None'")

    @weapon.setter
    def weapon(self, value: object):
        if value != None:
            self.__weapon = value
        else:
            raise objectErrors("The weapon must be an object")

    def pickup_weapon(self, weapon):
        self.weapon = weapon
        self.damage = self.weapon.damage

    def shoot(self):
        pass

    def delay(self):
        self.delay = 1000 / self.weapon.fire_rate
        pygame.time.wait(self.delay)

    def Movement(self):
        #print("test")
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.pos_x > 32:
            self.char.kill()
            self.char = ImageTransformer(self.image, 270)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group)
            self.pos_x -= self.speed    

        elif keys[pygame.K_d] and self.pos_x < 608:
            self.char.kill()
            self.char = ImageTransformer(self.image, 90)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group)
            self.pos_x += self.speed

        elif keys[pygame.K_w] and self.pos_y > 32:
            self.char.kill()
            self.char = ImageTransformer(self.image, 180)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group)
            self.pos_y -= self.speed

        elif keys[pygame.K_s] and self.pos_y < 608:
            self.char.kill()
            self.char = ImageTransformer(self.image, 0)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group)
            self.pos_y += self.speed

        background.draw(self.display_surf)
        Entities.draw(self.display_surf)
        pygame.display.update()

    def Collision(self):
        #enHit = pygame.sprite.spritecollide(self, obstacle_sprites, False)
        #Use for enemies
        pass

    def WeaponChanger(self):
        if self.weapon == pistol:
            self.image = "Pygame_GroupProject\Assets\Player\Player_pistol.png"
        elif self.weapon == smg:
            self.image = "Pygame_GroupProject\Assets\Player\Player_smg.png"
        elif self.weapon == rifle:
            self.image = "Pygame_GroupProject\Assets\Player\Player_rifle.png"
        elif self.weapon == shotgun:
            self.image = "Pygame_GroupProject\Assets\Player\Player_shotgun.png"

        self.direction.kill()
        self.direction = AreaSprite((self.x, self.y), self.image, Entities)

    def Update(self):
        self.Movement()
        self.Collision()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        if type(value) == int:
            if value > 0:
                self.__damage = value
        else:
            raise numErrors("You must enter a positive int")
    @fire_rate.setter
    def fire_rate(self, value: int):
        if type(value) == int:
            if value > 0 and value <= 10:
                self.__fire_rate = value
        else:
            raise numErrors("You must enter an int from 1 to 10")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        if value != "" and type(value) == str:
            self.__asset = value
        else:
            raise strErrors("You must enter a string")

    @showing.setter
    def showing(self, value: bool):
        if type(value) == bool:
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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Aliens(Characters):
    __target = None
    __spawn_rate = None
    __name = None

    def __init__(self, name, health, speed, damage, pos_x, pos_y, target, spawn_rate, image, group):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
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
        if "Shield" in value or "Turret" in value:
            self.__name = value
        elif "Armoured-wing" in value or "Bomber" in value:
            self.__name = value
        elif "Sniper" in value or "Mosquito" in value:
            self.__name = value
        else:
            raise strErrors("You must enter a name of an alien")
            
        
    @target.setter
    def target(self, value: object):
        if type(value) == object:
            self.__target = value
        else:
            objectErrors("Target must be an object")

    @spawn_rate.setter
    def spawn_rate(self, value):
        if type(value) == list or type(value) == int:
            self.__spawn_rate = value
        else:
            entryErrors("The spawn rate must be initialised as an int, then turned into a list")

    def __str__(self):
        return self.__name

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
            self.pos_x = 7
            self.pos_y = 0
        elif door_choice == 2:
            self.pos_x = 25
            self.pos_y = 0
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
            self.pos_x = 0
            self.pos_y = 7
        else:
            self.pos_x = 0
            self.pos_y = 25

    def move(self):
        if self.pos_x - self.target.pos_x > self.pos_y - self.target.pos_y:
            if self.target.pos_x > Settings.Width / 2:
                while(self.pos_x < self.target.pos_x):
                    self.pos_x += self.speed
            elif self.target.pos_x < Settings.Width / 2:
                while(self.pos_x > self.target.pos_x):
                    self.pos_x -= self.speed
        elif self.pos_y - self.target.pos_y > self.pos_x - self.target.pos_x:
            if self.target.pos_y > Settings.Height / 2:
                while(self.pos_y > self.target.pos_y):
                    self.pos_y -= self.speed
            elif self.target.pos_y < Settings.Height / 2:
                while(self.pos_y < self.target.pos_y):
                    self.pos_y += self.speed
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class RangedAliens(Aliens):
    pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class PhysicalAliens(Aliens):
    pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class GameManager():
    __aliens_alive = []
    def __init__(self):
        pass

    @staticmethod
    def start_game():
        game_round = 0
        GameManager.convert_alien_spawn_rates()
        GameManager.manage_rounds(game_round)
        return game_round

    @staticmethod
    def convert_alien_spawn_rates():
        try:
            shield.convert_spawn_rate(True, None)
            turret.convert_spawn_rate(False, shield.spawn_rate)
            armoured_wing.convert_spawn_rate(False, turret.spawn_rate)
            sniper.convert_spawn_rate(False, armoured_wing.spawn_rate)
            bomber.convert_spawn_rate(False, sniper.spawn_rate)
            mosquito.convert_spawn_rate(False, bomber.spawn_rate)
        except:
            raise entryErrors("The spawn rates are incorrect")

    @staticmethod
    def find_aliens(alien, lst):
        i = 0
        duplicate_aliens = 0
        while(i < len(lst)):
            if alien.name in lst[i].name:
                duplicate_aliens+= 1
            i+= 1
        return duplicate_aliens

    @staticmethod
    def remove_alien(alien_name, lst):
        i = 0
        while(i < len(lst)):
            if lst[i].name == alien_name:
                del lst[i]
            i+= 1

    @staticmethod
    def manage_spawns(game_round: int):
        spawn_rate_total = len(shield.spawn_rate) + len(turret.spawn_rate) + len(armoured_wing.spawn_rate) + len(bomber.spawn_rate) + len(mosquito.spawn_rate) + len(sniper.spawn_rate)
        if spawn_rate_total == 100:
            aliens_needed = game_round * 5
            i = 1
            aliens_needed+= i
            while(aliens_needed > i):
                alien = Aliens.random_spawn()
                duplicate_aliens = GameManager.find_aliens(alien, GameManager.__aliens_alive)
                if duplicate_aliens > 0:
                    alien.name += str(duplicate_aliens + 1)
                GameManager.__aliens_alive.append(alien)
                del(alien)
                print(GameManager.__aliens_alive[i - 1])
                i+= 1
            GameManager.remove_alien("Shield2", GameManager.__aliens_alive)
            print("\n")
            i = 0
            while(i < len(GameManager.__aliens_alive)):
                print(GameManager.__aliens_alive[i])
                i+= 1
        else:
            raise numErrors("The spawn rates must add up to 100")

    @staticmethod
    def manage_rounds(game_round: int):
        if len(GameManager.__aliens_alive) == 0:
            game_round+= 1
            GameManager.manage_spawns(game_round)
        return game_round

#parameters - (health, speed, damage, pos_x, pos_y, target, spawn_rate, image, groups)
    @staticmethod
    def create_shield():
        shield = Aliens("Shield", 200, 1, 20, 1, 1, player, 25, "Pygame_GroupProject\Pygame_GroupProject\Assets\Alien\Shield_armour.png", [Entities])
        return shield

    @staticmethod
    def create_turret():
        turret = Aliens("Turret", 200, 1, 15, 1, 1, player, 10, "Pygame_GroupProject\Pygame_GroupProject\Assets\Alien\turret.png", [Entities])
        return turret
    
    @staticmethod
    def create_armoured_wing():
        armoured_wing = Aliens("Armoured-wing", 150, 2, 30, 1, 1, player, 15, "Pygame_GroupProject\Pygame_GroupProject\Assets\Alien\armoured_wing.png", [Entities])
        return armoured_wing
    
    @staticmethod
    def create_bomber():
        bomber = Aliens("Bomber", 30, 5, 100, 1, 1, player, 10, "Pygame_GroupProject\Pygame_GroupProject\Assets\Alien\bomber.png", [Entities])
        return bomber
    
    @staticmethod
    def create_mosquito():
        mosquito = Aliens("Mosquito", 50, 3, 50, 1, 1, player, 25, "Pygame_GroupProject\Pygame_GroupProject\Assets\Alien\mosquito.png", [Entities])
        return mosquito
    
    @staticmethod
    def create_sniper():
        sniper = Aliens("Sniper", 40, 1, 75, 1, 1, player, 15, "Pygame_GroupProject\Pygame_GroupProject\Assets\Alien\sniper.png", [Entities])
        return sniper

#parameters - (health, speed, damage, pos_x, pos_y, power_up, weapon, image, groups)
    @staticmethod
    def create_player(weapon: object):
        if weapon == pistol:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"
        
        elif weapon == shotgun:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_shotgun.png"

        elif weapon == smg:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_smg.png"

        elif weapon == rifle:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_rifle.png"

        else:
            raise entryErrors("You must enter a weapon object")
        player = Player(100, 2, 20, 112, 112, weapon, image, [Entities])

        return player
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#parameters - (name, damage, fire_rate(shots per second))
pistol = Weapons("Pistol", 20, 3)
shotgun = Weapons("Shotgun", 100, 1)
smg = Weapons("Sub-machine-gun", 10, 10)
rifle = Weapons("Rifle", 20, 5)
#----------------------------------------------------------------------------------------------------#

#player = Player(100, 2, 20, 1, 1, None, pistol, "Pygame_GroupProject\Assets\Player\Player_pistol.png", None)
#----------------------------------------------------------------------------------------------------
#shield = GameManager.create_shield()
#turret = GameManager.create_turret()
#armoured_wing = GameManager.create_armoured_wing()
#sniper = GameManager.create_sniper()
#bomber = GameManager.create_bomber()
#mosquito = GameManager.create_mosquito()
#GameManager.start_game()
#----------------------------------------------------------------------------------------------------#
#running = True
game = Game()
running = True
while running:
    game.run()
