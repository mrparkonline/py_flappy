# Learning Pygame w/ Flappy Bird
# Learning Source #1: https://www.youtube.com/watch?v=jO6qQDNa2UY
# Learning Source #2: https://www.youtube.com/watch?v=UZg49z76cLw

import pygame, random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

def create_pipe():
    pipe_spacing = list(range(200, 360, 20))
    pipe_y = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, pipe_y))
    top_pipe = pipe_surface.get_rect(midbottom=(700, pipe_y - random.choice(pipe_spacing)))
    return (bottom_pipe, top_pipe)

def move_pipes(pipes):
    # argument = list of pipes
    for pipe in pipes:
        pipe.centerx -= 3

    pipes = list(filter(lambda x: x.centerx >= 0, pipes))

    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe): # collision are heavy performance hit
            # Two rectangle collision
            print('Pipe Collision')
            return False
    # end of pipe collision

    if bird_rect.top <= -100:
        print('out of bounds')
        return False

    if bird_rect.bottom >= 900:
        gravity = 0
        return False

    return True


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
game_active = True

# assets
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = [] # create pipes based on a timer
pipe_height = [h for h in range(450, 850, 50)] # variable heights

SPAWNPIPE = pygame.USEREVENT # custom event?
pygame.time.set_timer(SPAWNPIPE, 1200) # 2nd argument is in milliseconds


# game loop
run = True
while run:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if game_active and event.key == pygame.K_SPACE:
                bird_movement = 0 # removes the effect of gravity when space is pressed
                bird_movement -= 9
                print("flap")
            if not game_active and pygame.K_SPACE:
                # reset the game when
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                gravity = 0.25

        if event.type == SPAWNPIPE:
            print('Make Pipe!')

            # add a pipe in pipe_list
            pipe_list.extend(create_pipe())
            #print(pipe_list)

    # end of event loop

    screen.blit(bg_surface,(0,0)) # Background

    if game_active:
        # Draw Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_list)

        # Draw pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    else:
        screen.blit(bird_surface, bird_rect)
        print('Game Over')

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
