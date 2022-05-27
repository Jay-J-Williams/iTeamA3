import pygame, sys, random, gc
pygame.init()
#------------------------------------------------------
hud = pygame.sprite.Group()
aliens = pygame.sprite.Group()
menu_display = pygame.sprite.Group()
room_display = pygame.sprite.Group()
user_sprites = pygame.sprite.Group()
#------------------------------------------------------
pistol = [20, 3, 30]
shotgun = [150, 1.5, 10]
smg = [20, 10, 20]
rifle = [40, 5, 50]
#------------------------------------------------------
bullets = []
enemies = []
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
class Menu():
    def __init__(self):
        self.running = True
        room = "Pygame_GroupProject/Assets/Room/Menu.png"
        Background(room, menu_display)
        #------------------------------------------------------
    def Update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            self.running = False  
        elif keys[pygame.K_e]:
            difficulty = "easy"
            print(difficulty)
        elif keys[pygame.K_n]:
            difficulty = "normal"
            print(difficulty)
        elif keys[pygame.K_h]:
            difficulty = "hard"
            print(difficulty)
    #------------------------------------------------------
    def Run(self):
        self.Update()
        menu_display.draw(display)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
menu = Menu()
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