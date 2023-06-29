import pygame as pgk     #period to take on part of a library
import paddles
from constants import *


class Player(paddles.Paddle):       #Player is paddle; class is the blueprint to make objects
    def __init__(self, x):
        super().__init__(x)     #calling constructor for parent object


    def update(self, ball):           #tells ball to update and do math of movements checks for collisons
        keys = pgk.key.get_pressed()

        if keys[pgk.K_UP]:
            if self.rect.y > 0:     #top is self.rect.y, tells player it cannot go past 0 (top of screen)
                self.rect.y -= self.speed   #if it hits the paddle mi=ove in opposite direction

        if keys[pgk.K_DOWN]:
            if self.rect.y + self.rect.height < GAME_HEIGHT:    #paddle can't go past bottom
                self.rect.y += self.speed

        self.check_collision(ball)

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            ball.reverse()
