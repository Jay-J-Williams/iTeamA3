import pygame, sys
visible_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

#IMPORTANT NOTE - The assets folder cannot be directly accessed through Assets/blahblah/blahblah
#This is because the file path starts at the .sln file, this file is ONE folder above the game files
#This means that to add an asset, you have to follow the following file structure ->
#Pygame_GroupProject/Assets/blahblah/blahblah

#This took me too long to figure out and drove me crazy

#Less importantly, obviously, I figured out how to reduce the code to make it way easier to both 
#use and understand, and have added comments explaining them.

#Note - I created the sprite groups here instead, so they can be used in any class they need to be used in

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

                self.Door_indexes = [6, 14]

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
                #Doors
                elif col == "d" and row_index == 0:
                    image = "Pygame_GroupProject\Assets\Area\Door.png"
                    AreaSprite((x, y), image, [visible_sprites])

                elif col == "d" and  row_index in self.Door_indexes and col_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Door.png", 90)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "d" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Door.png", 180)
                    image = image.ReturnImage((x, y), [visible_sprites])

                elif col == "d" and  row_index in self.Door_indexes and col_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Assets\Area\Door.png", 270)
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
                    self.player = Character(100, 5, 20, (x, y), image, [visible_sprites])

                #Looks like less code, does it not? This is due to the change I made in ImageTransformer()
                #See it below - Adam

    def run(self):
        visible_sprites.draw(self.display_surface)
        self.player.Update()
        self.animation.LED_animations()
        visible_sprites.update()
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

    def Move(self, pos):
        self.rect = self.image.get_rect(topleft = pos)

#AreaSprite is now used to handle every single sprite of the game, and the Move() function is made to
# handle all the sprites that move, like player and aliens

#The main change was mentioned above: the Move() funtion, however, I also refined some __init__ code in 
# order to deal with all the sprites. Literally all of them. You're welcome.

# - Adam
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

        self.LED_animations()

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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)

    def ReturnImage(self, pos, groups):
        return AreaSprite(pos, self.image, groups)

#There are a total of 6 lines of code here, including the class statment. All of them have their uses, and
# all have been made to deal with all types of sprites, may get updated when we start working with aliens

#The main change I have made is in ReturnImage(), this now returns an AreaSprite object in order to lessen
# the code that is used, by alot too. It was primarily edited to deal with player movements with as little 
# issue as possible, then moved from there to handle all sprites.

# - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Character():
    health = None
    speed = None
    damage = None
    pos = None
    image = None
    groups = None

    #Characters have a main 6 attributes they all deal with, the player will only use these 6 so no need
    # to create a player class. However an alien class should be made to deal with their adjustments
    # until we figure out how to do them all in this one class. Might not happen, so an Alien sub-class
    # should still to be made
    # - Adam

    def __init__(self, health, speed, damage, pos, image, groups):
        self.health = health
        self.speed = speed
        self.damage = damage

        self.pos = pygame.Vector2(pos)
        self.org_image = image
        self.groups = groups

        self.char = AreaSprite(self.pos, image, groups)
        self.rect = self.char.rect

        #Little explanation here, there is a self. made to handle everything it needs to from all 6 
        # attributes, I have added the extra self.char and self.rect for the player. They could be used on
        # aliens, but seeing as that sub-class has not been done yet, I dunno if they definiely will
        # - Adam

    def Movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.pos.x > 32:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 270)
            self.char = self.char.ReturnImage(self.pos, self.groups)
            self.pos.x -= self.speed           

        elif keys[pygame.K_d] and self.pos.x < 608:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 90)
            self.char = self.char.ReturnImage(self.pos, self.groups)
            self.pos.x += self.speed

        elif keys[pygame.K_w] and self.pos.y > 32:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 180)
            self.char = self.char.ReturnImage(self.pos, self.groups)
            self.pos.y -= self.speed

        elif keys[pygame.K_s] and self.pos.y < 608:
            self.char.kill()
            self.char = ImageTransformer(self.org_image, 0)
            self.char = self.char.ReturnImage(self.pos, self.groups)
            self.pos.y += self.speed

        
        self.char.Move(self.pos)

        #This was the big one, but was only completed then refined thanks to Marc's work on movement on the
        # 11th of May, the day I am writing this. When I first tried the code, the map was filled
        # with multiple player objects showing every place the player was. This is due to new objects
        # being created every milisecond. This has been fixed by killing off the old player object and 
        # replacing it with the newly created one every milisecond.

    def Collision(self):
        #Hit = pygame.sprite.spritecollide(self, obstacle_sprites, False) - Used to detect colision
        #Use for aliens, after they are created
        # - Adam
        pass

    def Update(self):
        self.Movement()
        self.Collision()
        #This will update the player every milisecond - Adam
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
game = Game()
while True:
    game.run()