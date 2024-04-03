import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BG_COLOR = (0, 0, 0)
CELL_SIZE = 32  # Size of each maze cell

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Define your maze using a 2D array (0 for empty space, 1 for walls)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Load maze tile images (e.g., wall_image, pellet_image)

# Load Pac-Man image
pacman_image = pygame.image.load("pacman.png")  # Replace with the path to your Pac-Man image

# Pac-Man position and speed
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Pac-Man direction (initially, Pac-Man doesn't move)
pacman_direction = "none"

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle Pac-Man's movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_direction = "left"
    if keys[pygame.K_RIGHT]:
        pacman_direction = "right"
    if keys[pygame.K_UP]:
        pacman_direction = "up"
    if keys[pygame.K_DOWN]:
        pacman_direction = "down"

    # Update Pac-Man's position based on the direction
    if pacman_direction == "left":
        pacman_x -= pacman_speed
    elif pacman_direction == "right":
        pacman_x += pacman_speed
    elif pacman_direction == "up":
        pacman_y -= pacman_speed
    elif pacman_direction == "down":
        pacman_y += pacman_speed

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x, y = col * CELL_SIZE, row * CELL_SIZE
            if maze[row][col] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, CELL_SIZE, CELL_SIZE))  # Draw walls
            else:
                # Draw pellets (adjust position based on your grid)
                pygame.draw.circle(screen, (255, 255, 255), (x + CELL_SIZE // 2, y + CELL_SIZE // 2), 5)

    # Draw Pac-Man
    screen.blit(pacman_image, (pacman_x, pacman_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
