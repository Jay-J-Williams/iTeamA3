import pygame, sys

background = pygame.sprite.Group() #Room
entities = pygame.sprite.Group() #Player/Aliens
bullets = pygame.sprite.Group() #Bullets
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
        room = "Pygame_GroupProject\Pygame_GroupProject\Assets\Room\Room.png"
        Room(room, self.Width, self.Height)

        image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player.png"
        global player
        player = Player(100, 5, 20, (self.Width / 2), (self.Height / 2), image, [entities], self.Tilesize)
    #------------------------------------------------------
    def Run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("Black")
        player.Update(self.Width, self.Height)

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
    def Shoot(self):
        keys = pygame.key.get_pressed()
        mouse_clicks = pygame.mouse.get_pressed()

        if keys[pygame.K_SPACE] or mouse_clicks[0]:
            Bullet(self.x, self.y)
    #------------------------------------------------------
    def Update(self, width, height):
        self.Movement(width, height)
        self.Shoot()
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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 20
        self.image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Bullet\Bullet.png"
        bullets.add(self)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
game = Game()

while 1:
    game.Run()