# Learning Pygame w/ Flappy Bird
# Learning Source #1: https://www.youtube.com/watch?v=jO6qQDNa2UY
# Learning Source #2: https://www.youtube.com/watch?v=UZg49z76cLw

import pygame

pygame.init() # What is the purpose of this?
# TechWithTim does not have this
# Clear Code did.

WIDTH, HEIGHT = 576, 1024 # constant dimensions for game window

# display object has a set_mode method to set the size of the game window
# Provide a tuple argument of width and height.
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# can be called "screen"

# Colour dict
colour = {
    'white' : (255,255,255)
}

# Controlling the Speed of the Game's Loop --> Frames Per Second
FPS = 120 # Telling the game to update 120 frames per second

# Inserting Assets into the game --> Must have them as variables
BG_SURFACE = pygame.image.load('./assets/background-day.png').convert()
# .load() grabs the asset file
# .convert() a method optimizes the image file for pygame (optional)
BG_SURFACE = pygame.transform.scale2x(BG_SURFACE) # transform object's scale2x method
# helps to scale an assets by doubling its size

# Floor Asset
FLOOR = pygame.image.load('./assets/base.png').convert()
FLOOR = pygame.transform.scale2x(FLOOR)

# Bird Asset
BIRD_SURFACE = pygame.image.load('./assets/yellowbird-midflap.png').convert()
BIRD_SURFACE = pygame.transform.scale2x(BIRD_SURFACE)
BIRD_RECT = BIRD_SURFACE.get_rect(center = (100, 512)) # apply a rectangle on surface to help collision

def initialize():
    # Setting the Window Title of the Game
    pygame.display.set_caption('Flappy!')

    # set_caption method of display object allows us to change the window title
    # Start of editing our Game WINDOW
    WINDOW.fill(colour['white']) # .fill() method takes a rgb tuple
    # End of Game WINDOW editing

    # add BG_SURFACE onto display surface
    WINDOW.blit(BG_SURFACE, (0,0)) # .blit() method puts one surface on another
    # blit() :: 2 argumemnts required
    # -- 1. The surface we want to put on the WINDOW
    # -- 2. location (x,y) tuple ... (0,0) occurs top left of the WINDOW

    # Initialize Bird
    WINDOW.blit(BIRD_SURFACE, BIRD_RECT)

    # For any changes in the Game Window: update!
    pygame.display.update()
# end of initialize()

def draw(asset_name, location):
    ''' draw functions draws the given asset at the location '''
    WINDOW.blit(asset_name, location)
    #pygame.display.update()
# end of draw

# creating main
def main():
    # Game Variables
    F_X = 1 # Floor X value
    gravity = 0.25
    bird_movement = 0
    # end of Game Variables

    clock = pygame.time.Clock() # Declaring a clock object

    # initializing a Game Loop
    run = True
    while run:
        # Sychronize the Clock to set FPS
        clock.tick(FPS) # allows our game loop to run at 60 times a second

        # Creating an event Loop
        # Event driven game development
        for event in pygame.event.get():
            # pygame.event.get() returns a list of all events
            # Each event in this for loop are called "event"

            # Event 1: Quitting the game
            if event.type == pygame.QUIT:
                print('User quitted the game.')
                run = False
        # end of event for loop

        # Get the floor moving
        F_X -= 1
        draw(FLOOR, (F_X, 900))
        draw(FLOOR, (F_X+576, 900))
        if F_X <= -576:
            # Resetting F_X so that it looks like an infinite scroll
            F_X = 0

        # end of floor moving

        # Apply Gravity to Bird
        bird_movement += gravity
        BIRD_RECT.centery += bird_movement
        draw(BIRD_SURFACE, BIRD_RECT)

        # Display Update
        pygame.display.update()

    # end of game while loop

    pygame.quit() # Closing the window == quit event
# end of main()

# when the file executed only execute the main function
if __name__ == "__main__":
    initialize()
    main()
