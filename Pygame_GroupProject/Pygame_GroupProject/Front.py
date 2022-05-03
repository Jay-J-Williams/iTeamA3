import pygame, sys

#Maybe start with level setup | use the style the zelda video taught you, you can add file assets later

class Settings:
    Width = 1280
    Height = 720
    FPS = 60
    Tilesize = 64
    #Marc, we will have doors, floors, and walls. they cannot all be x. Maybe use different lettering for each item

    MAP = [
    ['w','w','w','w','w','w','w','w','w','w','d','w','w','w','w','w','w','w','w','w','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','w'],
    ['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w']
    ]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.Height,self.Width)
        pygame.display.set_caption('Alien Attack | Space Shrooms - Deluxe')
        self.clock = pygame.time.Clock()

        self.level=Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill=('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(self.FPS)
if __name__ == '__main__':
    game = Game()
    game.run()


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.visible_obstacle = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(self.MAP):
            for col_index, col in enumerate(row):
                x = col_index * self.TILESIZE
                y = row_index * self.TILESIZE
                if col == 'w':
                    Tile((x,y),[self.visible_sprites, self.visible_obstacle])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

                if col == 'f':
                    Floor((x,y),[self.visible_sprites])
                if col == 'd':
                    Door((x,y),[self.visible_sprites, self.visible_obstacle])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos) 

        self.direction = pygame.math.vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_A]:
            self.direction.y = -1
        elif keys{pygame.K_D}:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_A]:
            self.direction.x = 1
        elif keys{pygame.K_S:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self,direction):
        if direction == 'horizontal':
            if sprite.rect.colliderect(self,rect):
                if sprite.rect.colliderect(self,rect):
                    if self.direction.x > 0:    
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction =='vertical':
            if sprite.rect.colliderect(self,rect):
                if sprite.rect.colliderect(self,rect):
                    if self.direction.y > 0:  
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom


        if direction == 'vertical':
            pass
    def update(self):
        self.input()
        self.move(self.speed)

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos) 

class Door(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos) 

#for doors use "d" | for floors use 'f" | for walls use "w".....Done player will = 'p'