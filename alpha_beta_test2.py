# 큐를 이용해서 search space 관리

from gomoku_constant import *
from evaluate import *

class Ai2:
    def __init__(self, board):
        self.goBoard = board
        self.searchSpaceState, self.searchSpace = self.getInitialSearchSpaceState()
        self.stoneCnt = 1
        pass

    def getInitialSearchSpaceState(self):
        board = []
        searchSpace = []
        for i in range(GO_BOARD_X_COUNT):
            board.append([EMPTY] * GO_BOARD_Y_COUNT)
        for i in range(int(GO_BOARD_X_COUNT / 2) - 2, int(GO_BOARD_X_COUNT / 2) + 3):
            for j in range(int(GO_BOARD_Y_COUNT / 2) - 2, int(GO_BOARD_Y_COUNT / 2) + 3):
                board[i][j] = True
                if i == j:
                    continue
                searchSpace.append((i, j))
        return board

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

    def minmaxWithAlphaBeta(self, alpha, beta, depth, player):
        if depth == 0 or self.stoneCnt == GO_BOARD_X_COUNT * GO_BOARD_Y_COUNT:
            return (e_function(self.goBoard), None, None)
        if player == AI:
            maxValue = -INF
            x = 0
            y = 0
            checkBetaCut = False
            for i in range(self.searchSpace[0], self.searchSpace[1] + 1):
                for j in range(self.searchSpace[2], self.searchSpace[3] + 1):
                    if self.goBoard[i][j] == EMPTY:
                        self.goBoard[i][j] = AI
                        ret = self.minmaxWithAlphaBeta(alpha, beta, depth - 1, PLAYER1)
                        if ret[0] > maxValue:
                            maxValue = ret[0]
                            x = i
                            y = j
                            alpha = max(alpha, maxValue)
                        self.goBoard[i][j] = EMPTY
                        if beta <= alpha:
                            checkBetaCut = True
                            break
                if checkBetaCut:
                    break
            if depth == 1:
                return (maxValue, x, y)
            else:
                return (maxValue, None, None)
            pass
        else: # player == PLAYER1
            minValue = INF
            x = 0
            y = 0
            checkAlphaCut = False
            for i in range(self.searchSpace[0], self.searchSpace[1] + 1):
                for j in range(self.searchSpace[2], self.searchSpace[3] + 1):
                    if self.goBoard[i][j] == EMPTY:
                        self.goBoard[i][j] = PLAYER1
                        ret = self.minmaxWithAlphaBeta(alpha, beta, depth - 1, AI)
                        if ret[0] < minValue:
                            minValue = ret[0]
                            x = i
                            y = j
                            beta = min(beta, minValue)
                        self.goBoard[i][j] = EMPTY
                        if beta <= alpha:
                            checkAlphaCut = True
                            break
                    if checkAlphaCut:
                        break
            if depth == 1:
                return (minValue, x, y)
            else:
                return (minValue, None, None)
            pass

    def defence(self):
        for x in range(GO_BOARD_X_COUNT):
            for y in range(GO_BOARD_Y_COUNT):
                # → 체크
                if x < GO_BOARD_X_COUNT - 7:
                    for z in range(len(DEFENCE_7PATTERNS)):
                        check = True
                        for k in range(7):
                            if self.goBoard[x + k][y] != DEFENCE_7PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_7PATTERNS[z].index(EMPTY)
                            return (x + i, y)
                if x < GO_BOARD_X_COUNT - 6:
                    for z in range(len(DEFENCE_6PATTERNS)):
                        check = True
                        for k in range(6):
                            if self.goBoard[x + k][y] != DEFENCE_6PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_6PATTERNS[z].index(EMPTY)
                            return (x + i, y)
                if x < GO_BOARD_X_COUNT - 5:
                    for z in range(len(DEFENCE_5PATTERNS)):
                        check = True
                        for k in range(5):
                            if self.goBoard[x + k][y] != DEFENCE_5PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_5PATTERNS[z].index(EMPTY)
                            return (x + i, y)

                # ↘ 체크
                if x < GO_BOARD_X_COUNT - 7 and y < GO_BOARD_Y_COUNT - 7:
                    for z in range(len(DEFENCE_7PATTERNS)):
                        check = True
                        for k in range(7):
                            if self.goBoard[x + k][y + k] != DEFENCE_7PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_7PATTERNS[z].index(EMPTY)
                            return (x + i, y + i)
                if x < GO_BOARD_X_COUNT - 6 and y < GO_BOARD_Y_COUNT - 6:
                    for z in range(len(DEFENCE_6PATTERNS)):
                        check = True
                        for k in range(6):
                            if self.goBoard[x + k][y + k] != DEFENCE_6PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_6PATTERNS[z].index(EMPTY)
                            return (x + i, y + i)
                if x < GO_BOARD_X_COUNT - 5 and y < GO_BOARD_Y_COUNT - 5:
                    for z in range(len(DEFENCE_5PATTERNS)):
                        check = True
                        for k in range(5):
                            if self.goBoard[x + k][y + k] != DEFENCE_5PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_5PATTERNS[z].index(EMPTY)
                            return (x + i, y + i)

                # ↓ 체크
                if y < GO_BOARD_Y_COUNT - 7:
                    for z in range(len(DEFENCE_7PATTERNS)):
                        check = True
                        for k in range(7):
                            if self.goBoard[x][y + k] != DEFENCE_7PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_7PATTERNS[z].index(EMPTY)
                            return (x, y + i)
                if y < GO_BOARD_Y_COUNT - 6:
                    for z in range(len(DEFENCE_6PATTERNS)):
                        check = True
                        for k in range(6):
                            if self.goBoard[x][y + k] != DEFENCE_6PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_6PATTERNS[z].index(EMPTY)
                            return (x, y + i)
                if y < GO_BOARD_Y_COUNT - 5:
                    for z in range(len(DEFENCE_5PATTERNS)):
                        check = True
                        for k in range(5):
                            if self.goBoard[x][y + k] != DEFENCE_5PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_5PATTERNS[z].index(EMPTY)
                            return (x, y + i)

                # ↙ 체크
                if x >= 7 and y < GO_BOARD_Y_COUNT - 7:
                    for z in range(len(DEFENCE_7PATTERNS)):
                        check = True
                        for k in range(7):
                            if self.goBoard[x - k][y + k] != DEFENCE_7PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_7PATTERNS[z].index(EMPTY)
                            return (x - i, y + i)
                if x >= 6 and y < GO_BOARD_Y_COUNT - 6:
                    for z in range(len(DEFENCE_6PATTERNS)):
                        check = True
                        for k in range(6):
                            if self.goBoard[x - k][y + k] != DEFENCE_6PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_6PATTERNS[z].index(EMPTY)
                            return (x - i, y + i)
                if x >= 5 and y < GO_BOARD_Y_COUNT - 5:
                    for z in range(len(DEFENCE_5PATTERNS)):
                        check = True
                        for k in range(5):
                            if self.goBoard[x - k][y + k] != DEFENCE_5PATTERNS[z][k]:
                                check = False
                                break
                        if check:
                            i = DEFENCE_5PATTERNS[z].index(EMPTY)
                            return (x - i, y + i)
        return (None, None)

    def placement(self):
        x, y = self.defence()

        if x is None or y is None:
            place = self.minmaxWithAlphaBeta(-INF, INF, 1, AI)
            x = place[1]
            y = place[2]

        self.goBoard[x][y] = AI
        self.stoneCnt += 1
        self.resetSearchSpace(x, y)
        return True

    pass
