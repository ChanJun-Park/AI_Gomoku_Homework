import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Go Board Test')

#색깔 설정하기
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
YELLOW = (255, 211,  21)

goBoardImg = pygame.image.load('go.png')
goBoardImgX = 200
goBoardImgY = 100

mousex = 0
mousey = 0

DISPLAYSURF.fill(WHITE);
DISPLAYSURF.blit(goBoardImg, (goBoardImgX, goBoardImgY))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            print(mousex, mousey)
            pygame.draw.circle(DISPLAYSURF, BLACK, (mousex, mousey), 10, 0)
    pygame.display.update()