import pygame, sys, random, gc
pygame.init()
#------------------------------------------------------
hud = pygame.sprite.Group()
aliens = pygame.sprite.Group()
background = pygame.sprite.Group()
menu_tiles = pygame.sprite.Group()
user_sprites = pygame.sprite.Group()
#------------------------------------------------------
pistol = [20, 3, 30]
shotgun = [150, 1.5, 10]
smg = [20, 10, 20]
rifle = [40, 5, 50]
#------------------------------------------------------
bullets = []
#------------------------------------------------------
difficulty = "Normal"
width = 1280
height = 720
tilesize = 48
FPS = 60
#------------------------------------------------------
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
display = pygame.display.get_surface()
clock = pygame.time.Clock()
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Sprites(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, size):
        super().__init__(group)
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except:
            self.image = image
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class Background(pygame.sprite.Sprite):
    def __init__(self, image, group):
        super().__init__(group)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (0,0))
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
class StartMenu():
    def __init__(self):
        self.running = True
        #------------------------------------------------------
        self.start_left = tilesize * 11.5
        self.start_right = tilesize * 13
        self.start_up = tilesize * 9.5
        self.start_down = tilesize * 10.5
        #------------------------------------------------------
        self.easy_left = tilesize * 11.5
        self.easy_right = tilesize * 12
        self.easy = "Pygame_GroupProject/Assets/Room/Easy.png"
        self.E = False
        #------------------------------------------------------
        self.normal_left = tilesize * 12
        self.normal_right = tilesize * 13.5
        self.normal = "Pygame_GroupProject/Assets/Room/Normal.png"
        self.N = False
        #------------------------------------------------------
        self.hard_left = tilesize * 13.5
        self.hard_right = tilesize * 14
        self.hard = "Pygame_GroupProject/Assets/Room/Hard.png"
        self.H = False
        #------------------------------------------------------
        self.diff_up = tilesize * 10.5
        self.diff_down = tilesize * 11.5
        #------------------------------------------------------
        self.p720_left = tilesize * 11.5
        self.p720_right = tilesize * 13
        self.p720 = "Pygame_GroupProject/Assets/Room/720Res.png"
        self.P7 = False
        #------------------------------------------------------
        self.p1080_left = tilesize * 13
        self.p1080_right = tilesize * 15
        self.p1080 = "Pygame_GroupProject/Assets/Room/1080Res.png"
        self.P1 = False
        #------------------------------------------------------
        self.res_up = tilesize * 11.5
        self.res_down = tilesize * 12.5
        #------------------------------------------------------
        self.diff = [self.E, self.N, self.H]
        self.res = [self.P7, self.P1]
    #------------------------------------------------------
    def Start(self):
        room = "Pygame_GroupProject/Assets/Room/Menu.png"
        Background(room, background)
    #------------------------------------------------------
    def Update(self):
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        if mouse_press[0]:
            if mouse_pos[0] > self.start_left and mouse_pos[0] < self.start_right:
                if mouse_pos[1] > self.start_up and mouse_pos[1] < self.start_down:
                    self.running = False
                #------------------------------------------------------
            if mouse_pos[1] > self.diff_up and mouse_pos[1] < self.diff_down:
                for d in self.diff:
                    d = False
                    #------------------------------------------------------
                if mouse_pos[0] > self.easy_left and mouse_pos[0] < self.easy_right:
                    self.E = True
                    #------------------------------------------------------
                elif mouse_pos[0] > self.normal_left and mouse_pos[0] < self.normal_right:
                    #------------------------------------------------------
                    self.N = True
                elif mouse_pos[0] > self.hard_left and mouse_pos[0] < self.hard_right:
                    self.H = True
                    #------------------------------------------------------
            if mouse_pos[1] > self.res_up and mouse_pos[1] < self.res_down:
                for r in self.res:
                    r = False
                    #------------------------------------------------------
                if mouse_pos[0] > self.p720_left and mouse_pos[0] < self.p720_right:
                    self.P7 = True
                    #------------------------------------------------------
                elif mouse_pos[0] > self.p1080_left and mouse_pos[0] < self.p1080_right:
                    self.P1 = True
                    #------------------------------------------------------
        if keys[pygame.K_r]:
            self.running = False

        self.ImageChanger()
    #------------------------------------------------------
    def ImageChanger(self):
        for d in self.diff:
            if d == True:
                self.difficulty.kill()
                pos_y = (self.diff_up + self.diff_down) / 2
                #------------------------------------------------------
                if d == self.E:
                    pos_x = (self.easy_left + self.easy_right) / 2
                    image = self.easy
                    #------------------------------------------------------
                elif d == self.N:
                    pos_x = (self.normal_left + self.normal_right) / 2
                    #------------------------------------------------------
                    image = self.normal
                elif d == self.H:
                    pos_x = (self.hard_left + self.hard_right) / 2
                    image = self.hard
                    #------------------------------------------------------
                self.difficulty = Sprites((pos_x, pos_y), image, [menu_tiles], (tilesize, tilesize))
                self.diff_rect = self.difficulty.rect
    #------------------------------------------------------
    def Run(self):
        self.Update()
        background.draw(display)
        menu_tiles.draw(display)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
menu = StartMenu()
menu.Start()
run = True

while run:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()

    if menu.running == True:
        menu.Run()
    else:
        run = False

    pygame.display.update()
    clock.tick(FPS)

print("Test_O_tesT")