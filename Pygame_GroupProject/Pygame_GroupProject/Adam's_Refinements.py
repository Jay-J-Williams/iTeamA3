import pygame, sys
visible_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

#global Pistol
#global SMG   
#global Rifle   
#global Shotgun
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Settings:
    Width = 672
    Height = 672
    FPS = 60
    Tilesize = 32

    MAP = [
    ['c','w','w','w','w','l','d','l','w','w','w','w','w','l','d','l','w','w','w','w','c'], #1 | [0]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #2 | [1]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #3 | [2]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #4 | [3]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #5 | [4]
    ['l','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','l'], #6 | [5]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #7 | [6]
    ['l','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','l'], #8 | [7]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #9 | [8]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #10 | [9]
    ['w','f','f','f','f','f','f','f','f','f','fp','f','f','f','f','f','f','f','f','f','w'],#11 | [10]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #12 | [11]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #13 | [12]
    ['l','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','l'], #14 | [13]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #15 | [14]
    ['l','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','l'], #16 | [15]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #17 | [16]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #18 | [17]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #19 | [18]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #20 | [19]
    ['c','w','w','w','w','l','d','l','w','w','w','w','w','l','d','l','w','w','w','w','c']  #21 | [20]
    ]
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

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("black")
        self.map.run()
        pygame.display.update()
        self.clock.tick(self.FPS)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Map():
    def __init__(self):
        S = Settings()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.MAP = S.MAP
        self.TILESIZE = S.Tilesize
        self.create_map()

        self.animation = Animations()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                Door_indexes = [6, 14]

                col = col.lower()
                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Pygame_GroupProject\Assets\Area\Wall.png"
                    AreaSprite((x, y), image) 

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Wall.png", 90)
                    image = image.ReturnImage((x, y)) 

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Wall.png", 180)
                    image = image.ReturnImage((x, y)) 

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Wall.png", 270)
                    image = image.ReturnImage((x, y)) 
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Pygame_GroupProject\Assets\Area\Corner.png"
                    AreaSprite((x, y), image) 

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Corner.png", 90)
                    image = image.ReturnImage((x, y))       

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Corner.png", 180)
                    image = image.ReturnImage((x, y))  

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Corner.png", 270)
                    image = image.ReturnImage((x, y)) 
                #--------------------------------------------------------------------------------
                #Floor
                elif col == "f":
                    image = "Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image)   
                #--------------------------------------------------------------------------------
                #Player
                elif col == "fp":
                    image = "Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image)

                    image = "Pygame_GroupProject\Assets\Player\Player_pistol.png"
                    global player 
                    player = Player(100, 5, 20, x, y, image)

    def run(self):
        visible_sprites.draw(self.display_surface)
        player.Update()
        self.animation.Update()

        visible_sprites.update()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__(visible_sprites)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Animations():
    def __init__(self):
        S = Settings()
        self.map = S.MAP
        self.TILESIZE = S.Tilesize

        self.LEDOne = "Pygame_GroupProject\Assets\Area\LED.png"
        self.LEDTwo = "Pygame_GroupProject\Assets\Area\LED_frame2.png"
        self.LEDThree = "Pygame_GroupProject\Assets\Area\LED_frame3.png"
        self.LEDFour = "Pygame_GroupProject\Assets\Area\LED_frame4.png"

        self.LED_frames = [self.LEDOne, self.LEDTwo, self.LEDThree, self.LEDFour]
        self.LED_current = 0

        self.DoorOne = "Pygame_GroupProject\Assets\Area\Door.png"
        self.DoorTwo = "Pygame_GroupProject\Assets\Area\Door_frame2.png"
        self.DoorThree = "Pygame_GroupProject\Assets\Area\Door_frame3.png"
        self.DoorFour = "Pygame_GroupProject\Assets\Area\Door_frame4.png"

        self.Door_frames = [self.DoorOne, self.DoorTwo, self.DoorThree, self.DoorFour]
        self.Door_current = 0
        self.DoorOpening = False

    def LED_animations(self):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                self.LED_indexes = [5, 7, 13, 15]

                if col == "l" and row_index == 0:
                    image = self.LED_frames[int(self.LED_current)]
                    AreaSprite((x, y), image) 

                elif col == "l" and row_index in self.LED_indexes and col_index == 0:
                    image = ImageTransformer(self.LED_frames[int(self.LED_current)], 90)
                    image = image.ReturnImage((x, y)) 

                elif col == "l" and row_index == 20:
                    image = ImageTransformer(self.LED_frames[int(self.LED_current)], 180)
                    image = image.ReturnImage((x, y)) 

                elif col == "l" and row_index in self.LED_indexes and col_index == 20:
                    image = ImageTransformer(self.LED_frames[int(self.LED_current)], 270)
                    image = image.ReturnImage((x, y)) 

                self.LED_current += 0.2

                if self.LED_current >= len(self.LED_frames):
                    self.LED_current = 0

    def Door_animations(self):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                Door_indexes = [6, 14]

                if col == "d" and row_index == 0:
                    image = self.Door_frames[int(self.Door_current)]
                    AreaSprite((x, y), image) 

                elif col == "d" and row_index in Door_indexes and col_index == 0:
                    image = ImageTransformer(self.Door_frames[int(self.Door_current)], 90)
                    image = image.ReturnImage((x, y)) 

                elif col == "d" and row_index == 20:
                    image = ImageTransformer(self.Door_frames[int(self.Door_current)], 180)
                    image = image.ReturnImage((x, y)) 

                elif col == "d" and row_index in Door_indexes and col_index == 20:
                    image = ImageTransformer(self.Door_frames[int(self.Door_current)], 270)
                    image = image.ReturnImage((x, y)) 

                self.Door_current += 0.2

                if self.Door_current >= len(self.Door_frames):
                    self.Door_current = 0
                    self.DoorOpening = False

    def DoorStill(self):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                Door_indexes = [6, 14]

                if col == "d" and row_index == 0:
                    image = self.DoorOne
                    AreaSprite((x, y), image) 

                elif col == "d" and row_index in Door_indexes and col_index == 0:
                    image = ImageTransformer(self.DoorOne, 90)
                    image = image.ReturnImage((x, y)) 

                elif col == "d" and row_index == 20:
                    image = ImageTransformer(self.DoorOne, 180)
                    image = image.ReturnImage((x, y)) 

                elif col == "d" and row_index in Door_indexes and col_index == 20:
                    image = ImageTransformer(self.DoorOne, 270)
                    image = image.ReturnImage((x, y)) 

    def DoorPress(self): #Note - later turn into round based opening
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.DoorOpening = True

    def Update(self):
        self.LED_animations()      
        self.DoorPress()

        if self.DoorOpening:
            self.Door_animations()
        else:
            self.DoorStill()

#This is a really big class that I am hoping to refine and simplify later on, for now I am too tired to 
# realy care. So far LEDs work, however, door animation is proving to be a challenge. This should be left
# until we implement the round-based mode, since the animation will play at the beginning of the round.
# I will be testing the door animation with the "space bar" during testing tho.

# - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)

    def ReturnImage(self, pos):
        return AreaSprite(pos, self.image)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Character():
    health = None
    speed = None
    damage = None

    x = None
    y = None

    image = None
    groups = None

    def __init__(self, health, speed, damage, x, y, image):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.x = x
        self.y = y
        self.org_image = image

        self.char = AreaSprite((self.x, self.y), image)
        self.rect = self.char.rect

#This has become a class to hold all character related sprites, player and aliens - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Player(Character):
    weapon = None
    powerUp = None

    def __init__(self, health, speed, damage, x, y, image):
        super().__init__(health, speed, damage, x, y, image)
        self.weapon = None
        self.powerUp = None

    def Movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x > 32:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage((self.x, self.y)) 
            self.x -= self.speed           

        elif keys[pygame.K_d] and self.x < 608:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage((self.x, self.y)) 
            self.x += self.speed

        elif keys[pygame.K_w] and self.y > 32:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage((self.x, self.y)) 
            self.y -= self.speed

        elif keys[pygame.K_s] and self.y < 608:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage((self.x, self.y)) 
            self.y += self.speed

    def Collision(self):
        #enHit = pygame.sprite.spritecollide(self, obstacle_sprites, False)
        #Use for enemies
        pass

    def WeaponChanger(self):
        image = "Pygame_GroupProject\Assets\Player\Player_pistol.png"

        if self.weapon == Pistol:
            image = "Pygame_GroupProject\Assets\Player\Player_pistol.png"
        elif self.weapon == SMG:
            image = "Pygame_GroupProject\Assets\Player\Player_smg.png"
        elif self.weapon == Rifle:
            image = "Pygame_GroupProject\Assets\Player\Player_rifle.png"
        elif self.weapon == Shotgun:
            image = "Pygame_GroupProject\Assets\Player\Player_shotgun.png"

        self.org_image = image

        self.char.kill()
        self.char = AreaSprite((self.x, self.y), self.org_image) 

    def Update(self):
        self.Movement()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Weapon():
    damage = None #Damage done
    fireRate = None #Between 1 and 10, being shot/second
    shotRange = None #The tile range that a gun fires in
    isShot = False #Used for about 2 miliseconds, to show that a gun has been fired

    def __init__(self, damage, fireRate, shotRange):
        self.damage = damage
        self.fireRate = fireRate
        self.shotRange = shotRange

#Pistol = Weapon(15, 2, 5)
#SMG = Weapon(10, 1, 3)
#Rifle = Weapon(60, 5, 15)
#Shotgun = Weapon(50, 5, 2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Bullets():
    speed = None
    x = None
    y = None

    image = None
    group = None

    def __init__(self, speed, x, y):
        self.speed = speed
        self.x = x
        self.y = y

        self.image = "None"
        self.group = bullets
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

game = Game()
while True:
    game.run()