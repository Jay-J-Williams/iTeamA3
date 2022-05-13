import pygame, sys
visible_sprites = pygame.sprite.Group()
obstacle_sprites = pygame.sprite.Group()

global Pistol
global SMG   
global Rifle   
global Shotgun

#Changes have occured once more, in the form of door animations (work-in-progress | "space" to try) 
# and weapon / player classes, leaving Character() open for both player and alien use
#Note - Player and Weapon objects are now global objects, this means that you can use them wherever 
# in the code, though weapons have proved to only work after they've been called

# - Adam
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
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #11 | [10]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #12 | [11]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #13 | [12]
    ['l','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','l'], #14 | [13]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #15 | [14]
    ['l','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','l'], #16 | [15]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #17 | [16]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #18 | [17]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #19 | [18]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','fp','w'],#20 | [19]
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

                col = col.lower()
                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Pygame_GroupProject\Assets\Area\Wall.png"
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Wall.png", 90)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Wall.png", 180)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Wall.png", 270)
                    image = image.ReturnImage((x, y), [visible_sprites])
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Pygame_GroupProject\Assets\Area\Corner.png"
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Corner.png", 90)
                    image = image.ReturnImage((x, y), [visible_sprites])      

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Corner.png", 180)
                    image = image.ReturnImage((x, y), [visible_sprites]) 

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Corner.png", 270)
                    image = image.ReturnImage((x, y), [visible_sprites])
                #--------------------------------------------------------------------------------
                #Floor
                elif col == "f":
                    image = "Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image, [visible_sprites])      
                #--------------------------------------------------------------------------------
                #Player
                elif col == "fp":
                    image = "Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image, [visible_sprites])

                    image = "Pygame_GroupProject\Assets\Player\Player_pistol.png"
                    global player 
                    player = Player(100, 5, 20, x, y, image, [visible_sprites])

    def run(self):
        visible_sprites.draw(self.display_surface)
        player.Update()
        self.animation.Update()
        visible_sprites.update()

#Door was removed from this map list, in order to not repeat code from the door animation side, also
# Run() now uses self.animation.Update(), this is instead of using .LED_animations(). This is also
# due to door animations

#Player has become a global variable, thus solving the issue of using it across multiple classes. ...Whoo

# - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
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
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "l" and row_index in self.LED_indexes and col_index == 0:
                    image = ImageTransformer(self.LED_frames[int(self.LED_current)], 90)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "l" and row_index == 20:
                    image = ImageTransformer(self.LED_frames[int(self.LED_current)], 180)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "l" and row_index in self.LED_indexes and col_index == 20:
                    image = ImageTransformer(self.LED_frames[int(self.LED_current)], 270)
                    image = image.ReturnImage((x, y), [visible_sprites])

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
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "d" and row_index in Door_indexes and col_index == 0:
                    image = ImageTransformer(self.Door_frames[int(self.Door_current)], 90)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "d" and row_index == 20:
                    image = ImageTransformer(self.Door_frames[int(self.Door_current)], 180)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "d" and row_index in Door_indexes and col_index == 20:
                    image = ImageTransformer(self.Door_frames[int(self.Door_current)], 270)
                    image = image.ReturnImage((x, y), [visible_sprites])

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
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "d" and row_index in Door_indexes and col_index == 0:
                    image = ImageTransformer(self.DoorOne, 90)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "d" and row_index == 20:
                    image = ImageTransformer(self.DoorOne, 180)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "d" and row_index in Door_indexes and col_index == 20:
                    image = ImageTransformer(self.DoorOne, 270)
                    image = image.ReturnImage((x, y), [visible_sprites])

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

    def ReturnImage(self, pos, groups):
        return AreaSprite(pos, self.image, groups)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Character():
    health = None
    speed = None
    damage = None

    x = None
    y = None

    image = None
    groups = None

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

#This has become a class to hold all character related sprites, player and aliens - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Player(Character):
    weapon = None
    powerUp = None

    def __init__(self, health, speed, damage, x, y, image, group):
        super().__init__(health, speed, damage, x, y, image, group)
        self.weapon = None
        self.powerUp = None

    def Movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x > 32:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.x -= self.speed           

        elif keys[pygame.K_d] and self.x < 608:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.x += self.speed

        elif keys[pygame.K_w] and self.y > 32:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
            self.y -= self.speed

        elif keys[pygame.K_s] and self.y < 608:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage((self.x, self.y), self.groups)
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
        self.char = AreaSprite((self.x, self.y), self.org_image, [visible_sprites])

    def Update(self):
        self.Movement()
        self.Collision()

#The main addition is the weapon and powerUp variables, as well as the WeaponChanger() function, the
# variables do not need to be set during start-up, this is because you will always start the game with
# a pistol. The function is used to change to specific weapons, to be used when a weapon is collected

# - Adam
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

Pistol = Weapon(15, 2, 5)
SMG = Weapon(10, 1, 3)
Rifle = Weapon(60, 5, 15)
Shotgun = Weapon(50, 5, 2)

#This class is used for the basic weapon functions, like calculating damage, rate of fire, and range of 
# shot, all 3 variables have been used to create "sample" weaponry right below the class using the global
# variales created on lines 4 to 8. So far a work in progress, but as far as I know, this is all that
# is necessary. Likely that I am wrong, but once again, I am too tired to care

# - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
game = Game()
while True:
    game.run()