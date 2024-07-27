import pygame
import sys
import random
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_f 


# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fruit Ninja')




# Load background image
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load background music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Define colors
white = (255, 255, 255)

# Define button properties
button_font = pygame.font.Font(None, 50)

# Game variables
score = 0
lives = 3

# Define Fruit class
class Fruit(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, screen_width - 50)  # Random x position
        self.rect.y = random.randint(-100, -50)  # Start above the screen
        self.speed = random.randint(3, 6)  # Random speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.kill()  # Remove object when it goes off screen

# Create sprite groups
all_fruits = pygame.sprite.Group()

# Maximum number of fruits allowed
max_fruits = 10

# Tick delay variables
tick_delay = 0
max_tick_delay = 60  # Adjust this value as needed for longer or shorter delays

# Life font
life_font = pygame.font.Font(None, 36)

def draw_lives():
    life_text = life_font.render(f"Lives: {lives}", True, white)
    screen.blit(life_text, (20, 20))

def draw_score():
    score_text = life_font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (screen_width - 150, 20))

def draw_buttons():
    # Add any buttons if needed (not typically in Fruit Ninja style game)
    pass

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    keys = pygame.key.get_pressed()

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_f:
                pygame.display.toggle_fullscreen()

    screen.fill((0, 0, 0))  # Clear the screen

    # Draw background
    screen.blit(background_image, (0, 0))

    # Game logic
    if not lives <= 0:
        # Tick delay logic for spawning fruits
        if tick_delay > 0:
            tick_delay -= 1
        elif len(all_fruits) < max_fruits:
            new_fruit = Fruit('apple.png')  # Replace with actual fruit images
            all_fruits.add(new_fruit)
            tick_delay = max_tick_delay

        # Update and draw all fruits
        all_fruits.update()
        all_fruits.draw(screen)

        # Collision detection with mouse click or swipe
        for fruit in all_fruits:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fruit.rect.collidepoint(event.pos):
                    fruit.kill()
                    score += 1
            # You can add touch or swipe detection here for mobile support

        # Check if fruits hit the ground
        for fruit in all_fruits:
            if fruit.rect.y >= screen_height:
                fruit.kill()
                lives -= 1

        # Draw game info
        draw_lives()
        draw_score()

    else:
        # Game over logic (can be refined with more options like restart)
        game_over_text = button_font.render("GAME OVER", True, white)
        screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2))

    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate at 60 FPS

pygame.quit()
sys.exit()
