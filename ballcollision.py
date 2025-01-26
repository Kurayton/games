import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball")

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Ball properties
    ball_radius = 15
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed_x, ball_speed_y = 4, 3

    # Clock to control frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update ball position
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Check for collisions with walls
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_speed_x = -ball_speed_x
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # Clear the screen
        screen.fill(WHITE)

        # Draw the ball
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
