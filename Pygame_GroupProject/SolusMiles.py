import pygame, sys, random

background = pygame.sprite.Group() #Room | For visible spawning
entities = pygame.sprite.Group() #Player/Aliens | For visible spawning
aliens = pygame.sprite.Group() #Aliens | For collisions
bullets = pygame.sprite.Group() #Bullets | For visible spawning
hud_components = pygame.sprite.Group()
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
        self.difficulty = "Normal"
        self.Height = 1080
        #Either 1280 or 1920
        #------------------------------------------------------
        if self.Height == 720:
            self.Height = 1280
            self.Tilesize = 42.7
        #------------------------------------------------------
        elif self.Height == 1080:
            self.Width = 1920
            self.Tilesize = 64
        #------------------------------------------------------
        else:
            raise numErrors("Width must be either 1280 or 1920")
        #------------------------------------------------------

        self.FPS = 60
        self.run = False
        pygame.mouse.set_visible(False)
        self.game_round = 0

        self.screen = pygame.display.set_mode((self.Width, self.Height), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()

        pygame.display.set_caption("Solus Miles")
        self.clock = pygame.time.Clock()
    #------------------------------------------------------
    def Create_Map(self):
        room = "Pygame_GroupProject\Assets\Room\Room.png"
        Room(room, self.Width, self.Height)
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
        #GameManager.__aliens_alive.append(test_alien)
    #------------------------------------------------------
    def Run(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
            elif (keys[pygame.K_o]):
                if len(GameManager.aliens_alive) > 0:
                    GameManager.aliens_alive[0].char.kill()
                    del(GameManager.aliens_alive[0])

        self.screen.fill("Black")

        player.Update()
        GameManager.update_aliens()
        Bullet.Update()
        GameManager.manage_rounds()

        background.draw(self.display_surface)
        entities.draw(self.display_surface)
        aliens.draw(self.display_surface)
        bullets.draw(self.display_surface)
        hud.draw_healthbar()
        hud.draw_heart()

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

class HUD:
    def __init__(self):
        self.healthbar_length = player.health * 2
        self.fullHeart = "Pygame_GroupProject/Assets/Heart/Heart_Full.png"
        self.halfHeart = "Pygame_GroupProject/Assets/Heart/Heart_Half.png"
        self.QuarterOne_Heart = "Pygame_GroupProject/Assets/Heart/Heart_1Quarter.png"
        self.QuarterThree_Heart = "Pygame_GroupProject/Assets/Heart/Heart_3Quarter.png"
    #------------------------------------------------------
    def draw_healthbar(self):
        if player.health < 1001:
            pygame.draw.rect(game.display_surface, (255, 0, 0), pygame.Rect(10, 10, player.health * 2, 25))
            pygame.draw.rect(game.display_surface, (255,255,255), pygame.Rect(10, 10, self.healthbar_length, 25),4)
    def draw_heart(self):
        if player.health > 75:
            Sprite((0,0), self.fullHeart, [hud_components], game.Tilesize)
        elif player.health > 50 and player.health <= 75:
            Sprite((0,0), self.QuarterOne_Heart, [hud_components], game.Tilesize)
        elif player.health > 25 and player.health <= 50:
            Sprite((0,0), self.halfHeart, [hud_components], 48)
        elif player.health > 0 and player.health <= 25:
            Sprite((0,0), self.QuarterThree_Heart, [hud_components], game.Tilesize)
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
        self.size = game.Tilesize
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
        max_move = self.size * 2
        #------------------------------------------------------
        if keys[pygame.K_a] and self.pos_x > self.size:
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
        elif keys[pygame.K_w] and self.pos_y > self.size:
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
        self.char = Sprite((self.x, self.y), self.image, [bullets], (game.Tilesize / 8))
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
                #------------------------------------------------------
                elif Bulls[i].y > game.Tilesize * 16 or Bulls[i].y < game.Tilesize:
                    Bulls[i].char.kill()
                    del(Bulls[i])
                else:
                    Bulls[i].Move()
                i += 1
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Aliens(Character):
    def __init__(self, name, health, speed, damage, pos_x, pos_y, target, spawn_rate, image, group, showing):
        super().__init__(health, speed, damage, pos_x, pos_y, image, group)
        self.target = target
        self.spawn_rate = spawn_rate
        self.name = name
        self.showing = showing
        self.can_move = None
        self.cooldown = 100
        self.cooldown_2 = 100
        self.last_move = None
        self.old_pos_x = None
        self.old_pos_y = None
        print(game.Tilesize)
        if showing == True:
            self.char = Sprite((pos_x, pos_y), image, group, self.size)
            self.rect = self.char.rect

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

        #Next step in code - see below -
        #aliens.remove(self)
        #self.char = Sprite((self.pos_x, self.pos_y), self.org_image, temp_group, self.size)
        #hit_3 = pygame.sprite.spritecollide(self.char, aliens, False)
        #if hit_3:
        #    if last_alien % 2 == 0:
        #        if self.last_move == "right":
        #            self.pos_x -= self.speed * 10
        #        elif self.last_move == "left":
        #            self.pos_x += self.speed
        #        elif self.last_move == "up":
        #            self.pos_y += self.speed * 10
        #        elif self.last_move == "down":
        #            self.pos_y -= self.speed * 10
        #    elif last_alien % 2 == 1:
        #        if self.last_move == "right":
        #            self.pos_x += self.speed * 10
        #        elif self.last_move == "left":
        #            self.pos_x -= self.speed * 10
        #        elif self.last_move == "up":
        #            self.pos_y -= self.speed * 10
        #        elif self.last_move == "down":
        #            self.pos_y += self.speed * 10
        #self.char.kill()
        #self.char = Sprite((self.pos_x, self.pos_y), self.org_image, self.group, self.size)

        #for a in GameManager.aliens_alive:
        #    if a.name != self.name:
        #        print(a.name, self.name)
        ##        if a.pos_x < self.pos_x + self.speed:
        ##            a.pos_y = a.speed
        ##        elif a.pos_x > self.pos_x - self.speed:
        ##            a.pos_y -= a.speed

        #        #if last_alien % 2 == 0:
        #        #if game.Width == 1280:
        #        #    temp_tilesize = round(game.Tilesize)
        #        #    if self.pos_x in range(a.pos_x - temp_tilesize, a.pos_x):
        #        #        self.pos_x -= self.speed * 10
        #        #    elif self.pos_x in range(a.pos_x + temp_tilesize, a.pos_x):
        #        #        self.pos_x += self.speed * 10
        #        #    elif self.pos_y in range(a.pos_y - temp_tilesize, a.pos_y):
        #        #        self.pos_y -= self.speed * 10
        #        #    elif self.pos_y in range(a.pos_y + temp_tilesize, a.pos_y):
        #        #        self.pos_y += self.speed * 10
        #        #else:
        ###        a.pos_x = int(a.pos_x)
        #        a.pos_y = int(a.pos_y)
        #        self.pos_x = int(self.pos_x)
        #        self.pos_y = int(self.pos_y)
        #        gap = game.Tilesize
        #        if self.pos_x in range(a.pos_x - gap, a.pos_x + gap) and self.pos_y in range(a.pos_y - gap, a.pos_y + gap):
        #            print("Executed")
        #            if self.pos_x in range(a.pos_x - gap, a.pos_x):
        #                self.pos_x = (a.pos_x - gap)
        #                self.pos_y = (a.pos_y - gap)
        #            elif self.pos_x in range(a.pos_x, a.pos_x + gap):
        #                self.pos_x = (a.pos_x + gap)
        #                self.pos_y = (a.pos_y + gap)
        #            elif self.pos_y in range(a.pos_y - gap, a.pos_y):
        #                self.pos_y = (a.pos_y - gap)
        #                self.pos_x = (a.pos_x - gap)
        #            elif self.pos_y in range(a.pos_y, a.pos_y + gap):
        #                self.pos_y = (a.pos_y + gap)
        #                self.pos_x = (a.pos_x + gap)
                #elif last_alien % 2 == 1:
                #if self.pos_x > a.pos_x - game.Tilesize and self.pos_y <= a.pos_x:
                #    self.pos_x -= self.speed * 10
                #elif self.pos_x < a.pos_x - game.Tilesize and self.pos_y >= a.pos_x:
                #    self.pos_x += self.speed * 10
                #elif self.pos_y > a.pos_y - game.Tilesize and self.pos_y <= a.pos_y:
                #    self.pos_y -= self.speed * 10                            
                #elif self.pos_y < a.pos_y + game.Tilesize and self.pos_y >= a.pos_y:
                #    self.pos_y += self.speed * 10

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
            self.door = 1
            self.last_move = "right"
        #------------------------------------------------------
        elif door_choice == 2: # Left 2
            self.pos_x = 0 * game.Tilesize  # 0 x tilesize
            self.pos_y = 11 * game.Tilesize # 11 x tilesize
            self.door = 2
            self.last_move = "right"
        #------------------------------------------------------
        elif door_choice == 3: # Bottom 1
            self.pos_x = 8 * game.Tilesize  # 8 x tilesize
            self.pos_y = 16 * game.Tilesize # 16 x tilesize
            self.door = 3
            self.last_move = "up"
        #------------------------------------------------------
        elif door_choice == 4: # Bottom 2 
            self.pos_x = 21 * game.Tilesize # 21 x tilesize
            self.pos_y = 16 * game.Tilesize # 16 x tilesize
            self.door = 4
            self.last_move = "up"
        #------------------------------------------------------
        elif door_choice == 5: # Right 1 
            self.pos_x = 29 * game.Tilesize # 29 x tilesize
            self.pos_y = 5 * game.Tilesize  # 5 x tilesize
            self.door = 5
            self.last_move = "left"
        #------------------------------------------------------
        elif door_choice == 6: # Right 2
            self.pos_x = 29 * game.Tilesize # 29 x tilesize
            self.pos_y = 11 * game.Tilesize # 11 x tilesize
            self.door = 6
            self.last_move = "left"
        #------------------------------------------------------
        elif door_choice == 7: # Top 1
            self.pos_x = 21 * game.Tilesize # 21 x tilesize
            self.pos_y = 0 * game.Tilesize  # 0 x tilesize
            self.door = 7
            self.last_move = "down"
        #------------------------------------------------------
        elif door_choice == 8: # Top 2
            self.pos_x = 8 * game.Tilesize # 8 x tilesize
            self.pos_y = 0 * game.Tilesize # 0 x tilesize
            self.door = 8
            self.last_move = "down"
        #------------------------------------------------------

#Physical attacker movement
    def move(self):
        #------------------------------------------------------
        no_right = None
        no_left = None
        no_up = None
        no_down = None
        gap = game.Tilesize / 2
        gap = int(gap)
        self.pos_x = int(self.pos_x)
        self.pos_y = int(self.pos_y)
        self.speed = int(self.speed)
        for a in GameManager.aliens_alive:
            if a.name != self.name:
                a.pos_x = int(a.pos_x)
                a.pos_y = int(a.pos_y)
                a.speed = int(a.speed)
            if self.pos_x + self.speed / 2 in range(a.pos_x - gap, a.pos_x):
                no_right = True
            if self.pos_x - self.speed / 2 in range(a.pos_x, a.pos_x + gap):
                no_left = True
            if self.pos_y - self.speed / 2 in range(a.pos_y, a.pos_y + gap):
                no_up = True
            if self.pos_y + self.speed / 2 in range(a.pos_y - gap, a.pos_y):
                no_down = True
        if self.pos_x != player.pos_x:
             if self.pos_x < player.pos_x - self.speed / 2 and no_right != True:
                self.pos_x += self.speed / 2
                self.last_move = "right"
                print(self.last_move)
        #------------------------------------------------------
             elif self.pos_x > player.pos_x + self.speed / 2 and no_left != True:
                self.pos_x -= self.speed / 2
                self.last_move = "left"
                print(self.last_move)
        #------------------------------------------------------
        if self.pos_y != player.pos_y:
             if self.pos_y > player.pos_y + self.speed / 2 and no_up != True:
                self.pos_y -= self.speed / 2
                self.last_move = "up"
                print(self.last_move)
        #------------------------------------------------------
             elif self.pos_y < player.pos_y - self.speed / 2 and no_down != True:
                self.pos_y += self.speed / 2
                self.last_move = "down"
                print(self.last_move)

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

        self.char = self.char.ReturnImage((self.pos_x, self.pos_y), [aliens], game.Tilesize)
#Ranged attacker movement
    def ranged_move(self):
        if self.door < 3 or self.door in range(5, 7): #Left and Right
            if self.pos_y != player.pos_y:
               if self.pos_y < player.pos_y - self.speed:
                   self.pos_y += self.speed
                   self.last_move = "down"
               elif self.pos_y > player.pos_y + self.speed:
                   self.pos_y -= self.speed
                   self.last_move = "up"
        elif self.door in range(3, 5) or self.door in range(7, 9): #Bottom and Top
            if self.pos_x != player.pos_x:
                if self.pos_x < player.pos_x - self.speed:
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

        self.char = self.char.ReturnImage((self.pos_x, self.pos_y), [aliens], game.Tilesize)

# Door exiting
    def exit_door(self):
         i = 0
         if self.can_move != True:
             old_pos_x = self.pos_x
             old_pos_y = self.pos_y
             while(i < len(GameManager.aliens_alive)):
                 if GameManager.aliens_alive[i].name != self.name:
                     if self.door == 1: # Left 1
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_x != old_pos_x + game.Tilesize:
                                    self.pos_x += self.speed
                                 elif self.pos_y != old_pos_y - game.Tilesize:
                                    self.pos_y -= self.speed
                                 elif self.pos_x != GameManager.aliens_alive[i].pos_x and self.pos_y != GameManager.aliens_alive[i].pos_y:
                                    self.can_move = True
                     elif self.door == 2: # Left 2
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_x != old_pos_x + game.Tilesize:
                                    self.pos_x += self.speed
                                 elif self.pos_y != old_pos_y + game.Tilesize:
                                    self.pos_y += self.speed
                                 elif self.pos_x != GameManager.aliens_alive[i].pos_x and self.pos_y != GameManager.aliens_alive[i].pos_y:
                                    self.can_move = True
                     elif self.door == 3: # Bottom 1
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_y != old_pos_y - game.Tilesize:
                                    self.pos_y -= self.speed
                                 elif self.pos_x != old_pos_x - game.Tilesize:
                                    self.pos_x -= self.speed
                                 elif self.pos_x != GameManager.aliens_alive[i].pos_x and self.pos_y != GameManager.aliens_alive[i].pos_y:
                                    self.can_move = True
                     elif self.door == 4: # Bottom 2
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_y != old_pos_y - game.Tilesize:
                                    self.pos_y -= self.speed
                                 elif self.pos_x != old_pos_x + game.Tilesize:
                                    self.pos_x += self.speed
                                 elif self.pos_x != GameManager.aliens_alive[i].pos_x and self.pos_y != GameManager.aliens_alive[i].pos_y:
                                    self.can_move = True
                     elif self.door == 5: # Right 1
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_x != old_pos_x - game.Tilesize:
                                    self.pos_x -= self.speed
                                 elif self.pos_y != old_pos_y + game.Tilesize:
                                    self.pos_y += self.speed
                                 elif self.pos_x == old_pos_x - game.Tilesize and self.pos_y == old_pos_y + game.Tilesize:
                                    self.can_move = True
                     elif self.door == 6: # Right 2
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_x != old_pos_x - game.Tilesize:
                                    self.pos_x -= self.speed
                                 elif self.pos_y != old_pos_y - game.Tilesize:
                                    self.pos_y -= self.speed
                                 elif self.pos_x == old_pos_x - game.Tilesize and self.pos_y == old_pos_y - game.Tilesize:
                                    self.can_move = True
                     elif self.door == 7: # Top 1
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_y != old_pos_y + game.Tilesize:
                                    self.pos_y += self.speed
                                 elif self.pos_x != old_pos_x + game.Tilesize:
                                    self.pos_x += self.speed
                                 elif self.pos_x != GameManager.aliens_alive[i].pos_x and self.pos_y != GameManager.aliens_alive[i].pos_y:
                                    self.can_move = True
                     elif self.door == 8: # Top 2
                             if GameManager.aliens_alive[i].door == self.door:
                                 if self.pos_y != old_pos_y + game.Tilesize:
                                    self.pos_y += self.speed
                                 elif self.pos_x != old_pos_x - game.Tilesize:
                                    self.pos_x -= self.speed
                                 elif self.pos_x != GameManager.aliens_alive[i].pos_x and self.pos_y != GameManager.aliens_alive[i].pos_y:
                                    self.can_move = True
                     print(self.door, self.can_move)
                     i+= 1
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
                print(GameManager.aliens_alive[i - 1].pos_x, GameManager.aliens_alive[i - 1].pos_y)
                del(alien)
                print(GameManager.aliens_alive[i - 1].__str__)
                i+= 1
            #GameManager.remove_alien("Shield2")
            print("\n")
        else:
            raise numErrors("The spawn rates must add up to 100")

    @staticmethod
    def manage_rounds():
        if len(GameManager.aliens_alive) == 0:
            game.game_round += 1
            GameManager.manage_spawns()

    @staticmethod
    def update_aliens():
        i = 0
        while(i < len(GameManager.aliens_alive)):
            GameManager.aliens_alive[i].update_last_move()
            #GameManager.aliens_alive[i].char.kill()
            #GameManager.aliens_alive[i].char = ImageTransformer(GameManager.aliens_alive[i].org_image, 0)
            #GameManager.aliens_alive[i].char = GameManager.aliens_alive[i].char.ReturnImage((GameManager.aliens_alive[i].pos_x, GameManager.aliens_alive[i].pos_y), GameManager.aliens_alive[i].group, GameManager.aliens_alive[i].size)
            #GameManager.aliens_alive[i].exit_door()
            #if GameManager.aliens_alive[i].can_move == True:
            #if "Turret" in GameManager.aliens_alive[i].name or "Armoured-wing" in GameManager.aliens_alive[i].name:
            #    GameManager.aliens_alive[i].ranged_move()
            #elif "Sniper" in GameManager.aliens_alive[i].name:
            #    GameManager.aliens_alive[i].ranged_move()
            #elif "Shield" in GameManager.aliens_alive[i].name or "Mosquito" in GameManager.aliens_alive[i].name:
            #    GameManager.aliens_alive[i].move()
            #elif "Bomber" in GameManager.aliens_alive[i].name:
            #    GameManager.aliens_alive[i].move()
            GameManager.aliens_alive[i].move()
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
        player = Player(100, 3, 20, (game.Width / 2), (game.Height / 2), weapon, image, [entities])

        return player
#----------------------------------------------------------------------------------------------------
pistol = Weapon(40, 3, 30)
shotgun = Weapon(150, 1.5, 10)
smg = Weapon(20, 10, 20)
rifle = Weapon(40, 5, 50)

game = Game()
game.Create_Map()
running = False

#Press "r" to start the game. Note: this is where the menu will be
while(running == False):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                running = True

while(running):
    game.Run()