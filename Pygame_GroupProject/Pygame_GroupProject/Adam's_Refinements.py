import pygame, sys

background = pygame.sprite.Group() #Walls/Corners/Floors
Entities = pygame.sprite.Group() #Player/Aliens
bullets = pygame.sprite.Group()

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
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c'], #1 | [0]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #2 | [1]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #3 | [2]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #4 | [3]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #5 | [4]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #6 | [5]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #7 | [6]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #8 | [7]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #9 | [8]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #10 | [9]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],#11 | [10]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #12 | [11]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #13 | [12]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #14 | [13]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #15 | [14]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #16 | [15]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #17 | [16]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #18 | [17]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #19 | [18]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #20 | [19]
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c']  #21 | [20]
    ]

    entities = [
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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        S = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode((S.Width, S.Height))
        pygame.display.set_caption("Solus Miles")

        self.clock = pygame.time.Clock()
        self.map = Map()
        self.map.create_map()
        self.FPS = S.FPS

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill("black")
        self.map.run()
        self.clock.tick(self.FPS)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Map():
    def __init__(self):
        S = Settings()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.MAP = S.MAP
        self.Ent = S.entities
        self.TILESIZE = S.Tilesize
        #self.animation = Animations()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                col = col.lower()
                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png"
                    AreaSprite((x, y), image, [background])

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 90)
                    image = image.ReturnImage((x, y), [background])

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 180)
                    image = image.ReturnImage((x, y), [background])

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 270)
                    image = image.ReturnImage((x, y), [background])
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png"
                    AreaSprite((x, y), image, [background])

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 90)
                    image = image.ReturnImage((x, y), [background])     

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 180)
                    image = image.ReturnImage((x, y), [background])

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 270)
                    image = image.ReturnImage((x, y), [background])
                #--------------------------------------------------------------------------------
                #Floor
                elif col == "f":
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image, [background])     
                #--------------------------------------------------------------------------------

        for row_index, row in enumerate(self.Ent):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                if col == "p":
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"
                    global player
                    player = Player(100, 2, 20, x, y, image, [Entities])

        background.draw(self.display_surface)
        Entities.draw(self.display_surface)
        pygame.display.update()

    def run(self):
        player.Update()
        #self.animation.Update()

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

        self.map = Map()
        self.display_surf = self.map.display_surface

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

        background.draw(self.display_surf)
        Entities.draw(self.display_surf)
        pygame.display.update()

    def Collision(self):
        #enHit = pygame.sprite.spritecollide(self, obstacle_sprites, False)
        #Use for enemies
        pass

    def WeaponChanger(self):
        image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"

        if self.weapon == Pistol:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"
        elif self.weapon == SMG:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_smg.png"
        elif self.weapon == Rifle:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_rifle.png"
        elif self.weapon == Shotgun:
            image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_shotgun.png"

        self.org_image = image

        self.char.kill()
        self.char = AreaSprite((self.x, self.y), self.org_image, Entities)

    def Update(self):
        self.Movement()
        self.Collision()
        self.WeaponChanger()

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

class Bullet(pygame.sprite.Sprite):   
    x = None
    y = None
    speed = None
    image = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 20
        #self.image = "Pygame_GroupProject\Pygame_GroupProject\"

Pistol = Weapon(15, 2, 10)
SMG = Weapon(10, 1, 5)
Rifle = Weapon(60, 5, 15)
Shotgun = Weapon(50, 5, 5)

#This class is used for the basic weapon functions, like calculating damage, rate of fire, and range of 
# shot, all 3 variables have been used to create "sample" weaponry right below the class using the global
# variales created on lines 4 to 8. So far a work in progress, but as far as I know, this is all that
# is necessary. Likely that I am wrong, but once again, I am too tired to care

# - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
game = Game()

while True:
    game.run()