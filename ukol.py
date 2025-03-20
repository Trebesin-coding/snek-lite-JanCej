import pygame
import random
from sys import exit

pygame.init()

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

running = True


player_surf = pygame.image.load("pepan.png").convert_alpha()
player_size = 70  
player_surf = pygame.transform.scale(player_surf, (player_size, player_size))

player_speed = 10


player_x = 150
player_y = 150
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)


lives = 0
font = pygame.font.Font(None, 30)


mince_surf = pygame.image.load("mince.png").convert_alpha()
mince_size = 72
mince_surf = pygame.transform.scale(mince_surf, (mince_size, mince_size))

mince_color = (255, 0, 0)
mince_rect = pygame.Rect(random.randint(0, screen_width - mince_size), random.randint(0, screen_height - mince_size), mince_size, mince_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed

    if player_rect.colliderect(mince_rect):
        lives += 1
        mince_rect.x = random.randint(0, screen_width - mince_size)
        mince_rect.y = random.randint(0, screen_height - mince_size)

    screen.fill((255, 255, 255))

    screen.blit(player_surf, player_rect)
    screen.blit(mince_surf, mince_rect)

    lives_lives = font.render(f'lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_lives, (screen_width - 150, 10))

    pygame.display.update()
    clock.tick(60)
