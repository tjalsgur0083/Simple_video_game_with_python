import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
paddle = pygame.Rect(400, 500, 60, 10)

ball = pygame.Rect(400, 300, 10, 10)
ball_dx = 1
ball_dy = 1

bricks = [pygame.Rect(50 + 100 * i, 50 + 20 * j, 80, 10) for i in range(7) for j in range(3)]

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.bilt(text_surface, text_rect)

def game_over():
    draw_text("GAME OVER", 48, screen.get_width() / 2, screen.get_height() / 2)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def victory():
    draw_text("VICTORY!", 48, screen.get_width() / 2, screen.get_height() / 2)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

##game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 2
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.right += 2

    ball.left += ball_dx
    ball.top += ball_dy

    if ball.left <= 0 or ball.right >= 800:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
    
    if ball.top >= paddle.bottom:
        game_over()

    if ball.colliderect(paddle):
        ball_dy *= -1

    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_dy *= -1

    if len(bricks) == 0:
        victory()

    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.rect(screen, (255, 255, 255),  ball)
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), brick)

    pygame.display.flip()

    pygame.time.delay(10)