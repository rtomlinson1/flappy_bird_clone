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
import time
import random

pygame.init()

# create display surface
disp_h = 500
disp_w = 800
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 255)
blue = (0, 0, 255)
sky = (183, 233, 255)


game_display = pygame.display.set_mode((disp_w, disp_h))

# game title
pygame.display.set_caption('Flappy Bird Clone')

# fps display
clock = pygame.time.Clock()


def baths(bath_x, bath_y, bath_w, bath_h, bath_color):
    pygame.draw.rect(game_display, bath_color, [bath_x, bath_y, bath_w, bath_h])


# f_bird images initial state
def bird_pic(pic):
    pic = pygame.image.load(pic)
    return pic


f_bird = bird_pic('f_bird_down.png')

bird_h = 66

# bird bath for obstacle
bath = pygame.image.load('b_bath.png')

# debug events
debug = True


# function to display bird
def bird(x, y):
    game_display.blit(f_bird, (x, y))


# render font and get rectangle around text
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


# endgame message
def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rectangle = text_objects(text, large_text)
    text_rectangle.center = ((disp_w/2), (disp_h/2))
    game_display.blit(text_surface, text_rectangle)
    pygame.display.update()

    time.sleep(2)

    main_loop()


def hit_pipe():
    message_display('You crashed!')


def main_loop():
    # display coordinates
    x = (disp_w * 0.06)
    y = (disp_h * 0.4)
    y_change = 0

    # obstacle creation
    bath_start_x = random.randrange(250, disp_w)
    bath_start_y = 300
    bath_speed = 3
    bath_width = 75
    bath_height = 200

    bath_start_x2 = random.randrange(200, disp_w)
    bath_start_y2 = 0
    bath_speed2 = 3
    bath_width2 = 75
    bath_height2 = 175

    bath_start_x3 = random.randrange(250, disp_w)
    bath_start_y3 = 300
    bath_speed3 = 3
    bath_width3 = 75
    bath_height3 = 200

    bath_start_x4 = random.randrange(250, disp_w)
    bath_start_y4 = 0
    bath_speed4 = 3
    bath_width4 = 75
    bath_height4 = 200



    # game logic
    exit_game = False
    y_change = 3
    while not exit_game:
        # utilize pygames event collection

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_change = -3
                    bird_pic('f_bird_down.png')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_change = 3
                    bird_pic('f_bird.png')

            if debug:
                # print out events to console
                print(event)

        y += y_change
        # draw bird and background
        game_display.fill(sky)

        # def baths(bath_x, bath_y, bath_w, bath_h, bath_color):
        #     pygame.draw.rect(game_display, color, [bath_x, bath_y, bath_w, bath_h])
        baths(bath_start_x, bath_start_y, bath_width, bath_height, red)
        bath_start_x -= bath_speed

        baths(bath_start_x2, bath_start_y2, bath_width2, bath_height2, red)
        bath_start_x2 -= bath_speed2

        baths(bath_start_x3, bath_start_y3, bath_width3, bath_height3, black)
        bath_start_x3 -= bath_speed

        baths(bath_start_x4, bath_start_y4, bath_width4, bath_height4, black)
        bath_start_x4 -= bath_speed

        bird(x, y)

        # define boundaries
        if y > (disp_h - bird_h) or y < 0:
            y_change = 0
            hit_pipe()

        if bath_start_x < -60:
            bath_start_x = random.randrange(800, 1600)

        if bath_start_x2 < -60:
            bath_start_x2 = random.randrange(800, 1600)

        if bath_start_x3 < -60:
            bath_start_x3 = random.randrange(800, 1600)

        if bath_start_x4 < -60:
            bath_start_x4 = random.randrange(800, 1600)

        # logic for collisions
        if x < bath_start_x + bird_h:
            print(1)
            if y > bath_start_y and y < bath_start_y + bath_height or x + bird_h > bath_start_y and y + bird_h < bath_start_y + bath_height:
                print(2)
                hit_pipe()

        # update screen
        pygame.display.update()

        # fps
        clock.tick(60)

main_loop()
pygame.quit()
quit()

