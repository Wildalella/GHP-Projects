# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos_two = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def wrapped():
        if player_pos.x > screen.get_width():
            player_pos.x = 0
        if player_pos.x < 0:
            player_pos.x = screen.get_width
        if player_pos.y > screen.get_height():
            player_pos.y = 0
        if player_pos.y < 0:
            player_pos.y = screen.get_height

# Player Two
        if player_pos_two.x > screen.get_width():
            player_pos_two.x = 0
        if player_pos_two.x < 0:
           player_pos_two.x = screen.get_width
        if player_pos_two.y > screen.get_height():
            player_pos_two.y = 0
        if player_pos_two.y < 0:
            player_pos_two.y = screen.get_height    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", player_pos_two, 40)



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        wrapped()
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        wrapped()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        wrapped()
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        wrapped()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos_two.y -= 300 * dt
        wrapped()
    if keys[pygame.K_DOWN]:
        player_pos_two.y += 300 * dt
        wrapped()
    if keys[pygame.K_LEFT]:
        player_pos_two.x -= 300 * dt
        wrapped()
    if keys[pygame.K_RIGHT]:
        player_pos_two.x += 300 * dt
        wrapped()
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()