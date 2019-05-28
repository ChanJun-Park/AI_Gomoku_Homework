# 큐를 이용해서 search space 관리

from gomoku_constant import *
from evaluate import *


class Ai5:
    def __init__(self, board):
        self.goBoard = board
        self.searchSpaceState, self.searchSpace = self.getInitialSearchSpace()
        self.evaluationSpaceState, self.evaluationSpace = self.getInitialEvaluationSpace()
        self.stoneCnt = 1
        pass

    def getInitialSearchSpace(self):
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
        length = len(self.searchSpace)
        for i in range(length):
            if self.searchSpace[i] == (x, y):
                del self.searchSpace[i]
                break

        left = x - 2 if x - 2 >= 0 else 0
        right = x + 2 if x + 2 < GO_BOARD_X_COUNT else GO_BOARD_X_COUNT
        top = y - 2 if y - 2 >= 0 else 0
        bottom = y + 2 if y + 2 < GO_BOARD_Y_COUNT else GO_BOARD_Y_COUNT
        for i in range(left, right):
            for j in range(top, bottom):
                if self.searchSpaceState[i][j]:
                    continue
                self.searchSpaceState[i][j] = True
                self.searchSpace.append((i, j))
        pass

    def getInitialEvaluationSpace(self):
        board = []
        evaluationSpace = []
        for i in range(GO_BOARD_X_COUNT):
            board.append([EMPTY] * GO_BOARD_Y_COUNT)
        for i in range(int(GO_BOARD_X_COUNT / 2) - 1, int(GO_BOARD_X_COUNT / 2) + 2):
            for j in range(int(GO_BOARD_Y_COUNT / 2) - 1, int(GO_BOARD_Y_COUNT / 2) + 2):
                board[i][j] = True
                evaluationSpace.append((i, j))
        return board, evaluationSpace

    def resetEvaluationSpace(self, x, y):
        left = x - 1 if x - 1 >= 0 else 0
        right = x + 1 if x + 1 < GO_BOARD_X_COUNT else GO_BOARD_X_COUNT
        top = y - 1 if y - 1 >= 0 else 0
        bottom = y + 1 if y + 1 < GO_BOARD_Y_COUNT else GO_BOARD_Y_COUNT
        for i in range(left, right):
            for j in range(top, bottom):
                if self.evaluationSpaceState[i][j]:
                    continue
                self.evaluationSpaceState[i][j] = True
                self.evaluationSpace.append((i, j))
        pass

    def checkHorizontal(self, x, y, length, pattern, pattern_score):
        ret = 0
        if x < GO_BOARD_X_COUNT - length:
            for z in range(len(pattern)):
                check = True
                for k in range(length):
                    if self.goBoard[x + k][y] != pattern[z][k]:
                        check = False
                        break
                if check:
                    ret += pattern_score[z]
        return ret

    def checkVertical(self, x, y, length, pattern, pattern_score):
        ret = 0
        if y < GO_BOARD_Y_COUNT - length:
            for z in range(len(pattern)):
                check = True
                for k in range(length):
                    if self.goBoard[x][y + k] != pattern[z][k]:
                        check = False
                        break
                if check:
                    ret += pattern_score[z]
        return ret

    def checkMainDiag(self, x, y, length, pattern, pattern_score):
        ret = 0
        if x < GO_BOARD_X_COUNT - length and y < GO_BOARD_Y_COUNT - length:
            for z in range(len(pattern)):
                check = True
                for k in range(length):
                    if self.goBoard[x + k][y + k] != pattern[z][k]:
                        check = False
                        break
                if check:
                    ret += pattern_score[z]
        return ret

    def checkSubDiag(self, x, y, length, pattern, pattern_score):
        ret = 0
        if x >= length and y < GO_BOARD_Y_COUNT - length:
            for z in range(len(pattern)):
                check = True
                for k in range(length):
                    if self.goBoard[x - k][y + k] != pattern[z][k]:
                        check = False
                        break
                if check:
                    ret += pattern_score[z]
        return ret

    def evaluate(self):
        ai_score = 0
        player_score = 0

        for k in self.evaluationSpace:
            x, y = k
            # AI 스코어 체크
            # → 체크
            ai_score += self.checkHorizontal(x, y, 7, AI_7PATTERNS, AI_7PATTERNS_SCORE)
            ai_score += self.checkHorizontal(x, y, 6, AI_6PATTERNS, AI_6PATTERNS_SCORE)
            ai_score += self.checkHorizontal(x, y, 5, AI_5PATTERNS, AI_5PATTERNS_SCORE)
            ai_score += self.checkHorizontal(x, y, 4, AI_4PATTERNS, AI_4PATTERNS_SCORE)

            # ↘ 체크
            ai_score += self.checkMainDiag(x, y, 7, AI_7PATTERNS, AI_7PATTERNS_SCORE)
            ai_score += self.checkMainDiag(x, y, 6, AI_6PATTERNS, AI_6PATTERNS_SCORE)
            ai_score += self.checkMainDiag(x, y, 5, AI_5PATTERNS, AI_5PATTERNS_SCORE)
            ai_score += self.checkMainDiag(x, y, 4, AI_4PATTERNS, AI_4PATTERNS_SCORE)

            # ↓ 체크
            ai_score += self.checkVertical(x, y, 7, AI_7PATTERNS, AI_7PATTERNS_SCORE)
            ai_score += self.checkVertical(x, y, 6, AI_6PATTERNS, AI_6PATTERNS_SCORE)
            ai_score += self.checkVertical(x, y, 5, AI_5PATTERNS, AI_5PATTERNS_SCORE)
            ai_score += self.checkVertical(x, y, 4, AI_4PATTERNS, AI_4PATTERNS_SCORE)

            # ↙ 체크
            ai_score += self.checkSubDiag(x, y, 7, AI_7PATTERNS, AI_7PATTERNS_SCORE)
            ai_score += self.checkSubDiag(x, y, 6, AI_6PATTERNS, AI_6PATTERNS_SCORE)
            ai_score += self.checkSubDiag(x, y, 5, AI_5PATTERNS, AI_5PATTERNS_SCORE)
            ai_score += self.checkSubDiag(x, y, 4, AI_4PATTERNS, AI_4PATTERNS_SCORE)

            # 플레이어 스코어 체크
            # → 체크
            player_score += self.checkHorizontal(x, y, 7, PLAYER1_7PATTERNS, PLAYER1_7PATTERNS_SCORE)
            player_score += self.checkHorizontal(x, y, 6, PLAYER1_6PATTERNS, PLAYER1_6PATTERNS_SCORE)
            player_score += self.checkHorizontal(x, y, 5, PLAYER1_5PATTERNS, PLAYER1_5PATTERNS_SCORE)
            player_score += self.checkHorizontal(x, y, 4, PLAYER1_4PATTERNS, PLAYER1_4PATTERNS_SCORE)

            # ↘ 체크
            player_score += self.checkMainDiag(x, y, 7, PLAYER1_7PATTERNS, PLAYER1_7PATTERNS_SCORE)
            player_score += self.checkMainDiag(x, y, 6, PLAYER1_6PATTERNS, PLAYER1_6PATTERNS_SCORE)
            player_score += self.checkMainDiag(x, y, 5, PLAYER1_5PATTERNS, PLAYER1_5PATTERNS_SCORE)
            player_score += self.checkMainDiag(x, y, 4, PLAYER1_4PATTERNS, PLAYER1_4PATTERNS_SCORE)

            # ↓ 체크
            player_score += self.checkVertical(x, y, 7, PLAYER1_7PATTERNS, PLAYER1_7PATTERNS_SCORE)
            player_score += self.checkVertical(x, y, 6, PLAYER1_6PATTERNS, PLAYER1_6PATTERNS_SCORE)
            player_score += self.checkVertical(x, y, 5, PLAYER1_5PATTERNS, PLAYER1_5PATTERNS_SCORE)
            player_score += self.checkVertical(x, y, 4, PLAYER1_4PATTERNS, PLAYER1_4PATTERNS_SCORE)

            # ↙ 체크
            player_score += self.checkSubDiag(x, y, 7, PLAYER1_7PATTERNS, PLAYER1_7PATTERNS_SCORE)
            player_score += self.checkSubDiag(x, y, 6, PLAYER1_6PATTERNS, PLAYER1_6PATTERNS_SCORE)
            player_score += self.checkSubDiag(x, y, 5, PLAYER1_5PATTERNS, PLAYER1_5PATTERNS_SCORE)
            player_score += self.checkSubDiag(x, y, 4, PLAYER1_4PATTERNS, PLAYER1_4PATTERNS_SCORE)

        return ai_score - player_score

    def minmaxWithAlphaBeta(self, alpha, beta, depth, player):
        if depth == 0 or self.stoneCnt == GO_BOARD_X_COUNT * GO_BOARD_Y_COUNT:
            return (self.evaluate(), None, None)
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
        #x, y = self.defence()

        #if x is None or y is None:
        #    place = self.minmaxWithAlphaBeta(-INF, INF, 2, AI)
        #    x = place[1]
        #    y = place[2]

        place = self.minmaxWithAlphaBeta(-INF, INF, 2, AI)
        x = place[1]
        y = place[2]
        self.goBoard[x][y] = AI
        self.stoneCnt += 1
        self.resetSearchSpace(x, y)
        self.resetEvaluationSpace(x, y)
        return True

    pass
