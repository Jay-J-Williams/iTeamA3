import pygame, sys
#----------------------------------------------------------------------------------------------------
class Settings:
    Width = 672
    Height = 672
    #Width and Height are equal to 32 * 21, I tried 64 but it turned out too big. If we use less tiles,
    #maybe I can make it 64 by 64 sized - Adam
    FPS = 60
    Tilesize = 32

    MAP = [
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c'], #1 | [0]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #2 | [1]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #3 | [2]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #4 | [3]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #5 | [4]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #6 | [5]
    ['d','f','f','f','f','f','fp','f','f','f','f','f','f','f','f','f','f','f','f','f','d'],#7 | [6]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #8 | [7]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #9 | [8]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #10 | [9]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #11 | [10]
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
#Settings has been updated with some extra comments regarding list placement, also messed with
#screen and tile size to make 'em work well - Adam
#----------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        S = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode((S.Width, S.Height))
        pygame.display.set_caption("Space Shrooms - Deluxe")

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
#Game has been re-written (some of it) to properly hold the variables in __init__(), without error - Adam
#----------------------------------------------------------------------------------------------------
class Map():
    def __init__(self):
        S = Settings()
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.MAP = S.MAP
        self.TILESIZE = S.Tilesize
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE

                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Assets/Area/Wall.png"
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Assets/Area/Wall.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Assets/Area/Wall.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites]) 

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Assets/Area/Wall.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Assets/Area/Corner.png"
                    AreaSprite((x, y), image, [self.visible_sprites])

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Assets/Area/Corner.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites])              

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Assets/Area/Corner.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites])

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Assets/Area/Corner.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites])
                #--------------------------------------------------------------------------------
                #Doors
                elif col == "d" and row_index == 0:
                    image = "Assets/Area/Door.png"
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "d" and (row_index == 6 or row_index == 14) and col_index == 0:
                    image = ImageTransformer("Assets/Area/Door.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "d" and row_index == 20:
                    image = ImageTransformer("Assets/Area/Door.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "d" and (row_index == 6 or row_index == 14) and col_index == 20:
                    image = ImageTransformer("Assets/Area/Door.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])
                #--------------------------------------------------------------------------------
                #Floor
                elif "f" in col:
                    image = "Assets/Area/Floor.png"
                    AreaSprite((x, y), image, [self.visible_sprites])      
                #--------------------------------------------------------------------------------
                #Player
                if "p" in col:
                    image = "Assets/Player/Player_pistol.png"
                    Player((x, y), image, [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
#This was a big one, 
#first - I added some varialbes to the initialiser (init) in order to make sure "create_map" worked
#second - I have re-written all tile typed classes to one single class handling them all
#third - I then made an ""ImageTransformer" class for rotating images; input: image file and rotation amount
#you cannot add a "return" statement into an init, so I created the "ReturnImage" function to return them
#fourth - I had re-written all if statements in "create_map" to fit these new changes
#Mostly, you had done a great job Marc however, it is still the first pygame anything you've made so don't
#let my changes discourage you. Learn from them and how they work and you will be able to do a lot better than
#great. 
# - Adam
#----------------------------------------------------------------------------------------------------
class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
#Made one class for all the area related sprites (e.g. Walls and Floors) - Adam

class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)

    def ReturnImage(self):
        return self.image
#Used for the rotating of images by the degrees inputted by us - Adam
#----------------------------------------------------------------------------------------------------
#NOTE - Have NOT worked on player yet, haven't even seen it - Adam
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacles = obstacles

#class Player(pygame.sprite.Sprite):
#    def __init__(self, pos, groups,obstacle_sprites):
#        super().__init__(groups)
#        self.image = pygame.image.load('').convert_alpha()
#        self.rect = self.image.get_rect(topleft = pos) 

#        self.direction = pygame.math.vector2()
#        self.speed = 5

#        self.obstacle_sprites = obstacle_sprites

#    def input(self):
#        keys = pygame.key.get_pressed()

#        if keys[pygame.K_A]:
#            self.direction.y = -1
#        elif keys[pygame.K_D]:
#            self.direction.y = 1
#        else:
#            self.direction.y = 0

#        if keys[pygame.K_A]:
#            self.direction.x = 1
#        elif keys[pygame.K_S]:
#            self.direction.x = -1
#        else:
#            self.direction.x = 0

#    def move(self,speed):
#        if self.direction.magnitude() != 0:
#            self.direction = self.direction.normalize()
#        self.rect.x += self.direction.x * speed
#        self.collision('horizontal')
#        self.rect.y += self.direction.y * speed
#        self.collision('vertical')

#    def collision(self,direction):
#        if direction == 'horizontal':
#            if sprite.rect.colliderect(self,rect):
#                if sprite.rect.colliderect(self,rect):
#                    if self.direction.x > 0:    
#                        self.rect.right = sprite.rect.left
#                    if self.direction.x < 0:
#                        self.rect.left = sprite.rect.right

#        if direction =='vertical':
#            if sprite.rect.colliderect(self,rect):
#                if sprite.rect.colliderect(self,rect):
#                    if self.direction.y > 0:  
#                        self.rect.bottom = sprite.rect.top
#                    if self.direction.y < 0:
#                        self.rect.top = sprite.rect.bottom


#        if direction == 'vertical':
#            pass
#    def update(self):
#        self.input()
#        self.move(self.speed)
#----------------------------------------------------------------------------------------------------
running = True
game = Game()

while running:
    game.run()
#Gave this section a little tune-up, so that it runs well - Adam
#----------------------------------------------------------------------------------------------------