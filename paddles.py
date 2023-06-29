import pygame
from constants import *


class Paddle():
    def __init__(self, x): #defines (draws) the paddle and coordinates for paddle; the __init__ is the constructor
        self.rect = pygame.Rect(x, 0, 32, 200)
        self.rect.y = 300 - self.rect.height // 2
        self.speed = 5

    def update(self):           #tells ball to update and do math of movements checks for collisons
        pass



    def draw(self, surface):
        pygame.draw.rect(surface, WHITE,(self.rect.x, self.rect.y, self.rect.width, self.rect.height))

