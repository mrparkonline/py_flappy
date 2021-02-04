# Learning Pygame w/ Flappy Bird
# Learning Source #1: https://www.youtube.com/watch?v=jO6qQDNa2UY
# Learning Source #2: https://www.youtube.com/watch?v=UZg49z76cLw

import pygame

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

pygame.init()

WIDTH, HEIGHT = 576, 1024
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

# assets
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

# game loop
run = True
while run:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0 # removes the effect of gravity when space is pressed
                bird_movement -= 12
                print("flap")
    # end of event loop
    screen.blit(bg_surface,(0,0)) # Background

    # Draw Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    # end of Floor

    pygame.display.update()
    clock.tick(120)
# end of game while loop
pygame.quit() # Closing the window == quit event
