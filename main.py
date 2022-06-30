import pygame
import datetime as dt
from insects import Firefly
from colors import *

SCREEN_W, SCREEN_H = 600, 600
FPS = 60
NUM_FIREFLIES = 25


start_time = dt.datetime.now()
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()


def game_loop():

    vel = 0.01
    fireflies = [Firefly(SCREEN_W, SCREEN_H) for i in range(NUM_FIREFLIES)]

    while True:
        
        vel += 1
        time_elapsed = (dt.datetime.now() - start_time).total_seconds()
        delta_t = clock.tick(FPS) / 1000

        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        
        for firefly in fireflies:
            firefly.update_radius(time_elapsed, 2)
            firefly.update_pos(time_elapsed, delta_t, SCREEN_W, SCREEN_H, vel)
            firefly.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()