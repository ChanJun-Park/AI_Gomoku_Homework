import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10     # 아이콘 가로줄 수
BOARDHEIGHT = 7     # 아이콘 세로줄 수
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Borad needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#             R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDHEIGHT * BOARDWIDTH, \
    "Board is too big for the number of shapes/colors defined"

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()        # column들의 배열
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None       # 첫번째 상자를 클릭했을 때 (x, y)를 저장

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)
    pass

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    # 모든 가능한 색에서 가능한 모양의 목록을 모두 얻어낸다.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))

    random.shuffle(icons)
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)  # 얼마나 많은 아이콘이 필요한지 계산
    icons = icons[:numIconsUsed] * 2  # 각각의 짝을 만든다
    random.shuffle(icons)

    # 랜덤으로 아이콘이 놓여 있는 게임판의 데이터 구조를 만든다.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize, theList):
    # 리스트를 2차원 리스트로 만든다. 안쪽의 리스트는 최대로
    # groupSize개 만큼의 아이템이 있다.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx, boxy):
    # 게임판 좌표계를 픽셀 좌표계로 변환
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25) # syntatic sugar
    half =    int(BOXSIZE * 0.5)  # syntatic sugar

def getShapeAndColor(board, boxx, boxy):
    # x,y 위치의 아이콘 형태의 값은 board[x][y][0]에 있다.
    # x,y 위치의 아이콘 색깔의 값은 board[x][y][1]에 있다.
    return board[boxx][boxy][0], board[boxx][boxy][1]

def drawBoard(board, revealed):
    # 모든 상자를 상태에 맞게 그리기
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # 닫힌 상자를 그린다
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # 열린 상자, 즉 아이콘을 그린다
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)

def startGameAnimation(board):
    # 무작위로 한 번에 8개씩 상자를 열어서 보여준다.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
