import pygame
import datetime as dt
from insects import Firefly
from colors import *
from time import sleep
from math import sin,cos

SCREEN_W, SCREEN_H = 900, 900
FPS = 60
NUM_FIREFLIES = 20


start_time = dt.datetime.now()
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

bg_img = pygame.image.load("backgrounds/forest8.jpg")

def game_loop():

    fireflies = [Firefly(SCREEN_W, SCREEN_H) for i in range(NUM_FIREFLIES)]

    while True:
    
        time_elapsed = (dt.datetime.now() - start_time).total_seconds()
        delta_t = clock.tick(FPS) / 1000

        screen.fill(BLACK)
        bg_img_y = cos(time_elapsed * 0.4) * 300 - 300#-1 * abs(sin(time_elapsed * 0.1) * 300)
        screen.blit(bg_img, [0, bg_img_y])
        print(bg_img_y)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        
        for firefly in fireflies:
            firefly.update_radius(time_elapsed, 2)
            firefly.update_pos_rng(time_elapsed, delta_t, SCREEN_W, SCREEN_H)
            firefly.draw(screen, time_elapsed)

        pygame.display.update()
        #sleep(0.1)


if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()