import pygame, sys

background = pygame.sprite.Group() #Room
entities = pygame.sprite.Group() #Player/Aliens
bullets = pygame.sprite.Group() #Bullets
Bulls = []

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
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        pygame.init()

        self.Width = 1280
        self.Height = 720
        self.Tilesize = 48
        self.FPS = 60

        # Size possibilities -
            # 1280 / 720  | Tilesize = 48
            # 1920 / 1080 | Tilesize = 64
            # 2560 / 1440 | Tilesize = 96
            # 3840 / 2160 | Tilesize = 128

        # Simply input the size you want to test
        # NOTE - This will change when a main menu is implemented

        # - Adam

        self.screen = pygame.display.set_mode((self.Width, self.Height), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()

        pygame.display.set_caption("Solus Miles")
        self.clock = pygame.time.Clock()

        self.Create_Map()
    #------------------------------------------------------
    def Create_Map(self):
        room = "Pygame_GroupProject\Assets\Room\Room.png"
        Room(room, self.Width, self.Height)

        image = "Pygame_GroupProject\Assets\Player\Player.png"
        global player
        player = Player(100, 5, 20, (self.Width / 2), (self.Height / 2), image, [entities], self.Tilesize)
    #------------------------------------------------------
    def Run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("Black")
        player.Update(self.Width, self.Height, self.Tilesize)

        for b in Bulls:
            b.Move(self.Height)

        background.draw(self.display_surface)
        entities.draw(self.display_surface)
        bullets.draw(self.display_surface)
        pygame.display.update()

        self.clock.tick(self.FPS)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, tilesize):
        super().__init__(groups)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale(self.image, (tilesize, tilesize))
        self.rect = self.image.get_rect(topleft = pos)
# This class will not be dealing with the background (room) anymore
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Room(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super().__init__(background)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (0,0))
# This class has been made to handle the background (room)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)
    #------------------------------------------------------
    def ReturnImage(self, pos, groups, size):
        return Sprite(pos, self.image, groups, size)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Character():
    health = None
    speed = None
    damage = None
    x = None
    y = None
    image = None
    groups = None
    size = None
    #------------------------------------------------------
    def __init__(self, health, speed, damage, x, y, image, groups, tilesize):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.x = x
        self.y = y
        self.org_image = image
        self.groups = groups
        self.size = tilesize
        self.char = Sprite((x, y), image, groups, tilesize)
        self.rect = self.char.rect
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Player(Character):
    weapon = None
    powerUp = None
    #------------------------------------------------------
    def __init__(self, health, speed, damage, x, y, image, group, size):
        super().__init__(health, speed, damage, x, y, image, group, size)
        self.weapon = None
        self.powerUp = None
    #------------------------------------------------------
    def Movement(self, width, height):
        keys = pygame.key.get_pressed()
        max_move = self.size * 2

        if keys[pygame.K_a] and self.x > self.size:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups, self.size)
            self.x -= self.speed           
        #------------------------------------------------------
        elif keys[pygame.K_d] and self.x < (width - max_move):
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups, self.size)
            self.x += self.speed
        #------------------------------------------------------
        elif keys[pygame.K_w] and self.y > self.size:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups, self.size)
            self.y -= self.speed
        #------------------------------------------------------
        elif keys[pygame.K_s] and self.y < (height - max_move):
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups, self.size)
            self.y += self.speed
    #------------------------------------------------------
    def Shoot(self, tilesize):
        keys = pygame.key.get_pressed()
        mouse_clicks = pygame.mouse.get_pressed()

        if keys[pygame.K_SPACE] or mouse_clicks[0]: # [0] = Left Click
            Bullet(self.x, self.y, tilesize)
            self.weapon.isShot = True
    #------------------------------------------------------
    def Update(self, width, height, tilesize):
        self.Movement(width, height)      
        #self.Shoot(tilesize)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Weapon():
    damage = None 
    fireRate = None 
    shotRange = None 
    isShot = None
    #------------------------------------------------------
    def __init__(self, damage, fireRate, shotRange):
        self.damage = damage
        self.fireRate = fireRate
        self.shotRange = shotRange
        self.isShot = False
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Bullet(pygame.sprite.Sprite):   
    x = None
    y = None
    speed = None
    image = None
    #------------------------------------------------------
    def __init__(self, x, y, tilesize):
        self.x = x
        self.y = y
        self.speed = 20
        self.size = tilesize
        self.image = "Pygame_GroupProject\Assets\Bullet\Bullet.png"
        self.char = Sprite(((x + 24 / 2), (y + 24 / 2)), self.image, [bullets], (tilesize / 4))
        self.rect = self.char.rect

        Bulls.append(self)
    #------------------------------------------------------
    def Move(self, height):
        max_size = self.size * 2
        try:
            if self.y < (height - max_size):
                self.y += self.speed
        except Exception as e:
            print(e)
            print("Fail")
#--------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Aliens(Character):
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
