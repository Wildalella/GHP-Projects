# Example file showing a circle moving on screen
import random
import pygame
import pygame as pg # Alias to 
import os


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
wall_pos = pygame.Rect(30, 30, 100, 100)
color = (255,0,0)

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "assets")



# Load Sound // Help function to lead resources
def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound



def direction():
    r1 = random.randint(0,3)
    if r1 == 0:
        player_pos.x -=  1000 * dt
    if r1 == 1:
        player_pos.x +=  1000 * dt
    if r1 == 2:
        player_pos.y -=  1000 * dt
    if r1 == 3:
        player_pos.y +=  1000 * dt


# Wraps character around screen
def wrapped():
    if player_pos.x > screen.get_width():
        player_pos.x = 0
    elif player_pos.x < 0:
        player_pos.x = screen.get_width()
    elif player_pos.y > screen.get_height():
        player_pos.y = 0
    elif player_pos.y < 0:
        player_pos.y = screen.get_height()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

     # call Sprite initializer //int local variables
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.rect(screen, color, wall_pos)

    # Creat Sound
    annoyingSound = load_sound("high_piched.mp3")
    warningSound = load_sound("virus_warning.mp3")
    #warningSound.play()

    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Get to the Red Square to Win", True, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
        screen.blit(text, textpos)

   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction()
        wrapped()
        annoyingSound.play()
    if keys[pygame.K_s]:
        direction()
        wrapped()
        annoyingSound.play()
    if keys[pygame.K_a]:
        direction()
        wrapped()
        annoyingSound.play()
    if keys[pygame.K_d]:
        direction()
        wrapped()
        annoyingSound.play()


    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()