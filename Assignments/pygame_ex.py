import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Tortoise Race")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)  # Define BLACK color

# Load tortoise images
tortoise1_image = pygame.image.load('moonwalk.gif')  # Replace with your image path
tortoise2_image = pygame.image.load('moonwalk.gif')  # Replace with your image path

# Scale images to appropriate size (optional)
tortoise1_image = pygame.transform.scale(tortoise1_image, (50, 30))
tortoise2_image = pygame.transform.scale(tortoise2_image, (50, 30))

# Initial positions
x1, y1 = 50, 150
x2, y2 = 50, 100
speed1 = 0
speed2 = 0

# Font for the result
font = pygame.font.Font(None, 36)

# Function to display the result
def display_result(result):
    text = font.render(result, True, (0, 0, 0))
    screen.blit(text, (200, 150))

# Main game loop
running = True
race_in_progress = False
while running:
    screen.fill(WHITE)

    # Draw the race track and finish line
    pygame.draw.line(screen, BLACK, (50, 250), (450, 250), 2)  # Race track line
    pygame.draw.line(screen, RED, (450, 0), (450, 300), 2)  # Finish line

    # Draw the tortoises using images
    screen.blit(tortoise1_image, (x1, y1))  # Tortoise 1 (using image)
    screen.blit(tortoise2_image, (x2, y2))  # Tortoise 2 (using image)

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not race_in_progress:
                race_in_progress = True
                x1, x2 = 50, 50  # Reset positions
                y1, y2 = 150, 100
                speed1 = random.randint(5, 10)  # Random speed for tortoise 1
                speed2 = random.randint(5, 10)  # Random speed for tortoise 2

    if race_in_progress:
        # Move the tortoises
        x1 += speed1
        x2 += speed2

        # Check if any tortoise reached the finish line
        if x1 >= 450 and x2 >= 450:
            result = "It's a tie!"
            race_in_progress = False
        elif x1 >= 450:
            result = "Tortoise 1 wins!"
            race_in_progress = False
        elif x2 >= 450:
            result = "Tortoise 2 wins!"
            race_in_progress = False

        # Display result when race ends
        if not race_in_progress:
            display_result(result)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
