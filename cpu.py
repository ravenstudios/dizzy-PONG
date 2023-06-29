import player
from constants import *


class Cpu(player.Player):       #Cpu class name
    def __init__(self, x):
        super().__init__(x)

    def chase(self, ball):
        if ball.yspeed < 0:
            if self.rect.top > 0 :
                self.rect.y -= self.speed
        else:
            if self.rect.bottom < GAME_HEIGHT:
                self.rect.y += self.speed

    def update(self, ball):           #tells ball to update and do math of movements checks for collisons
        self.chase(ball)
        self.check_collision(ball)






