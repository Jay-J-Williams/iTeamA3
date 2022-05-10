import pygame, sys
#----------------------------------------------------------------------------------------------------
#FRONT-END
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
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #11 | [10]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #12 | [11]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #13 | [12]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #14 | [13]
    ['d','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','d'], #15 | [14]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #16 | [15]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #17 | [16]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #18 | [17]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'], #19 | [18]
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','fp','w'],#20 | [19]
    ['c','w','w','w','w','w','d','w','w','w','w','w','w','w','d','w','w','w','w','w','c']  #21 | [20]
    ]
#----------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------
class Map():
    def __init__(self):
        S = Settings()
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.offset = pygame.math.Vector2()
        self.MAP = S.MAP
        self.TILESIZE = S.Tilesize
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE
                self.y = y
                self.x = x
                col = col.lower()
                #--------------------------------------------------------------------------------
                #Walls
                if col == "w" and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png"
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "w" and col_index == 0 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "w" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites]) 

                elif col == "w" and col_index == 20 and row_index > 0 and row_index < 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Wall.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])
                #--------------------------------------------------------------------------------
                #Corners
                elif col == "c" and col_index == 20 and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png"
                    AreaSprite((x, y), image, [self.visible_sprites])

                elif col == "c" and col_index == 0 and row_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites])         

                elif col == "c" and col_index == 0 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites])

                elif col == "c" and col_index == 20 and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Corner.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites])
                #--------------------------------------------------------------------------------
                #Doors
                elif col == "d" and row_index == 0:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png"
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "d" and (row_index == 6 or row_index == 14) and col_index == 0:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png", 90)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "d" and row_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png", 180)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])

                elif col == "d" and (row_index == 6 or row_index == 14) and col_index == 20:
                    image = ImageTransformer("Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Door.png", 270)
                    image = image.ReturnImage()
                    AreaSprite((x, y), image, [self.visible_sprites, self.obstacle_sprites])
                #--------------------------------------------------------------------------------
                #Floor
                elif "f" in col:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Area\Floor.png"
                    AreaSprite((x, y), image, [self.visible_sprites])      
                #--------------------------------------------------------------------------------
                #Player
                if "p" in col:
                    image = "Pygame_GroupProject\Pygame_GroupProject\Assets\Player\Player_pistol.png"
                    self.player = Player((x, y), image, self.visible_sprites, self.obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
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

class ImageTransformer(pygame.sprite.Sprite):
    def __init__(self, image, degrees):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.rotate(self.image, degrees)

    def ReturnImage(self):
        return self.image
#----------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, obstacles):
        super().__init__(groups)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacles = obstacles
        self.direction = pygame.math.Vector2(pos)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction.x -= 1
        elif keys[pygame.K_d]:
            self.direction.x += 1

        if keys[pygame.K_w]:
            self.direction.y -= 1
        elif keys[pygame.K_s]:
            self.direction.y += 1

    def update(self):
        Player.movement(self)
        self.rect = self.image.get_rect(topleft = self.direction)
#----------------------------------------------------------------------------------------------------
running = True
game = Game()
while running:
    game.run()
#----------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------#
#BACK-END