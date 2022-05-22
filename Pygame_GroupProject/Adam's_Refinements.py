import pygame, random, sys
pygame.init()

background = pygame.sprite.Group()
user = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bulls = []

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
        self.round = 0
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.display = pygame.display.get_surface()
        pygame.display.set_caption("Solus Miles | Lone Soldier")
    #------------------------------------------------------
    def Initialize(self): 
        room = "Pygame_GroupProject\Assets\Room\Room.png"
        Room(room) 

        global player
        playerImage = "Pygame_GroupProject\Assets\Player\Player_Pistol.png"
        player = Player(100, 5, (game.width / 2), (game.height / 2), playerImage, user, game.size)
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
    def __init__(self, health, speed, x, y, image, group, size):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.image = image
        self.group = group
        self.size = size
        self.char = Sprite((x, y), image, group, size) 
        self.rect = self.char.rect
#--------------------------------------------------------------------------------------------------------
class Player(Character):
    def __init__(self, health, speed, x, y, image, group, size):
        super().__init__(health, speed, x, y, image, group, size)
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
            self.cooldown += self.weapon[0]
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
game = Game()
game.Initialize() 

while True:
    game.Run()