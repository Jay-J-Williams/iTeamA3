import pygame, sys

background = pygame.sprite.Group() #Room
entities = pygame.sprite.Group() #Player/Aliens
bullets = pygame.sprite.Group() #Bullets
#--------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        pygame.init()

        self.Width = 1920
        self.Height = 1088
        self.FPS = 60

        self.entities = [
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

        self.screen = pygame.display.set_mode((self.Width, self.Height))
        self.display_surface = pygame.display.get_surface()

        pygame.display.set_caption("Solus Miles")
        self.clock = pygame.time.Clock()

        self.Create_Map()
    #------------------------------------------------------
    def Create_Map(self):
        room = "Pygame_GroupProject\Pygame_GroupProject\Assets\Room\Room.png"
        AreaSprite((0,0), room, [background])

        for row_index, row in enumerate(self.entities):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64

                if col == "p":
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player.png"
                    global player
                    player = Player(100, 5, 20, x, y, image, [entities])

    #------------------------------------------------------
    def Run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("Blue")
        player.Update()

        background.draw(self.display_surface)
        entities.draw(self.display_surface)
        pygame.display.update()

        self.clock.tick(self.FPS)
#--------------------------------------------------------------------------------------------------------
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.rect = self.image.get_rect(topleft = pos)
#--------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)
    #------------------------------------------------------
    def ReturnImage(self, pos, groups):
        return AreaSprite(pos, self.image, groups)
#--------------------------------------------------------------------------------------------------------
class Character():
    health = None
    speed = None
    damage = None
    x = None
    y = None
    image = None
    groups = None
    #------------------------------------------------------
    def __init__(self, health, speed, damage, x, y, image, groups):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.x = x
        self.y = y
        self.org_image = image
        self.groups = groups
        self.char = AreaSprite((self.x, self.y), image, groups)
        self.rect = self.char.rect
#--------------------------------------------------------------------------------------------------------
class Player(Character):
    weapon = None
    powerUp = None
    #------------------------------------------------------
    def __init__(self, health, speed, damage, x, y, image, group):
        super().__init__(health, speed, damage, x, y, image, group)
        self.weapon = None
        self.powerUp = None
    #------------------------------------------------------
    def Movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x > 64:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.x -= self.speed           
        #------------------------------------------------------
        elif keys[pygame.K_d] and self.x < 1856:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.x += self.speed
        #------------------------------------------------------
        elif keys[pygame.K_w] and self.y > 64:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.y -= self.speed
        #------------------------------------------------------
        elif keys[pygame.K_s] and self.y < 1856:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.y += self.speed
    #------------------------------------------------------
    def Update(self):
        self.Movement()
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
#--------------------------------------------------------------------------------------------------------
game = Game()

while True:
    game.Run()