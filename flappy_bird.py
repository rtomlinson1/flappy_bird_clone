# I found this rubric on reddit...Thought Id give it a shot
# Make an object appear on the screen.
# Make it something other than a rectangle (one student chose my face).
# Make it move SOMEHOW based on keyboard input. It doesn't have to be Flappy Bird movement.
# Make it bounce with gravity after given keyboard input. This is really the only thing that is math-y in the project.
# Prevent it from going off the screen.
# Make a pipe appear.
# Make the pipe move left across the screen.
# Make a bottom pipe appear below a top pipe and move together across the screen.
# Generate a new top/bottom pipe after a certain amount of time (or once the last pipes reach a certain point).
# Freeze everything if the bird collides with either pipe.
# Create a score that increases for every pipe the bird passes.
# Allow the player to reset the game after death.
# Hold onto a high score.
# Create frame animations for the bird.

import pygame

pygame.init()

# create display surface
window_size = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption('Flappy Bird Clone')

# fps display
clock = pygame.time.Clock()

# debug events
debug = True

# game logic
hitPipe = False

while not hitPipe:
    # utilize pygames event collection
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hitPipe = True
            if debug:
                # print out events to console
                print(event)

    # update screen
    pygame.display.update()

    # fps
    clock.tick(60)

pygame.quit()
quit()

