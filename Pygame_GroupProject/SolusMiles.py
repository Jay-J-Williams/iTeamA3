import pygame, sys, random

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

        self.Width = 1920
        self.Height = 1080
        self.Tilesize = 64
        self.FPS = 60

        # Size possibilities -
            # 1280 / 720  | Tilesize = 48
            # 1920 / 1080 | Tilesize = 64
            # 2560 / 1440 | Tilesize = 96 - So far, do not use
            # 3840 / 2160 | Tilesize = 128 - So far, do not use

        # Simply input the size you want to test
        # NOTE - This will change when a main menu is implemented

        # - Adam

        self.screen = pygame.display.set_mode((self.Width, self.Height), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()

        pygame.display.set_caption("Solus Miles")
        self.clock = pygame.time.Clock()

    #------------------------------------------------------
    def Create_Map(self):
        room = "Pygame_GroupProject\Assets\Room\Room.png"
        Room(room, self.Width, self.Height)
        global player
        player = GameManager.create_player(pistol)
        global shield
        shield = GameManager.create_shield(False)
        global turret
        turret = GameManager.create_turret(False)
        global armoured_wing
        armoured_wing = GameManager.create_armoured_wing(False)
        global bomber
        bomber = GameManager.create_bomber(False)
        global mosquito
        mosquito = GameManager.create_mosquito(False)
        global sniper
        sniper = GameManager.create_sniper(False)
        GameManager.manage_rounds(0)
        #GameManager.__aliens_alive.append(test_alien)
    #------------------------------------------------------
    def Run(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()

        self.screen.fill("Black")
        player.Update(self.Width, self.Height, self.Tilesize)
        GameManager.update_aliens()

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
        self.image = pygame.transform.scale(self.image, (tilesize, tilesize)) # <-- HERE | Scales to size
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
    pos_x = None
    pos_y = None
    image = None
    group = None
    size = None
    #------------------------------------------------------
    def __init__(self, health, speed, damage, pos_x, pos_y, image, group):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.org_image = image
        self.group = group
        self.size = game.Tilesize
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Player(Character):
    weapon = None
    powerUp = None
    #------------------------------------------------------
    def __init__(self, health, speed, damage, pos_x, pos_y, weapon, image, group):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
        self.weapon = weapon
        self.powerUp = None
        self.char = Sprite((pos_x, pos_y), image, group, self.size)
        self.rect = self.char.rect
    #------------------------------------------------------
    def Movement(self, width, height):
        keys = pygame.key.get_pressed()
        max_move = self.size * 2

        if keys[pygame.K_a] and self.pos_x > self.size:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_x -= self.speed           
        #------------------------------------------------------
        elif keys[pygame.K_d] and self.pos_x < (width - max_move):
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_x += self.speed
        #------------------------------------------------------
        elif keys[pygame.K_w] and self.pos_y > self.size:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_y -= self.speed
        #------------------------------------------------------
        elif keys[pygame.K_s] and self.pos_y < (height - max_move):
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_y += self.speed
    #------------------------------------------------------
    def Shoot(self, tilesize):
        keys = pygame.key.get_pressed()
        mouse_clicks = pygame.mouse.get_pressed()

        if keys[pygame.K_SPACE] or mouse_clicks[0]: # [0] = Left Click
            Bullet(self.pos_x, self.pos_y, tilesize)
    #------------------------------------------------------
    def Update(self, width, height, tilesize):
        self.Movement(width, height)  
        self.Shoot(tilesize)
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
                print("|-|-|-|")
                self.y += self.speed
                print("...Try_IT_Out...")
        except Exception as e:
            print(e)
            print("Fail")
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Aliens(Character):
    __target = None
    __spawn_rate = None
    __name = None

    def __init__(self, name, health, speed, damage, pos_x, pos_y, target, spawn_rate, image, group, showing):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
        self.target = target
        self.spawn_rate = spawn_rate
        self.name = name
        self.showing = showing
        if showing == True:
            self.char = Sprite((pos_x, pos_y), image, group, self.size)
            self.rect = self.char.rect

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
            alien = GameManager.create_shield(True)
        elif alien_choice >= turret.spawn_rate[0] and alien_choice <= turret.spawn_rate[-1]:
            alien = GameManager.create_turret(True)
        elif alien_choice >= armoured_wing.spawn_rate[0] and alien_choice <= armoured_wing.spawn_rate[-1]:
            alien = GameManager.create_armoured_wing(True)
        elif alien_choice >= sniper.spawn_rate[0] and alien_choice <= sniper.spawn_rate[-1]:
            alien = GameManager.create_sniper(True)
        elif alien_choice >= bomber.spawn_rate[0] and alien_choice <= bomber.spawn_rate[-1]:
            alien = GameManager.create_bomber(True)
        else:
            alien = GameManager.create_mosquito(True)
        alien.spawn(door_choice)
        return alien

    def spawn(self, door_choice: int): 
        # Door choices from left to top, in relation to the top-left corner (0,0)
        #------------------------------------------------------
        if door_choice == 1: # Left 1
            self.pos_x = 0 * game.Tilesize # 0 x tilesize
            self.pos_y = 5 * game.Tilesize # 5 x tilesize
        #------------------------------------------------------
        elif door_choice == 2: # Left 2
            self.pos_x = 0 * game.Tilesize # 0 x tilesize
            self.pos_y = 11 * game.Tilesize # 11 x tilesize
        #------------------------------------------------------
        elif door_choice == 3: # Bottom 1
            self.pos_x = 8 * game.Tilesize # 8 x tilesize
            self.pos_y = 16 * game.Tilesize # 16 x tilesize
        #------------------------------------------------------
        elif door_choice == 4: # Bottom 2 
            self.pos_x = 21 * game.Tilesize # 21 x tilesize
            self.pos_y = 16 * game.Tilesize # 16 x tilesize
        #------------------------------------------------------
        elif door_choice == 5: # Right 1 
            self.pos_x = 29 * game.Tilesize # 29 x tilesize
            self.pos_y = 5 * game.Tilesize # 5 x tilesize
        #------------------------------------------------------
        elif door_choice == 6: # Right 2
            self.pos_x = 29 * game.Tilesize # 29 x tilesize
            self.pos_y = 11 * game.Tilesize # 11 x tilesize
        #------------------------------------------------------
        elif door_choice == 7: # Top 1
            self.pos_x = 21 * game.Tilesize # 21 x tilesize
            self.pos_y = 0 * game.Tilesize # 0 x tilesize
        #------------------------------------------------------
        elif door_choice == 8: # Top 2
            self.pos_x = 8 * game.Tilesize # 8 x tilesize
            self.pos_y = 0 * game.Tilesize # 0 x tilesize
        #------------------------------------------------------
        print(door_choice)

#Physical attacker movement
    def move(self):
        #------------------------------------------------------
        if self.pos_x != player.pos_x:
             if self.pos_x < player.pos_x:
                    self.pos_x += self.speed * 0.5
        #------------------------------------------------------
             elif self.pos_x > player.pos_x:
                self.pos_x -= self.speed * 0.5
        #------------------------------------------------------
        if self.pos_y != player.pos_y:
             if self.pos_y > player.pos_y:
                self.pos_y -= self.speed * 0.5
        #------------------------------------------------------
             elif self.pos_y < player.pos_y:
                self.pos_y += self.speed * 0.5

# Door exiting
         #i = 0
         #if self.pos_x == 0 and self.pos_y == 5 * game.Tilesize: # Left 1
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 0 and self.pos_y == 11 * game.Tilesize: # Left 2
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 8 * game.Tilesize and self.pos_y == 16 * game.Tilesize: # Bottom 1
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 21 * game.Tilesize and self.pos_y == 16 * game.Tilesize: # Bottom 2
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 29 * game.Tilesize and self.pos_y == 5 * game.Tilesize: # Right 1
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 29 * game.Tilesize and self.pos_y == 11 * game.Tilesize: # Right 2
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 21 * game.Tilesize and self.pos_y == 0 * game.Tilesize: # Top 1
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #elif self.pos_x == 8 * game.Tilesize and self.pos_y == 0 * game.Tilesize: # Top 2
         #    while (i < len(GameManager.aliens_alive)):
         #        if GameManager.aliens_alive[i].pos_x != self.pos_x + game.Tilesize and GameManager.aliens_alive[i].pos_y != self.pos_y + game.Tilesize:
         #            can_move = True
         #        else:
         #            can_move = False
         #print(can_move)
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
    aliens_alive = []
    def __init__(self):
        pass

    @staticmethod
    def start_game():
        game_round = 0
        GameManager.convert_alien_spawn_rates()
        GameManager.manage_rounds(game_round)
        return game_round

    @staticmethod
    def find_aliens(alien):
        i = 0
        duplicate_aliens = 0
        while(i < len(GameManager.aliens_alive)):
            if alien.name in GameManager.aliens_alive[i].name:
                duplicate_aliens+= 1
            i += 1
        return duplicate_aliens

    @staticmethod
    def remove_alien(alien_name):
        i = 0
        while(i < len(GameManager.aliens_alive)):
            if GameManager.aliens_alive[i].name == alien_name:
                GameManager.aliens_alive[i].char.kill()
                del (GameManager.aliens_alive[i])
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
                if i > 1:
                    duplicate_aliens = GameManager.find_aliens(alien)
                    if duplicate_aliens > 0:
                        alien.name += str(duplicate_aliens + 1)
                GameManager.aliens_alive.append(alien)
                print(GameManager.aliens_alive[i - 1].pos_x, GameManager.aliens_alive[i - 1].pos_y)
                del(alien)
                print(GameManager.aliens_alive[i - 1])
                i+= 1
            #GameManager.remove_alien("Shield2")
            print("\n")
            i = 0
            while(i < len(GameManager.aliens_alive)):
                i+= 1
        else:
            raise numErrors("The spawn rates must add up to 100")

    @staticmethod
    def manage_rounds(game_round: int):
        if len(GameManager.aliens_alive) == 0:
            game_round+= 1
            GameManager.manage_spawns(game_round)
        return game_round

    @staticmethod
    def update_aliens():
        i = 0
        while(i < len(GameManager.aliens_alive)):
            GameManager.aliens_alive[i].char.kill()
            GameManager.aliens_alive[i].char = ImageTransformer(GameManager.aliens_alive[i].org_image, 0)
            GameManager.aliens_alive[i].char = GameManager.aliens_alive[i].char.ReturnImage((GameManager.aliens_alive[i].pos_x, GameManager.aliens_alive[i].pos_y), GameManager.aliens_alive[i].group, GameManager.aliens_alive[i].size)
            GameManager.aliens_alive[i].move()
            i+= 1


#parameters - (health, speed, damage, pos_x, pos_y, target, spawn_rate, image, groups, game width, game height)
    @staticmethod
    def create_shield(showing):
        shield = Aliens("Shield", 200, 2, 20, 100, 100, player, 25, "Pygame_GroupProject\Assets\Aliens\\Normal\Shield_Armour.png", [entities], showing)
        shield.convert_spawn_rate(True, None)
        return shield

    @staticmethod
    def create_turret(showing):
        turret = Aliens("Turret", 200, 2, 15, 200, 200, player, 10, "Pygame_GroupProject\Assets\Aliens\\Normal\Turret.png", [entities], showing)
        turret.convert_spawn_rate(False, shield.spawn_rate)
        return turret
    
    @staticmethod
    def create_armoured_wing(showing):
        armoured_wing = Aliens("Armoured-wing", 150, 3, 30, 300, 300, player, 15, "Pygame_GroupProject\Assets\Aliens\\Normal\Armoured_Wing.png", [entities], showing)
        armoured_wing.convert_spawn_rate(False, turret.spawn_rate)
        return armoured_wing
    
    @staticmethod
    def create_bomber(showing):
        bomber = Aliens("Bomber", 30, 6, 100, 400, 400, player, 10, "Pygame_GroupProject\Assets\Aliens\\Normal\Bomber.png", [entities], showing)
        bomber.convert_spawn_rate(False, armoured_wing.spawn_rate)
        return bomber
    
    @staticmethod
    def create_mosquito(showing):
        mosquito = Aliens("Mosquito", 50, 5, 50, 500, 500, player, 25, "Pygame_GroupProject\Assets\Aliens\\Normal\Mosquito.png", [entities], showing)
        mosquito.convert_spawn_rate(False, bomber.spawn_rate)
        return mosquito
    
    @staticmethod
    def create_sniper(showing):
        sniper = Aliens("Sniper", 40, 1, 75, 600, 600, player, 15, "Pygame_GroupProject\Assets\Aliens\\Normal\Sniper.png", [entities], showing)
        sniper.convert_spawn_rate(False, mosquito.spawn_rate)
        return sniper

#parameters - (health, speed, damage, pos_x, pos_y, power_up, weapon, image, groups)
    @staticmethod
    def create_player(weapon: object):
        if weapon == pistol:
            image = "Pygame_GroupProject\Assets\Player\Player.png"
        
        elif weapon == shotgun:
            image = "Pygame_GroupProject\Assets\Player\Player.png"

        elif weapon == smg:
            image = "Pygame_GroupProject\Assets\Player\Player.png"

        elif weapon == rifle:
            image = "Pygame_GroupProject\Assets\Player\Player.png"

        else:
            raise entryErrors("You must enter a weapon object")
        player = Player(100, 3, 20, (game.Width / 2), (game.Height / 2), weapon, image, [entities])

        return player
#----------------------------------------------------------------------------------------------------
pistol = Weapon(20, 3, 30)
shotgun = Weapon(100, 1, 10)
smg = Weapon(10, 10, 20)
rifle = Weapon(20, 5, 50)

game = Game()
game.Create_Map()

while True:
    game.Run()
