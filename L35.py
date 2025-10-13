import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rectangle and Text Example")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

# Font for text
font = pygame.font.Font(None, 36)  # None = default font, 36 = font size

# Text to display
text = font.render("Hello, Pygame!", True, black)

# Rectangle dimensions
rect_x = 200
rect_y = 150
rect_width = 200
rect_height = 100

# Game loop
running = True
while running:
    # Fill the background
    screen.fill(white)

    # Draw rectangle
    pygame.draw.rect(screen, blue, (rect_x, rect_y, rect_width, rect_height))

    # Draw text (centered on the rectangle)
    text_rect = text.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
    screen.blit(text, text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
