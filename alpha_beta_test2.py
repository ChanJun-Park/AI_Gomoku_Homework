# 큐를 이용해서 search space 관리

from gomoku_constant import *
from evaluate import *


class Ai3:
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
        return board, searchSpace

    def resetSearchSpace(self, x, y):
        self.searchSpaceState[x][y] = True
        for i in range(len(self.searchSpace)):
            if self.searchSpace[i] == (x, y):
                del self.searchSpace[i]
                break

        left = x - 2 if x - 2 >= 0 else 0
        right = x + 2 if x + 2 < GO_BOARD_X_COUNT else GO_BOARD_X_COUNT - 1
        top = y - 2 if y - 2 >= 0 else 0
        bottom = y + 2 if y + 2 < GO_BOARD_Y_COUNT else GO_BOARD_Y_COUNT - 1
        for i in range(left, right):
            for j in range(top, bottom):
                if self.searchSpaceState[i][j]:
                    continue
                self.searchSpaceState[i][j] = True
                self.searchSpace.append((i, j))
        pass

    def minmaxWithAlphaBeta(self, alpha, beta, depth, player):
        if depth == 0 or self.stoneCnt == GO_BOARD_X_COUNT * GO_BOARD_Y_COUNT:
            return (e_function(self.goBoard), None, None)
        if player == AI:
            maxValue = -INF
            x = 0
            y = 0
            for k in self.searchSpace:
                i, j = k
                if self.goBoard[i][j] == EMPTY:
                    self.goBoard[i][j] = AI
                    ret = self.minmaxWithAlphaBeta(alpha, beta, depth - 1, PLAYER1)
                    if ret[0] > maxValue:
                        maxValue = ret[0]
                        x = i
                        y = j
                        alpha = max(alpha, maxValue)
                    self.goBoard[i][j] = EMPTY
                    if beta <= alpha:  # Beta Cut
                        break
            if depth == 2:
                return (maxValue, x, y)
            else:
                return (maxValue, None, None)
            pass
        else: # player == PLAYER1
            minValue = INF
            x = 0
            y = 0
            for k in self.searchSpace:
                i, j = k
                if self.goBoard[i][j] == EMPTY:
                    self.goBoard[i][j] = PLAYER1
                    ret = self.minmaxWithAlphaBeta(alpha, beta, depth - 1, AI)
                    if ret[0] < minValue:
                        minValue = ret[0]
                        x = i
                        y = j
                        beta = min(beta, minValue)
                    self.goBoard[i][j] = EMPTY
                    if beta <= alpha:  # Alpha Cut
                        break
            if depth == 2:
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
            place = self.minmaxWithAlphaBeta(-INF, INF, 2, AI)
            x = place[1]
            y = place[2]

        self.goBoard[x][y] = AI
        self.stoneCnt += 1
        self.resetSearchSpace(x, y)
        return True

    pass
