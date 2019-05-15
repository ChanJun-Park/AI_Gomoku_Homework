import pygame, sys
from pygame.locals import *

BOARDWIDTH = 4
BOARDHEIGHT = 4
TITLESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

BLACK = (0,0,0)
WHITE = (255,255,255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

BGCOLOR = DARKTURQUOISE
TITLECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BGCOLOR

BASICFONTSIZE = 20
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TITLESIZE * BOARDWIDTH + (BOARDWIDTH - 1)))/2)
YMARGIN = int((WINDOWHEIGHT - (TITLESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1)))/2)
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT,\
        NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('button Test')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TITLECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if RESET_RECT.collidepoint(event.pos):
                    print("리셋 버튼이 눌림")
                    pass

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def makeText(text, color, bgcolor, top, left):
    #Surface 객체와 Rect 객체를 만들어 텍스트를 보여준다
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

if __name__ == "__main__":
    main()