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
video_info = pygame.display.Info()
width, height = video_info.current_w, video_info.current_h

if height < 1080:
    tilesize = 48
    difference = 1
elif height >= 1080 and height < 1440:
    tilesize = 64
elif height >= 1440 and height < 2160:
    tilesize = 96
elif height >= 2160:
    tilesize = 128

print(tilesize)

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
        self.start_left = tilesize * 12.5
        self.start_right = tilesize * 14
        self.start_up = tilesize * 10.5
        self.start_down = tilesize * 11.5
        #------------------------------------------------------
        self.easy_left = tilesize * 12.5
        self.easy_right = tilesize * 13
        self.easy = "Pygame_GroupProject/Assets/Room/Easy.png"
        #------------------------------------------------------
        self.normal_left = tilesize * 13
        self.normal_right = tilesize * 14.5
        self.normal = "Pygame_GroupProject/Assets/Room/Normal.png"
        #------------------------------------------------------
        self.hard_left = tilesize * 14.5
        self.hard_right = tilesize * 15
        self.hard = "Pygame_GroupProject/Assets/Room/Hard.png"
        #------------------------------------------------------
        self.diff_up = tilesize * 11.5
        self.diff_down = tilesize * 12.5
        #------------------------------------------------------
        diff_x = (self.normal_left + self.normal_right) / (2 * difference)
        diff_y = (self.diff_up + self.diff_down) / (2 * difference)
        self.difficulty = Sprites((diff_x - 30, diff_y - 30), self.normal, [menu_tiles], (tilesize, tilesize))
        self.diff_rect = self.difficulty.rect
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
                    #------------------------------------------------------
                if mouse_pos[0] > self.easy_left and mouse_pos[0] < self.easy_right:
                    self.DiffChanger("easy", mouse_pos[0], mouse_pos[1])
                    #------------------------------------------------------
                elif mouse_pos[0] > self.normal_left and mouse_pos[0] < self.normal_right:   
                    self.DiffChanger("normal", mouse_pos[0], mouse_pos[1])
                    #------------------------------------------------------
                elif mouse_pos[0] > self.hard_left and mouse_pos[0] < self.hard_right:
                    self.DiffChanger("hard", mouse_pos[0], mouse_pos[1])
                    #------------------------------------------------------              
        if keys[pygame.K_r]:
            self.running = False   
    #------------------------------------------------------
    def DiffChanger(self, diff, x, y):
        if diff == "easy":
            image = self.easy
        elif diff == "normal":
            image = self.normal
        elif diff == "hard":
            image = self.hard

        self.difficulty.kill()
        self.difficulty = Sprites((x, y), image, [menu_tiles], (tilesize, tilesize))
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

    gc.collect()
    pygame.display.update()
    clock.tick(FPS)