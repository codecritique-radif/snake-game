import pygame
import random

# Initialize the game
pygame.init()

# Set up the screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Define the snake
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_x_change = 0
snake_y_change = 0

# Define the food
food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Game over flag
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0

    # Update the snake's position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with the boundaries of the screen
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over = True

    # Create the snake's body
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    # Remove the tail if the snake is longer than snake_length
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with the snake's body
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Update the screen
    screen.fill(black)
    pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])
    for segment in snake_list:
        pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])

    pygame.display.update()

    # Check if the snake has eaten the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Control the game speed
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
