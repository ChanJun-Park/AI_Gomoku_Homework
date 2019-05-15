'''
2019.05.12
기본적인 오목 UI 만들기
0. 흑돌, 백돌 선택 버튼
1. 게임 시작 버튼
2. 게임 리셋 버튼
3. 누구의 턴인지 알려주는 텍스트
4. 게임 승패를 알려주는 텍스트
'''

import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600

BASICFONTSIZE = 20
#the hand cursor
_HAND_CURSOR = (
"     XX         ",
"    X..X        ",
"    X..X        ",
"    X..X        ",
"    X..XXXXX    ",
"    X..X..X.XX  ",
" XX X..X..X.X.X ",
"X..XX.........X ",
"X...X.........X ",
" X.....X.X.X..X ",
"  X....X.X.X..X ",
"  X....X.X.X.X  ",
"   X...X.X.X.X  ",
"    X.......X   ",
"     X....X.X   ",
"     XXXXX XX   ")
_HCURS, _HMASK = pygame.cursors.compile(_HAND_CURSOR, ".", "X")
HAND_CURSOR = ((16, 16), (5, 1), _HCURS, _HMASK)

#색깔       R,   G,   B
BLACK  = (  0,   0,   0)
GRAY   = (200, 200, 200)
WHITE  = (255, 255, 255)
YELLOW = (255, 211,  21)

BGCOLOR = WHITE
TEXTCOLOR = BLACK

# 바둑판 이미지
GO_BOARD_IMG = pygame.image.load('go.png')
GO_BOARD_WIDTH = 580
GO_BOARD_HEIGHT = 580
GO_BOARD_IMG_X = int(WINDOWWIDTH / 3) - int(GO_BOARD_WIDTH / 2)
GO_BOARD_IMG_Y = int(WINDOWHEIGHT / 2) - int(GO_BOARD_HEIGHT / 2)
GO_BOARD_MARGIN = 20
GO_BOARD_CELL_GAP = 30
GO_BOARD_X_COUNT = 19
GO_BOARD_Y_COUNT = 19
STONE_RADIUS = int(GO_BOARD_CELL_GAP / 2)

# 바둑판에서 (0,0)의 픽셀 좌표
TOP_LEFT_X = GO_BOARD_IMG_X + GO_BOARD_MARGIN
TOP_LEFT_Y = GO_BOARD_IMG_Y + GO_BOARD_MARGIN

# 바둑판 상태
EMPTY   = 0
PLAYER1 = 1
PLAYER2 = 2

def main():
    global DISPLAYSURF, BASICFONT,\
    STONE_SELECT_SURF, STONE_SELECT_RECT, \
    NEW_SURF, NEW_RECT, \
    TURN_SURF, TURN_RECT, \
    P1_COLOR, P2_COLOR

    global turn

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Go Board Test')

    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    P1_COLOR, P2_COLOR = selectStoneColor()
    if P1_COLOR == BLACK:
        turn = PLAYER1
    else:
        turn = PLAYER2

    NEW_SURF, NEW_RECT = makeText('New', BLACK, WHITE, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)

    # 바둑돌의 상태를 저장하는 2차원 리스트
    goBoard = getInitialBoard()

    mousex = 0
    mousey = 0

    # 바둑판 위의 좌표
    boardx = 0
    boardy = 0

    drawBoard(goBoard)
    # 메인 게임 루프
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(goBoard)

        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                mouseClicked = True

        boardx, boardy = getBoardPosAtPixel(mousex, mousey)
        if boardx != None and boardy != None:
            if not goBoard[boardx][boardy]:
                drawPseudoStone(goBoard, boardx, boardy)
            if not goBoard[boardx][boardy] and mouseClicked:
                goBoard[boardx][boardy] = turn
                turn = (PLAYER1 if turn == PLAYER2 else PLAYER2)
                pass
            pass

        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()
    pass

def makeText(text, color, bgcolor, x, y):
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.center = (x, y)
    return (textSurf, textRect)

def getInitialBoard():
    board = []
    for i in range(GO_BOARD_X_COUNT):
        board.append([EMPTY] * GO_BOARD_Y_COUNT)
    return board

def getPixelPosOfBoard(boardx, boardy):
    left = GO_BOARD_IMG_X + GO_BOARD_MARGIN + boardx * GO_BOARD_CELL_GAP
    top = GO_BOARD_IMG_Y + GO_BOARD_MARGIN + boardy * GO_BOARD_CELL_GAP
    return (left, top)

def getBoardPosAtPixel(x, y):
    boardx = int((x - TOP_LEFT_X + STONE_RADIUS) / GO_BOARD_CELL_GAP)
    boardy = int((y - TOP_LEFT_Y + STONE_RADIUS) / GO_BOARD_CELL_GAP)
    if boardx >= 0 and boardx < 19 and boardy >=0 and boardy < 19:
        return (boardx, boardy)
    return (None, None)

def drawBoard(board):
    DISPLAYSURF.blit(GO_BOARD_IMG, (GO_BOARD_IMG_X, GO_BOARD_IMG_Y))
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    for x in range(GO_BOARD_X_COUNT):
        for y in range(GO_BOARD_Y_COUNT):
            left, top = getPixelPosOfBoard(x, y)
            if board[x][y] == PLAYER1:
                pygame.draw.circle(DISPLAYSURF, BLACK, (left, top), STONE_RADIUS, 0)
                pass
            elif board[x][y] == PLAYER2:
                pygame.draw.circle(DISPLAYSURF, WHITE, (left, top), STONE_RADIUS, 0)
                pass
    pass

def drawPseudoStone(board, x, y):
    left, top = getPixelPosOfBoard(x, y)
    if board[x][y] == EMPTY:
        if turn == PLAYER1:
            pygame.draw.circle(DISPLAYSURF, P1_COLOR, (left, top), STONE_RADIUS, 2)
        else: # turn == PLAYER2
            pygame.draw.circle(DISPLAYSURF, P2_COLOR, (left, top), STONE_RADIUS, 2)
    pass

# player1, player2 의 돌의 색깔을 선택하여 반환해준다.
def selectStoneColor():
    pygame.draw.rect(DISPLAYSURF, GRAY, (WINDOWWIDTH/2 - 200, WINDOWHEIGHT/2 - 200, 400, 400));
    OPTION_BLACK_SURF, OPTION_BLACK_RECT = makeText('Black', BLACK, GRAY, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 50);
    OPTION_WHITE_SURF, OPTION_WHITE_RECT = makeText('White', BLACK, GRAY, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 50);
    DISPLAYSURF.blit(OPTION_BLACK_SURF, OPTION_BLACK_RECT);
    DISPLAYSURF.blit(OPTION_WHITE_SURF, OPTION_WHITE_RECT);
    pygame.display.update()

    mousex = 0
    mousey = 0

    mouseClicked = False

    # 마우스 입력을 받을 때까지 대기
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouseClicked = True;
                mousex, mousey = event.pos


        if OPTION_BLACK_RECT.collidepoint(mousex, mousey):
            pygame.mouse.set_cursor(*HAND_CURSOR)
            if mouseClicked:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                return (BLACK, WHITE)
        elif OPTION_WHITE_RECT.collidepoint(mousex, mousey):
            pygame.mouse.set_cursor(*HAND_CURSOR)
            if mouseClicked:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                return (WHITE, BLACK)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pass

if __name__ == "__main__":
    main()
