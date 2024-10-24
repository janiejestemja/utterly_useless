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
    colour = "b"
    colour_cd = "d"
    while frame <= frames:
        # ticking clock
        clock.tick(fps)


        # doing animation
        for i in range(precision):
            # parameterisation of current frame
            prog = frame / frames + i / precision / frames
            # drawing a circle
            pygame.draw.circle(
                screen,
                dyn_colour(0, colour),
                circle(prog),
                radius=1,
            )
            # drawing another circle
            pygame.draw.circle(
                screen,
                dyn_colour(0, colour),
                circle(prog, reversed=True),
                radius=1,
            )
            # drawing a spiral
            pygame.draw.circle(
                screen,
                dyn_colour(frame, colour_cd),
                spiral(prog),
                radius=1,
            )
            # drawing another spiral
            pygame.draw.circle(
                screen,
                dyn_colour(frame, colour_cd),
                spiral(prog, reversed=True),
                radius=1,
            )

        # counting frames
        frame += 1

        # looping the animation by resetting frames to zero
        if frame > frames:
            frame = 0
        
        # changing colour periodically
        if frame == frames:
            match colour:
                case "a":
                    colour = "b"
                case "b":
                    colour = "a"
        
        if frame == frames // 2:
            match colour_cd:
                case "c":
                    colour_cd = "d"
                case "d":
                    colour_cd = "c"
            

        # updating animation by flipping the screen
        pygame.display.flip()

        # listening for the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def circle(progress, reversed=False):
    if not reversed:
        return (
            width//2 + width//2 * cos(2 * pi * progress),
            height//2 + height//2 * sin(2 * pi * progress)
        )
    else:
        return (
            width//2 - width//2 * cos(2 * pi * progress),
            height//2 - height//2 * sin(2 * pi * progress)
        )


def spiral(progress, reversed=False):
    if not reversed:
        return (
            width//2 + progress * width//2 * cos(2 * pi * progress),
            height//2 + progress * height//2 * sin(2 * pi * progress)
        )
    else:
        return (
            width//2 - progress * width//2 * cos(2 * pi * progress),
            height//2 - progress * height//2 * sin(2 * pi * progress)
        )

def dyn_colour(frame, colour_var):
    match colour_var:
        case "a":
            return (0 + frame, 0 + frame, 0 + frame)
        case "b":
            return (180 - frame, 180 - frame, 180 - frame)
        case "c":
            return (0 , 0 , 0)
        case "d":
            return (0, 180 - frame, 180 - frame)


if __name__ == "__main__":
    main()