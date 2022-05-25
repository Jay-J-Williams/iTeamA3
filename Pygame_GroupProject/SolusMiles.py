import pygame, sys, random, gc
pygame.init()

background = pygame.sprite.Group() #Room | For visible spawning
menu_screen = pygame.sprite.Group() # For the menu
entities = pygame.sprite.Group() #Player/Aliens | For visible spawning
aliens = pygame.sprite.Group() #Aliens | For collisions
bullets = pygame.sprite.Group() #Bullets | For visible spawning
hud_components = pygame.sprite.Group()
power_ups = pygame.sprite.Group()
power_ups_lst = []
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
class Menu:
    def __init__(self, height):
        self.Height = height

        if self.Height == 720:
            self.Width = 1280
            self.size = 48
        elif self.Height == 1080:
            self.Width = 1920
            self.size = 64 

        self.difficulty = "Normal"

        self.screen = pygame.display.set_mode((self.Width, self.Height), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.running = True

    def StartUp(self):
        room = "Pygame_GroupProject/Assets/Room/Menu.png"
        Room(room, self.Width, self.Height, menu_screen)

    def Update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.running = False
            game.running = True

    def Run(self):
        self.screen.fill("black")
        self.Update()
        menu_screen.draw(self.display_surface)

        pygame.display.update()
        self.clock.tick(self.FPS)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self, height, difficulty):
        self.difficulty = difficulty
        self.Height = height
        #------------------------------------------------------
        if self.Height == 720:
            self.Width = 1280
            self.Tilesize = 43
        #------------------------------------------------------
        elif self.Height == 1080:
            self.Width = 1920
            self.Tilesize = 64
        #------------------------------------------------------
        else:
            raise numErrors("Width must be either 1280 or 1920")
        #------------------------------------------------------

        self.FPS = 60
        self.game_round = 0

        self.screen = pygame.display.set_mode((self.Width, self.Height), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()

        pygame.display.set_caption("Solus Miles")
        self.clock = pygame.time.Clock()
    #------------------------------------------------------
    def Create_Map(self):
        room = "Pygame_GroupProject\Assets\Room\Room.png"
        Room(room, self.Width, self.Height, background)
        global player
        player = GameManager.create_player(rifle)
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
        global hud
        hud = HUD()
        GameManager.manage_rounds()
    #------------------------------------------------------
    def Run(self):
        self.screen.fill("Black")

        player.Update()
        GameManager.update_aliens()
        Bullet.Update()
        GameManager.manage_rounds()
        hud.Update()

        background.draw(self.display_surface)
        entities.draw(self.display_surface)
        aliens.draw(self.display_surface)
        bullets.draw(self.display_surface)
        hud_components.draw(self.display_surface)
        
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
        self.image = pygame.transform.scale(self.image, tilesize)
        self.rect = self.image.get_rect(topleft = pos)
# This class will not be dealing with the background (room) anymore
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Room(pygame.sprite.Sprite):
    def __init__(self, image, width, height, group):
        super().__init__(group)
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
class HUD():
    def __init__(self):
        self.health = "Pygame_GroupProject/Assets/HUD/FullBar.png"
        self.health = Sprite((0,0), self.health, [hud_components], (game.Tilesize * 2, game.Tilesize))

        self.powerUp_width = game.Width - game.Tilesize
        self.weapon_width = game.Width - (game.Tilesize * 2)
        self.size = (game.Tilesize / 2) + (game.Tilesize / 4)

        self.weapon = "Pygame_GroupProject/Assets/HUD/Pistol.png"
        self.weapon = Sprite((self.weapon_width, 10), self.weapon, [hud_components], (self.size, self.size))

        self.powerUp = "Pygame_GroupProject/Assets/HUD/Base.png"
        self.powerUp = Sprite((self.powerUp_width, 10), self.powerUp, [hud_components], (self.size, self.size))
    #------------------------------------------------------
    def draw_heart(self):
        self.health.kill()

        if player.health > 75:
            self.health = "Pygame_GroupProject/Assets/HUD/FullBar.png"
        elif player.health > 50 and player.health <= 75:
            self.health = "Pygame_GroupProject/Assets/HUD/QuarterBar.png"
        elif player.health > 25 and player.health <= 50:
            self.health = "Pygame_GroupProject/Assets/HUD/HalfBar.png"
        elif player.health > 0 and player.health <= 25:
            self.health = "Pygame_GroupProject/Assets/HUD/3QuarterBar.png"

        if player.health > 0:
            self.health = Sprite((0,0), self.health, [hud_components], (game.Tilesize * 2, game.Tilesize))
    #------------------------------------------------------
    def draw_weapon(self):
        self.weapon.kill()

        if player.weapon == pistol:
            self.weapon = "Pygame_GroupProject/Assets/HUD/Pistol.png"
        elif player.weapon == smg:
            self.weapon = "Pygame_GroupProject/Assets/HUD/SMG.png"
        elif player.weapon == shotgun:
            self.weapon = "Pygame_GroupProject/Assets/HUD/Shotgun.png"
        elif player.weapon == rifle:
            self.weapon = "Pygame_GroupProject/Assets/HUD/Rifle.png"
        print(self.size)
        self.weapon = Sprite((self.weapon_width, 10), self.weapon, [hud_components], (self.size, self.size))
    #------------------------------------------------------
    def draw_powerUp(self):
        self.powerUp.kill()

        if player.powerUp == None:
            self.powerUp = "Pygame_GroupProject/Assets/HUD/Base.png"
        elif player.powerUp == "adrenaline":
            self.powerUp = "Pygame_GroupProject/Assets/HUD/Adrenaline.png"
        elif player.powerUp == "double_damage":
            self.powerUp = "Pygame_GroupProject/Assets/HUD/DoubleDamage.png"
        elif player.powerUp == "pest_control":
            self.powerUp = "Pygame_GroupProject/Assets/HUD/PestControl.png"
        print(self.size)
        self.powerUp = Sprite((self.powerUp_width, 10), self.powerUp, [hud_components], (self.size, self.size))
    #------------------------------------------------------
    def Update(self):
        self.draw_heart()
        self.draw_weapon()
        self.draw_powerUp()
        gc.collect()
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Character():
    def __init__(self, health, speed, damage, pos_x, pos_y, image, group):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.org_image = image
        self.group = group
        self.size = (game.Tilesize, game.Tilesize)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Player(Character):
    #------------------------------------------------------
    def __init__(self, health, speed, damage, pos_x, pos_y, weapon, image, group):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
        self.weapon = weapon
        self.powerUp = None
        self.last_move = "down"
        self.char = Sprite((pos_x, pos_y), image, group, self.size)
        self.rect = self.char.rect
        self.cooldown = 500
    #------------------------------------------------------
    def take_damage(self, amount):
        self.health -= amount
    #------------------------------------------------------
    def heal(self, amount):
        if self.health < 100:
            self.health += amount
        if self.health > 100:
            self.health = 100
    #------------------------------------------------------
    def Movement(self):
        keys = pygame.key.get_pressed()
        max_move = game.Tilesize * 2
        #------------------------------------------------------
        if keys[pygame.K_a] and self.pos_x > self.size[0]:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_x -= self.speed    
            self.last_move = "left"
        #------------------------------------------------------
        elif keys[pygame.K_d] and self.pos_x < (game.Width - max_move):
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_x += self.speed
            self.last_move = "right"
        #------------------------------------------------------
        elif keys[pygame.K_w] and self.pos_y > self.size[0]:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_y -= self.speed
            self.last_move = "up"
        #------------------------------------------------------
        elif keys[pygame.K_s] and self.pos_y < (game.Height - max_move):
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, self.size)
            self.pos_y += self.speed
            self.last_move = "down"
    #------------------------------------------------------
        gc.collect()

    def Shoot(self):
        keys = pygame.key.get_pressed()
        mouse_clicks = pygame.mouse.get_pressed()         
        #------------------------------------------------------
        if self.cooldown >= 100:
            if (keys[pygame.K_SPACE] or mouse_clicks[0]): # [0] = Left Click
                if player.last_move == "up":
                    bullet = Bullet((self.pos_x + (game.Tilesize / 2)), (self.pos_y - (game.Tilesize / 2)))
                elif player.last_move == "down":
                    bullet = Bullet((self.pos_x + (game.Tilesize / 2)), (self.pos_y + (game.Tilesize / 2)))
                elif player.last_move == "left":
                    bullet = Bullet((self.pos_x - (game.Tilesize / 2)), (self.pos_y + (game.Tilesize / 2)))
                elif player.last_move == "right":
                    bullet = Bullet((self.pos_x + (game.Tilesize / 2)), (self.pos_y + (game.Tilesize / 2)))
                self.cooldown = 0
                Bulls.append(bullet)
                del(bullet)
                gc.collect()
        #------------------------------------------------------
        else:
            self.cooldown += self.weapon.fire_rate
    #------------------------------------------------------
    def Update(self):
        self.Movement()
        self.Shoot()
        if self.health < 1:
            pygame.quit()
            sys.exit()
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Weapon():
    def __init__(self, damage, fire_rate, shot_range):
        self.damage = damage
        self.fire_rate = fire_rate
        self.shot_range = shot_range
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Bullet():   
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.size = game.Tilesize * 0.2
        self.image = "Pygame_GroupProject\Assets\Bullet\Bullet.png"
        self.org_image = self.image
        self.size = (game.Tilesize / 8, game.Tilesize / 8)
        self.char = Sprite((self.x, self.y), self.image, [bullets], self.size)
        self.rect = self.char.rect
        self.group = bullets
        self.direction = player.last_move
        self.hit = False
    #------------------------------------------------------
    def Move(self):
        #try:                                             
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
    #------------------------------------------------------
    @staticmethod
    def Update():
        i = 0
        if len(Bulls) > 0:
            while i < len(Bulls):
                Bulls[i].char.kill()
                Bulls[i].char = ImageTransformer(Bulls[i].org_image, 0)
                Bulls[i].char = Bulls[i].char.ReturnImage((Bulls[i].x, Bulls[i].y), Bulls[i].group, Bulls[i].size)
                #------------------------------------------------------
                if Bulls[i].x > game.Tilesize * 29 or Bulls[i].x < game.Tilesize:
                    Bulls[i].char.kill()
                    del(Bulls[i])
                    gc.collect()
                #------------------------------------------------------
                elif Bulls[i].y > game.Tilesize * 16 or Bulls[i].y < game.Tilesize:
                    Bulls[i].char.kill()
                    del(Bulls[i])
                    gc.collect()
                else:
                    Bulls[i].Move()
                i += 1
#--------------------------------------------------------------------------------------------------------
class PowerUp:
    def __init__(self, showing, pos_x, pos_y, image, spawn_rate):
        self.size = game.Tilesize
        self.image = image
        self.group = power_ups
        self.spawn_rate = spawn_rate
        if self.showing == True:
            self.char = Sprite((pos_x, pos_y), image, power_ups, self.size)
            self.rect = self.char.rect
        power_ups_lst.append(self)
        if len(power_ups_lst) == 1:
            self.spawn_rate = list(len(spawn_rate + 1))
        else:
            starting_point = power_ups_lst.index(self) - 1
            starting_point = power_ups_lst[starting_point].spawn_rate[-1] + 1
            end_point = self.spawn_rate + starting_point



    def colide(self):
        hit = pygame.sprite.spritecollide(self.char, entities, False)

        if hit:
            player.powerUp = self
            self.char.kill()
            i = power_ups_lst.index(self)
            del(power_ups_lst[i])
            del(i)
            gc.collect()

    @staticmethod
    def random_spawn():
        power_up_choice = random.randint(1, 4)
        location_choice_width = random.randint(Game.Width + Game.Tilesize, Game.Width - Game.Tilesize)
        if power_up_choice == 1:
            double_damage = GameManager.create_shield(True)
        elif power_up_choice == 2:
            alien = GameManager.create_turret(True)
        else:
            alien = GameManager.create_mosquito(True)
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Aliens(Character):
    def __init__(self, name, health, speed, damage, pos_x, pos_y, target, spawn_rate, image, group, showing):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
        self.target = target
        self.spawn_rate = spawn_rate
        self.name = name
        self.showing = showing
        self.cooldown = 100
        self.cooldown_2 = 100
        self.last_move = None
        self.no_right = None
        self.no_left = None
        self.no_up = None
        self.no_down = None
        print(game.Tilesize)
        if showing == True:
            self.char = Sprite((pos_x, pos_y), image, group, self.size)
            self.rect = self.char.rect

    def __str__(self):
        return self.name

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

    def Collide(self):
        hit1 = pygame.sprite.spritecollide(self.char, bullets, False)

        if hit1 and self.cooldown >= 100:
            self.health -= player.weapon.damage
            self.cooldown = 0
            print(self.health)
            Bulls[0].char.kill()
            del(Bulls[0])
            gc.collect()
        else:
            self.cooldown += player.weapon.fire_rate

#Alien collision with the player (needs to be adjusted once ranged aliens are incorporated)

        hit_2 = pygame.sprite.spritecollide(self.char, entities, False)

        if hit_2:
            if self.last_move == "right":
                self.pos_x -= self.speed
            elif self.last_move == "left":
                self.pos_x += self.speed
            elif self.last_move == "up":
                self.pos_y += self.speed
            elif self.last_move == "down":
                self.pos_y -= self.speed
            if self.cooldown_2 >= 100:
                player.health -= self.damage
                print(self.damage)
                self.cooldown_2 = 0
            else:
                self.cooldown_2 += 2

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
        door_duplicates = 0
        for a in GameManager.aliens_alive:
            if door_choice == a.door:
                door_duplicates += 1
        #------------------------------------------------------
        if door_choice == 1: # Left 1
            self.pos_x = 0 * game.Tilesize # 0 x tilesize
            self.pos_y = 5 * game.Tilesize # 5 x tilesize
            self.door = 1
            self.last_move = "right"
            while(door_duplicates > 0):
                self.pos_x -= game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 2: # Left 2
            self.pos_x = 0 * game.Tilesize  # 0 x tilesize
            self.pos_y = 11 * game.Tilesize # 11 x tilesize
            self.door = 2
            self.last_move = "right"
            while(door_duplicates > 0):
                self.pos_x -= game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 3: # Bottom 1
            self.pos_x = 8 * game.Tilesize  # 8 x tilesize
            self.pos_y = 16 * game.Tilesize # 16 x tilesize
            self.door = 3
            self.last_move = "up"
            while(door_duplicates > 0):
                self.pos_y += game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 4: # Bottom 2 
            self.pos_x = 21 * game.Tilesize # 21 x tilesize
            self.pos_y = 16 * game.Tilesize # 16 x tilesize
            self.door = 4
            self.last_move = "up"
            while(door_duplicates > 0):
                self.pos_y += game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 5: # Right 1 
            self.pos_x = 29 * game.Tilesize # 29 x tilesize
            self.pos_y = 5 * game.Tilesize  # 5 x tilesize
            self.door = 5
            self.last_move = "left"
            while(door_duplicates > 0):
                self.pos_x += game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 6: # Right 2
            self.pos_x = 29 * game.Tilesize # 29 x tilesize
            self.pos_y = 11 * game.Tilesize # 11 x tilesize
            self.door = 6
            self.last_move = "left"
            while(door_duplicates > 0):
                self.pos_x += game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 7: # Top 1
            self.pos_x = 21 * game.Tilesize # 21 x tilesize
            self.pos_y = 0 * game.Tilesize  # 0 x tilesize
            self.door = 7
            self.last_move = "down"
            while(door_duplicates > 0):
                self.pos_y -= game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------
        elif door_choice == 8: # Top 2
            self.pos_x = 8 * game.Tilesize # 8 x tilesize
            self.pos_y = 0 * game.Tilesize # 0 x tilesize
            self.door = 8
            self.last_move = "down"
            while(door_duplicates > 0):
                self.pos_y -= game.Tilesize
                door_duplicates -= 1
        #------------------------------------------------------

#Physical attacker movement
    def move(self):
        #------------------------------------------------------
        self.no_right = None
        self.no_left = None
        self.no_up = None
        self.no_down = None
        gap = game.Tilesize / 2
        gap = int(gap)
        for a in GameManager.aliens_alive:
            if a.name != self.name:
                if self.pos_x + self.speed / 2 > a.pos_x - gap and self.pos_x + self.speed / 2 < a.pos_x:
                    self.no_right = True
                if self.pos_x - self.speed / 2 > a.pos_x and self.pos_x - self.speed / 2 < a.pos_x + gap:
                    self.no_left = True
                if self.pos_y - self.speed > a.pos_y and self.pos_y - self.speed < a.pos_y + gap:
                    self.no_up = True
                if self.pos_y + self.speed / 2 > a.pos_y - gap and self.pos_y + self.speed / 2 < a.pos_y:
                    self.no_down = True
        if self.pos_x < game.Tilesize and self.no_right != True:
            self.pos_x += self.speed
            self.last_move = "right"
        elif self.pos_x > game.Width - game.Tilesize and self.no_left != True:
            self.pos_x -= self.speed
            self.last_move = "left"
        elif self.pos_x != player.pos_x:
             if self.pos_x < player.pos_x - self.speed / 2 and self.no_right != True:
                self.pos_x += self.speed / 2
                self.last_move = "right"
        #------------------------------------------------------
             elif self.pos_x > player.pos_x + self.speed / 2 and self.no_left != True:
                self.pos_x -= self.speed / 2
                self.last_move = "left"
        #------------------------------------------------------
        if self.pos_y < game.Tilesize and self.no_down != True:
            self.pos_y += self.speed
            self.last_move = "down"
        elif self.pos_y > game.Height - game.Tilesize and self.no_up != True:
            self.pos_y -= self.speed
            self.last_move = "up"
        elif self.pos_y != player.pos_y:
             if self.pos_y > player.pos_y + self.speed / 2 and self.no_up != True:
                self.pos_y -= self.speed / 2
                self.last_move = "up"
        #------------------------------------------------------
             elif self.pos_y < player.pos_y - self.speed / 2 and self.no_down != True:
                self.pos_y += self.speed / 2
                self.last_move = "down"

    def update_last_move(self):
        if self.last_move == "up":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)          
        elif self.last_move == "down":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
        elif self.last_move == "left":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
        elif self.last_move == "right":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)

        self.char = self.char.ReturnImage((self.pos_x, self.pos_y), [aliens], (game.Tilesize, game.Tilesize))
#Ranged attacker movement
    def ranged_move(self):
        if self.door < 3 or self.door in range(5, 7): #Left and Right
            if self.pos_y != player.pos_y:
               if self.pos_x < game.Tilesize:
                   self.pos_x += self.speed
                   self.last_move = "right"
               elif self.pos_x > game.Width - game.Tilesize:
                   self.pos_x -= self.speed
                   self.last_move = "left"
               elif self.pos_y < player.pos_y - self.speed:
                   self.pos_y += self.speed
                   self.last_move = "down"
               elif self.pos_y > player.pos_y + self.speed:
                   self.pos_y -= self.speed
                   self.last_move = "up"
        elif self.door in range(3, 5) or self.door in range(7, 9): #Bottom and Top
            if self.pos_x != player.pos_x:
                if self.pos_y < game.Tilesize:
                    self.pos_y += self.speed
                    self.last_move = "down"
                elif self.pos_y > game.Height - game.Tilesize:
                    self.pos_y -= self.speed
                    self.last_move = "up"
                elif self.pos_x < player.pos_x - self.speed:
                    self.pos_x += self.speed
                    self.last_move = "right"
                elif self.pos_x > player.pos_x - self.speed:
                    self.pos_x -= self.speed
                    self.last_move = "left"
        if self.last_move == "up":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
        elif self.last_move == "down":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
        elif self.last_move == "left":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
        elif self.last_move == "right":
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)

        self.char = self.char.ReturnImage((self.pos_x, self.pos_y), [aliens], (game.Tilesize, game.Tilesize))
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
        GameManager.manage_rounds(game_round)
        return game_round

    @staticmethod
    def find_aliens(alien):
        i = 0
        duplicate_aliens = 0
        while(i < len(GameManager.aliens_alive)):
            if alien.name in GameManager.aliens_alive[i].name:
                duplicate_aliens += 1
            i += 1
        return duplicate_aliens

    @staticmethod
    def remove_alien(alien_name):
        i = 0
        while(i < len(GameManager.aliens_alive)):
            if GameManager.aliens_alive[i].name == alien_name:
                GameManager.aliens_alive[i].char.kill()
                del(GameManager.aliens_alive[i])
                gc.collect()
            i+= 1

    @staticmethod
    def manage_spawns():
        spawn_rate_total = len(shield.spawn_rate) + len(turret.spawn_rate) + len(armoured_wing.spawn_rate) + len(bomber.spawn_rate) + len(mosquito.spawn_rate) + len(sniper.spawn_rate)
        if spawn_rate_total == 100:
            aliens_needed = game.game_round * 3
            i = 1
            aliens_needed+= i
            while(aliens_needed > i):
                alien = Aliens.random_spawn()
                if i > 1:
                    duplicate_aliens = GameManager.find_aliens(alien)
                    if duplicate_aliens > 0:
                        alien.name += str(duplicate_aliens + 1)
                GameManager.aliens_alive.append(alien)
                del(alien)
                print(str(GameManager.aliens_alive[i - 1]))
                i+= 1
            gc.collect()
        else:
            raise numErrors("The spawn rates must add up to 100")

    @staticmethod
    def manage_rounds():
        if len(GameManager.aliens_alive) == 0:
            game.game_round += 1
            print("\n"+str(game.game_round)+"\n")
            GameManager.manage_spawns()

    @staticmethod
    def update_aliens():
        i = 0
        while(i < len(GameManager.aliens_alive)):
            GameManager.aliens_alive[i].update_last_move()
            #if GameManager.aliens_alive[i].can_move == True:
            if "Turret" in GameManager.aliens_alive[i].name or "Armoured-wing" in GameManager.aliens_alive[i].name:
                GameManager.aliens_alive[i].ranged_move()
            elif "Sniper" in GameManager.aliens_alive[i].name:
                GameManager.aliens_alive[i].ranged_move()
            elif "Shield" in GameManager.aliens_alive[i].name or "Mosquito" in GameManager.aliens_alive[i].name:
                GameManager.aliens_alive[i].move()
            elif "Bomber" in GameManager.aliens_alive[i].name:
                GameManager.aliens_alive[i].move()
            #GameManager.aliens_alive[i].move()
            GameManager.aliens_alive[i].Collide()
            if GameManager.aliens_alive[i].health < 1:
                GameManager.remove_alien(GameManager.aliens_alive[i].name)
            i += 1


#parameters - (health, speed, damage, pos_x, pos_y, target, spawn_rate, image, groups, game width, game height)
    @staticmethod
    def create_shield(showing):
        shield = Aliens("Shield", 200, 2, 20, 100, 100, player, 25, "Pygame_GroupProject\Assets\Aliens\\Normal\Shield_Armour.png", [aliens], showing)
        GameManager.Difficulty(shield)
        shield.convert_spawn_rate(True, None)
        return shield

    @staticmethod
    def create_turret(showing):
        turret = Aliens("Turret", 200, 2, 15, 200, 200, player, 10, "Pygame_GroupProject\Assets\Aliens\\Normal\Turret.png", [aliens], showing)
        GameManager.Difficulty(turret)
        turret.convert_spawn_rate(False, shield.spawn_rate)
        return turret
    
    @staticmethod
    def create_armoured_wing(showing):
        armoured_wing = Aliens("Armoured-wing", 150, 3, 20, 300, 300, player, 15, "Pygame_GroupProject\Assets\Aliens\\Normal\Armoured_Wing.png", [aliens], showing)
        GameManager.Difficulty(armoured_wing)
        armoured_wing.convert_spawn_rate(False, turret.spawn_rate)
        return armoured_wing
    
    @staticmethod
    def create_bomber(showing):
        bomber = Aliens("Bomber", 30, 4, 100, 400, 400, player, 10, "Pygame_GroupProject\Assets\Aliens\\Normal\Bomber.png", [aliens], showing)
        GameManager.Difficulty(bomber)
        bomber.convert_spawn_rate(False, armoured_wing.spawn_rate)
        return bomber
    
    @staticmethod
    def create_mosquito(showing):
        mosquito = Aliens("Mosquito", 50, 4, 30, 500, 500, player, 25, "Pygame_GroupProject\Assets\Aliens\\Normal\Mosquito.png", [aliens], showing)
        GameManager.Difficulty(mosquito)
        mosquito.convert_spawn_rate(False, bomber.spawn_rate)
        return mosquito
    
    @staticmethod
    def create_sniper(showing):
        sniper = Aliens("Sniper", 50, 2, 75, 600, 600, player, 15, "Pygame_GroupProject\Assets\Aliens\\Normal\Sniper.png", [aliens], showing)
        GameManager.Difficulty(sniper)
        sniper.convert_spawn_rate(False, mosquito.spawn_rate)
        return sniper

    @staticmethod
    def Difficulty(alien):
        if game.difficulty == "Easy":
            alien.health *= 0.75
            alien.speed *= 0.75
            alien.damage *= 0.75
        elif game.difficulty == "Hard":
            alien.health *= 1.25
            alien.speed *= 1.25
            alien.damage *= 1.25

#parameters - (health, speed, damage, pos_x, pos_y, power_up, weapon, image, groups)
    @staticmethod
    def create_player(weapon: object):
        if weapon == pistol:
            image = "Pygame_GroupProject\Assets\Player\Player_Pistol.png"
        #------------------------------------------------------
        elif weapon == shotgun:
            image = "Pygame_GroupProject\Assets\Player\Player_Shotgun.png"
        #------------------------------------------------------
        elif weapon == smg:
            image = "Pygame_GroupProject\Assets\Player\Player_SMG.png"
        #------------------------------------------------------
        elif weapon == rifle:
            image = "Pygame_GroupProject\Assets\Player\Player_Rifle.png"
        #------------------------------------------------------
        else:
            raise entryErrors("You must enter a weapon object")
        #------------------------------------------------------
        player = Player(100, 3, 20, int(round(game.Width / 2)), int(round(game.Width / 2)),  weapon, image, [entities])

        return player
#----------------------------------------------------------------------------------------------------
pistol = Weapon(20, 3, 30)
shotgun = Weapon(150, 1.5, 10)
smg = Weapon(20, 10, 20)
rifle = Weapon(40, 5, 50)

menu = Menu(720)
menu.StartUp()

game = Game(720, "Normal")
game.Create_Map()

#Press "r" to start the game. Note: this is where the menu will be
while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()

    if menu.running == True:
        menu.Run()
    elif game.running == True:
        game.Run()