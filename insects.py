import pygame
import random
from math import sin, tan
from colors import *

MIN_VEL = 10

class Firefly():
    def __init__(self, screen_w, screen_h):
        self.r = random.randint(6, 16)
        self.x = random.randint(0, screen_w)
        self.y = random.randint(0, screen_h)
        self.pulse = random.randint(6,12) # determines the radius of the blink
        self.offset = random.randint(1,10) # offsets the blink pattern timing
        self.vel_x = self.rand_vel(40, 80)
        self.vel_y = self.rand_vel(40, 80)
    
    def rand_vel(self, low, high): # returns random velocity
        num = random.randint(low, high)
        if random.randint(0,1):
            return -num
        return num

    def update_radius(self, time_elapsed, freq_scale=1):
        self.r = sin((time_elapsed+self.offset)*freq_scale) * self.pulse
        
    def update_pos(self, time_elapsed, delta_t, screen_w, screen_h, vel):
        self.x += (self.vel_x) * delta_t
        self.y += self.vel_y * delta_t
        
        if self.x - self.r > screen_w: # checks right side
            self.x = -self.r
        
        elif self.x <= -self.r:
            self.x = screen_w + self.r
        
        if self.y + self.r <= 0: # checks top
            self.y = screen_h + self.r
        
        elif self.y - self.r >= screen_h:
            self.y = -self.r

    def draw(self, screen):
        if self.r > 0:
            pygame.draw.circle(screen, WHITE, [self.x,self.y], self.r+2, 2)
            pygame.draw.circle(screen, YELLOW, [self.x,self.y], self.r)
            