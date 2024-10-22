from math import cos, sin, pi
import sys
import pygame 


# defintion of colors 
black = (0, 0, 0)
white = (255, 255, 255)

# setting screen bounds
width = 600
height = 600

def main():

    # initialising screen
    screen = pygame.display.set_mode((width, height))
    screen.fill(black)

    # setting framerates and durations
    clock = pygame.time.Clock()
    fps = 60
    precision = 60
    duration = 3
    frames = duration * fps

    # setting loop 
    frame = 0
    while frame <= frames:
        # ticking clock
        clock.tick(fps)

        # doing animation
        for i in range(precision):
            prog = frame / frames + i / precision / frames
            pygame.draw.circle(
                screen,
                white,
                circle(prog),
                radius=1,
            )

        # counting frames
        frame += 1

        # looping the animation by resetting frames to zero
        if frame > frames:
            frame = 0
            screen.fill(black)

        # updating animation by flipping the screen
        pygame.display.flip()

        # listening for the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def circle(progress):
    return (
        width//2 + width//2 * cos(2 * pi * progress),
        height//2 + height//2 * sin(2 * pi * progress)
    )

if __name__ == "__main__":
    main()