import pygame
import random
from constants import *

class Ball():
    def __init__(self):         #defines (draws) the ball and coordinates for ball; the __init__ is the constructor
        #self.x = random.randint(0, GAME_WIDTH - 50)
        #self.y = random.randint(0, GAME_HEIGHT - 50)
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.radius = 32
        self.xspeed = 8
        self.yspeed = 8
        self.player_score = 0
        self.cpu_score = 0
        self.reset()



    def update(self):           #tells ball to update and do math of movements checks for collisons
        self.rect = self.rect.move(self.xspeed, self.yspeed)
        #if self.x < 0:
        #   self.xspeed = -self.xspeed
        if self.rect.y > GAME_HEIGHT:
            self.yspeed = -self.yspeed
        if self.rect.y < 0:
            self.yspeed = -self.yspeed
        if self.rect.x < -self.rect.width:  #tells the computer to reset the ball if it goes outside boundaries; left side CPU
            self.reset()
            self.cpu_score += 1                 #add to CPU score
        if self.rect.x > GAME_WIDTH:
            self.reset()
            self.player_score +=1                #add to player score


    #def get_coords(self):
        #return{"x": self.rect.x,             #"key":value; if you want the value ask for key
         #      "y": self.rect.y,
          #     "radius": self.radius}

    def reverse(self):      #how we reverse the ball
        if self.xspeed > 0:
            self.rect = self.rect.move(-10, 0)
        else:
            self.rect = self.rect.move(10, 0)

        self.xspeed = -self.xspeed

    def reset(self):
        self.rect.x = GAME_WIDTH // 2 - self.rect.width // 2
        self.rect.y = GAME_HEIGHT // 2 - self.rect.height // 2
        x = random.randint(0, 1)
        if x:                                   #asking for true/false
            self.xspeed = -self.xspeed
        pygame.time.delay(500)
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE,(self.rect.x, self.rect.y), self.radius)

