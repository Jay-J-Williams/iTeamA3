import pygame, sys, random, gc
pygame.init()
#------------------------------------------------------
hud = pygame.sprite.Group()
aliens = pygame.sprite.Group()
menu_display = pygame.sprite.Group()
room_display = pygame.sprite.Group()
user_sprites = pygame.sprite.Group()
#------------------------------------------------------
pistol = [20, 3, 30]
shotgun = [150, 1.5, 10]
smg = [20, 10, 20]
rifle = [40, 5, 50]
# Damage [0] | Fire Rate [1] | Shot Rate [2]
#------------------------------------------------------
P_bullets = []
A_bullets = []
enemies = []
#------------------------------------------------------
difficulty = "normal"
video_info = pygame.display.Info()
width, height = video_info.current_w, video_info.current_h

if height < 1080:
    tilesize = 48
elif height >= 1080 and height < 1440:
    tilesize = 64
elif height >= 1440 and height < 2160:
    tilesize = 96
elif height >= 2160:
    tilesize = 128

FPS = 60
#------------------------------------------------------
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
display = pygame.display.get_surface()
clock = pygame.time.Clock()
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Sprites(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, size):
        super().__init__(group)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)
    #------------------------------------------------------
    def ReturnImage(self, pos, groups, size):
        return Sprites(pos, self.image, groups, size)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Background(pygame.sprite.Sprite):
    def __init__(self, image, group):
        super().__init__(group)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (0,0))
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Menu():
    def __init__(self):
        self.running = True
        room = "Pygame_GroupProject/Assets/Room/Menu.png"
        Background(room, menu_display)
        #------------------------------------------------------
    def Update(self):
        keys = pygame.key.get_pressed()
        global difficulty
        
        if keys[pygame.K_RETURN]:
            self.running = False  
        elif keys[pygame.K_e]:           
            difficulty = "easy"
        elif keys[pygame.K_n]:
            difficulty = "normal"
        elif keys[pygame.K_h]:
            difficulty = "hard"
    #------------------------------------------------------
    def Run(self):
        self.Update()
        menu_display.draw(display)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Character():
    def __init__(self, health, speed, damage, pos_x, pos_y, image, group):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image
        self.group = group
        self.size = (tilesize, tilesize)

        self.char = Sprites((pos_x, pos_y), image, group, self.size)
        self.rect = self.char.rect
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Player(Character):
    def __init__(self, health, speed, damage, pos_x, pos_y):
        self.image = "Pygame_GroupProject/Assets/Player/Player_Pistol.png"
        super().__init__(health, speed, damage, pos_x, pos_y, self.image, user_sprites)
        self.weapon = pistol
        self.powerUp = None
        self.last_move = "down"
        self.cooldown = 500
        self.hit_cooldown = 100
    #------------------------------------------------------
    def Heal(self, amount):
        if self.health < 100:
            self.health += amount
        if self.health > 100:
            self.health = 100
    #------------------------------------------------------
    def Movement(self):
        keys = pygame.key.get_pressed()
        max_size = tilesize * 2

        if keys[pygame.K_a] and self.pos_x > tilesize:
            degrees = 270            
            self.pos_x -= self.speed
            self.last_move = "left"

        elif keys[pygame.K_d] and self.pos_x < (width - max_size):
            degrees = 90
            self.pos_x += self.speed
            self.last_move = "right"

        elif keys[pygame.K_w] and self.pos_y > tilesize:
            degrees = 180
            self.pos_y -= self.speed
            self.last_move = "up"

        elif keys[pygame.K_d] and self.pos_y < (height - max_size):
            degrees = 0
            self.pos_y += self.speed
            self.last_move = "down"

        self.char.kill()
        self.char = ImageTransformer(self.image, degrees)
        self.char = self.char.ReturnImage((self.pos_x, self.pos_y), self.group, tilesize)
    #------------------------------------------------------
    def Update(self):
        self.Movement()
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Bullet():
    def __init__(self, x, y, last_move, creator):
        self.x = x
        self.y = y
        self.direction = last_move
        self.creator = creator
        self.size = tilesize / 8
        self.image = "Pygame_GroupProject/Assets/Bullet/Bullet.png"
        self.char = Sprites((self.x, self.y), self.image, user_sprites, (self.size, self.size))
        self.rect = self.char.rect
    #------------------------------------------------------
    def Move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
    #------------------------------------------------------
    def Update(self):
        for b in P_bullets:
            if (b.x > tilesize or b.x < (width - tilesize)) or (b.y > tilesize or b.y < (width - tilesize)):
                b.char.kill()
                del(b)
            else:
                b.Move()

        for b in A_bullets:
            if (b.x > tilesize or b.x < (width - tilesize)) or (b.y > tilesize or b.y < (width - tilesize)):
                b.char.kill()
                del(b)
            else:
                b.Move()
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Alien(Character):
    def __init__(self, name):
        self.name = name 

        if self.name == "shield":
            self.health = 200
            self.speed = 2
            self.damage = 20
            self.image = "Pygame_GroupProject/Assets/Aliens/Normal/Shield_Armour.png"
        elif self.name == "turret":
            self.health = 200
            self.speed = 1.5
            self.damage = 15
            self.image = "Pygame_GroupProject/Assets/Aliens/Normal/Turret.png"
        elif self.name == "armoured_wing":
            self.health = 150
            self.speed = 3 
            self.damage = 20
            self.image = "Pygame_GroupProject/Assets/Aliens/Normal/Armoured_Wing.png"
        elif self.name == "mosquito":
            self.health = 50
            self.speed = 4 
            self.damage = 30 
            self.image = "Pygame_GroupProject/Assets/Aliens/Normal/Mosquito.png"
        elif self.name == "bomber":
            self.health = 30
            self.speed = 4 
            self.damage = 100 
            self.image = "Pygame_GroupProject/Assets/Aliens/Normal/Bomber.png"
        elif self.name == "sniper":
            self.health = 50
            self.speed = 1.5
            self.damage = 75 
            self.image = "Pygame_GroupProject/Assets/Aliens/Normal/Sniper.png"

        self.Difficulty()
    #------------------------------------------------------
    def Difficulty(self):
        if difficulty == "easy":
            self.health *= 0.75
            self.speed *= 0.75
            self.damage *= 0.75
        elif difficulty == "hard":
            self.health *= 1.25
            self.speed *= 1.25
            self.damage *= 1.25
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
menu = Menu()
run = True

while run:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()

    if menu.running == True:
        menu.Run()
    else:
        run = False

    gc.collect()
    pygame.display.update()
    clock.tick(FPS)