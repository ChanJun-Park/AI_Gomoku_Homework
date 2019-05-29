from gomoku_constant import *
from evaluate import *


class Ai1:
    def __init__(self, board):
        self.goBoard = board
        self.searchSpace = [int(GO_BOARD_X_COUNT / 2) - 2, int(GO_BOARD_X_COUNT / 2) + 2,
                            int(GO_BOARD_Y_COUNT / 2) - 2, int(GO_BOARD_Y_COUNT / 2) + 2]
        self.stoneCnt = 1
        pass

    def resetSearchSpace(self, x, y):
        if self.searchSpace[0] > x:
            self.searchSpace[0] = (x - 2 if x > 1 else x)
        if self.searchSpace[1] < x:
            self.searchSpace[1] = (x + 2 if x < GO_BOARD_X_COUNT - 2 else x)
        if self.searchSpace[2] > y:
            self.searchSpace[2] = (y - 2 if y > 1 else y)
        if self.searchSpace[3] < y:
            self.searchSpace[3] = (y + 2 if y < GO_BOARD_Y_COUNT - 2 else y)
        pass

    def minmax(self, depth, player):
        if depth == 0 or self.stoneCnt == GO_BOARD_X_COUNT * GO_BOARD_Y_COUNT:
            return (e_function(self.goBoard), None, None)
        if player == AI:
            maxValue = -INF
            x = 0
            y = 0
            for i in range(self.searchSpace[0], self.searchSpace[1] + 1):
                for j in range(self.searchSpace[2], self.searchSpace[3] + 1):
                    if self.goBoard[i][j] == EMPTY:
                        self.goBoard[i][j] = AI
                        ret = self.minmax(depth - 1, PLAYER1)
                        if ret[0] > maxValue:
                            maxValue = ret[0]
                            x = i
                            y = j
                        self.goBoard[i][j] = EMPTY

            if depth == 1:
                return (maxValue, x, y)
            else:
                return (maxValue, None, None)
            pass
        else: # player == PLAYER1
            minValue = INF
            x = 0
            y = 0
            for i in range(self.searchSpace[0], self.searchSpace[1] + 1):
                for j in range(self.searchSpace[2], self.searchSpace[3] + 1):
                    if self.goBoard[i][j] == EMPTY:
                        self.goBoard[i][j] = PLAYER1
                        ret = self.minmax(depth - 1, AI)
                        if ret[0] < minValue:
                            minValue = ret[0]
                            x = i
                            y = j
                        self.goBoard[i][j] = EMPTY
            if depth == 1:
                return (minValue, x, y)
            else:
                return (minValue, None, None)
            pass


    def placement(self):
        place = self.minmax(1, AI)
        x = place[1]
        y = place[2]

        self.goBoard[x][y] = AI
        self.stoneCnt += 1
        self.resetSearchSpace(x, y)
        return True

    pass
