import pygame, random, sys
pygame.init()

background = pygame.sprite.Group()
user = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bulls = []
ens = []

pistol = [20, 3, 30]
shotgun = [150, 1, 10]
smg = [10, 10, 20]
rifle = [20, 5, 50]
# Damage [0] | Fire_Rate [1] | Shot_Range [2]
#--------------------------------------------------------------------------------------------------------
class Game():
    def __init__(self):
        self.width = 1280 #Either 1280 or 1920

        if self.width == 1280:
            self.height = 720
            self.size = 48
        #------------------------------------------------------
        elif self.width == 1920:
            self.height = 1080
            self.size = 64
        
        self.FPS = 60
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.display = pygame.display.get_surface()
        pygame.display.set_caption("Solus Miles | Lone Soldier")
    #------------------------------------------------------
    def Initialize(self): 
        room = "Pygame_GroupProject\Assets\Room\Room.png"
        Room(room) 
        #------------------------------------------------------
        global player
        player = Player(100, 5, (game.width / 2), (game.height / 2), user)
        #------------------------------------------------------
        global shield
        global turret
        global armoured_wing
        global mosquito
        global bomber 
        global sniper 
    #------------------------------------------------------
    def Run(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT or player.health < 1:
                pygame.quit()
                sys.exit()

        self.screen.fill("black")
        player.Update()
        Bullet.Update()

        background.draw(self.display)
        user.draw(self.display)
        bullets.draw(self.display)

        pygame.display.update()
        self.clock.tick(self.FPS)
#--------------------------------------------------------------------------------------------------------
class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, size):
        super().__init__(group)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
#--------------------------------------------------------------------------------------------------------
class Room(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__(background)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (game.width, game.height))
        self.rect = self.image.get_rect(topleft = (0,0))
#--------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)
    #------------------------------------------------------
    def ReturnImage(self, pos, group, size):
        return Sprite(pos, self.image, group, size)
#--------------------------------------------------------------------------------------------------------
class Character():
    def __init__(self, health, speed, x, y, image, group, size, showing):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.image = image
        self.group = group
        self.size = size
        if showing == True:
            self.char = Sprite((x, y), image, group, size) 
            self.rect = self.char.rect
#--------------------------------------------------------------------------------------------------------
class Player(Character):
    def __init__(self, health, speed, x, y, group):
        image = "Pygame_GroupProject/Assets/Player/Player_Pistol.png"
        super().__init__(health, speed, x, y, image, group, game.size, True)
        self.weapon = pistol
        self.powerUp = None
        self.last_move = "down"
        self.cooldown = 100
    #------------------------------------------------------
    def Move(self):
        keys = pygame.key.get_pressed()
        max_move = game.size * 2

        if keys[pygame.K_a] and self.x > game.size:
            self.char.kill()
            self.char = ImageTransformer(self.image, 270)
            self.char = self.char.ReturnImage((self.x, self.y), [user], self.size)
            self.x -= self.speed
            self.last_move = "left"
            #------------------------------------------------------
        elif keys[pygame.K_d] and self.x < game.width - max_move:
            self.char.kill()
            self.char = ImageTransformer(self.image, 90)
            self.char = self.char.ReturnImage((self.x, self.y), [user], self.size)
            self.x += self.speed
            self.last_move = "right"
            #------------------------------------------------------
        elif keys[pygame.K_w] and self.y > game.size:
            self.char.kill()
            self.char = ImageTransformer(self.image, 180)
            self.char = self.char.ReturnImage((self.x, self.y), [user], self.size)
            self.y -= self.speed
            self.last_move = "up"
            #------------------------------------------------------
        elif keys[pygame.K_s] and self.y < game.height - max_move:
            self.char.kill()
            self.char = ImageTransformer(self.image, 0)
            self.char = self.char.ReturnImage((self.x, self.y), [user], self.size)
            self.y += self.speed
            self.last_move = "down"
    #------------------------------------------------------
    def Shoot(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        #------------------------------------------------------
        if self.cooldown >= 100:
            if keys[pygame.K_SPACE] or mouse[0]:
                if self.last_move == "up":
                    B = Bullet((self.x + (game.size / 2)), (self.y - (game.size / 2)))
                elif self.last_move == "down":
                    B = Bullet((self.x + (game.size / 2)), (self.y + (game.size / 2)))
                elif self.last_move == "left":
                    B = Bullet((self.x - (game.size / 2)), (self.y + (game.size / 2)))
                elif self.last_move == "right":
                    B = Bullet((self.x + (game.size / 2)), (self.y + (game.size / 2)))
                self.cooldown = 0
                bulls.append(B)
        else:
            self.cooldown += self.weapon[1]
    #------------------------------------------------------
    def Update(self):
        self.Move()
        self.Shoot()
#--------------------------------------------------------------------------------------------------------
class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = player.last_move
        self.size = game.size / 8
        self.group = bullets
        self.image = "Pygame_GroupProject/Assets/Bullet/Bullet.png"
        self.char = Sprite((x, y), self.image, [bullets], self.size)
        self.rect = self.char.rect
    #------------------------------------------------------
    def Move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed 
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
    #------------------------------------------------------
    def Update():
        for b in bulls:
            b.char.kill()
            b.char = Sprite((b.x, b.y), b.image, b.group, b.size)
            b.rect = b.char.rect
            if b.x > (game.width - game.size) or b.x < game.size:          
                b.char.kill()
                del(b)
            elif b.y > (game.height - game.size) or b.y < game.size:
                b.char.kill()
                del(b)
            else:
                b.Move()
#--------------------------------------------------------------------------------------------------------
class Alien(Character):
    def __init__(self, name, health, speed, damage, x, y, spawn_rate, image, group, showing, range):
        super().__init__(health, speed, x, y, image, group, game.size, showing)
        self.name = name
        self.damage = damage 
        self.spawn_rate = spawn_rate
        self.showing = showing
        self.range = range #Either "long" or "short"
    #------------------------------------------------------
    def ShortRan_Move(self):
        if self.x != player.x:
            if self.x < player.x:
                self.x += self.speed * 0.5
                #------------------------------------------------------
            elif self.x > player.x:
                self.x -= self.speed * 0.5
            #------------------------------------------------------
        if self.y != player.y:
            if self.y < player.y:
                self.y += self.speed * 0.5
                #------------------------------------------------------
            elif self.y > player.y:
                self.y -= self.speed * 0.5
    #------------------------------------------------------
    def LongRan_Move(self):
        pass #Wait for Jay to finish up
    #------------------------------------------------------
    def Spawn(self, door):
        # Door choices from left to top, in relation to the top-left corner (0,0)
        if door == 1: # Left 1
            self.x = 0 * game.size
            self.y = 5 * game.size
            #------------------------------------------------------
        elif door == 2: # Left 2
            self.x = 0 * game.size
            self.y = 11 * game.size
            #------------------------------------------------------
        elif door == 3: #Bottom 1
            self.x = 8 * game.size
            self.y = 16 * game.size
            #------------------------------------------------------
        elif door == 4: # Bottom 2
            self.x = 21 * game.size
            self.y = 16 * game.size
            #------------------------------------------------------
        elif door == 5: # Right 1
            self.x = 29 * game.size
            self.y = 5 * game.size
            #------------------------------------------------------
        elif door == 6: # Right 2
            self.x = 29 * game.size
            self.y = 11 * game.size
            #------------------------------------------------------
        elif door = 7: # Top 1
            self.x = 21 * game.size
            self.y = 0 * game.size
            #------------------------------------------------------
        elif door == 8: # Top 2
            self.x = 8 * game.size
            self.y = 0 * game.size
    #------------------------------------------------------
    def Random_Spawn(self):
        alien = random.randint(1, 100)
        door = random.randint(1, 8)

        if alien > 0 and alien <= 25: #Shield | 25
            Rounds_Manager.Create_Shield()
        elif alien > 25 and alien <= 35: #Turret | 10
            Rounds_Manager.Create_Turret()
        elif alien > 35 and alien <= 50: #Armoured Wing | 15
            Rounds_Manager.Create_Armoured_Wing()
        elif alien > 50 and alien <= 75: #Mosquito | 25
            Rounds_Manager.Create_Mosquito()
        elif alien > 75 and alien <= 85: #Bomber | 10
            Rounds_Manager.Create_Bomber()
        elif alien > 85 and alien <= 100: #Sniper | 15
            Rounds_Manager.Create_Sniper()

        self.Spawn(door)
    #------------------------------------------------------
    def Update(self):
        self.Move()
#--------------------------------------------------------------------------------------------------------
class Rounds_Manager():
    def __init__(self):
        self.round = 0
    #------------------------------------------------------
    def Game_Start(self):
        self.round = 0
    #------------------------------------------------------
    def Create_Shield(self):       
        shieldImage = "Pygame_GroupProject/Assets/Aliens/Normal/Shield_Armour.png"
        shield = Alien("Shield", 200, 2, 20, 100, 100, 25, shieldImage, [enemies], True, "short")
    #------------------------------------------------------
    def Create_Turret(self):  
        turretImage = "Pygame_GroupProject/Assets/Aliens/Normal/Turret.png"
        turret = Alien("Turret", 200, 1, 15, 200, 200, 10, turretImage, [enemies], True, "long")
    #------------------------------------------------------
    def Create_Armoured_Wing(self):
        wingImage = "Pygame_GroupProject/Assets/Aliens/Normal/Armoured_Wing.png"
        armoured_wing = Alien("Armoured Wing", 150, 3, 30, 300, 300, 15, wingImage, [enemies], True, "long")
    #------------------------------------------------------
    def Create_Mosquito(self):
        mosquitoImage = "Pygame_GroupProject/Assets/Aliens/Normal/Mosquito.png"
        mosquito = Alien("Mosquito", 50, 4, 50, 400, 400, 25, mosquitoImage, True, [enemies], "short")
    #------------------------------------------------------
    def Create_Bomber(self):
        bomberImage = "Pygame_GroupProject/Assets/Aliens/Normal/Bomber.png"
        bomber = Alien("Bomber", 30, 4, 100, 500, 500, 10, bomberImage, True, [enemies], "short")
    #------------------------------------------------------
    def Create_Sniper(self):
        sniperImage = "Pygame_GroupProject/Assets/Aliens/Normal/Sniper.png"
        sniper = Alien("Sniper", 40, 1.5, 75, 600, 600, 15, sniperImage, True, [enemies], "long")
#--------------------------------------------------------------------------------------------------------
game = Game()
game.Initialize() 

while True:
    game.Run()