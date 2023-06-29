import pygame
import balls
import player
import cpu
from constants import *


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()           #tells pygame to start/starts game engine
ball = balls.Ball() #create an object called ball
ballz = []
for i in range(0):          #create multiple balls
    ballz.append(balls.Ball())
player = player.Player(0) #         #creates object called player
cpu = cpu.Cpu(GAME_WIDTH - player.rect.width)       #creates object called CPU

def main():     #main game route
    running = True

    while running:
        clock.tick(TICK_RATE) #sets FPS (frames per second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                #if event.key == pygame.K_r:
                    #board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill(BLACK) #erase the screen
    ball.draw(surface)
    player.draw(surface)
    cpu.draw(surface)
    draw_court(surface)
    draw_score(surface)
    for b in ballz:
        b.draw(surface)

    pygame.display.flip()   #tells us to move onto the next frame

def update():
    ball.update()
    player.update(ball)
    cpu.update(ball)
    for b in ballz:
        b.update()

def draw_court(surface):
    how_many = 20
    how_long = GAME_HEIGHT // 40
    w = 20
    for i in range(how_many):
        y = i *  (how_long * 2) + 10
        pygame.draw.rect(surface, WHITE, (GAME_WIDTH // 2 - w // 2, y, w, how_long))

def draw_score(surface):
    font = pygame.font.Font("freesansbold.ttf", 32)
    player_score_text = font.render(str(ball.player_score), True, WHITE, BLACK)
    cpu_score_text = font.render(str(ball.cpu_score), True, WHITE, BLACK)
    player_textrect = player_score_text.get_rect()
    cpu_textrect = cpu_score_text.get_rect()
    player_textrect.center = (GAME_WIDTH // 2 - 50, 50)
    cpu_textrect.center = (GAME_WIDTH // 2 + 50, 50)
    surface.blit(player_score_text, player_textrect)
    surface.blit(cpu_score_text, cpu_textrect)



if __name__ == "__main__":              #tells it to run the main function
    main()