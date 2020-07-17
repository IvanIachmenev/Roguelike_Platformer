import pygame

# from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_mode((600, 400))

    clock = pygame.time.Clock()
    FPS = 60
    
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()