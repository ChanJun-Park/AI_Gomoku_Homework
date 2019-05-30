# 큐를 이용해서 search space 관리
# TODO 오목판 배열에서 패턴을 체크하는 중복을 제거하자
from gomoku_constant import *
from evaluate import *
import copy
import random

class Ai6:
    def __init__(self, board):
        self.goBoard = board
        self.searchSpaceState, self.searchSpace = self.getInitialSearchSpace()
        self.searchCandidate = copy.deepcopy(self.searchSpace)
        self.evaluationSpaceState, self.evaluationSpace = self.getInitialEvaluationSpace()
        self.stoneCnt = 1
        self.searchSize = 30
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
        length = len(self.searchCandidate)
        for i in range(length):
            if self.searchCandidate[i] == (x, y):
                del self.searchCandidate[i]
                break

        count = len(self.searchCandidate)
        if self.searchSize <= count:
            count = self.searchSize
        self.searchSpace = random.sample(self.searchCandidate, count)

        left = x - 2 if x - 2 >= 0 else 0
        right = x + 2 if x + 2 < GO_BOARD_X_COUNT else GO_BOARD_X_COUNT
        top = y - 2 if y - 2 >= 0 else 0
        bottom = y + 2 if y + 2 < GO_BOARD_Y_COUNT else GO_BOARD_Y_COUNT
        for i in range(left, right):
            for j in range(top, bottom):
                if self.searchSpaceState[i][j]:
                    continue
                self.searchSpaceState[i][j] = True
                self.searchCandidate.append((i, j))
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

    def endGameCheckHorizontal(self, x, y, patternList, order):
        for p in patternList:
            if x < GO_BOARD_X_COUNT - len(p):
                check = True
                for k in range(len(p)):
                    if self.goBoard[x + k][y] != p[k]:
                        check = False
                        break
                if check:
                    loc = p.index(EMPTY)
                    if order == 2:
                        loc += p[loc+1:].index(EMPTY)
                        loc += 1
                    return x + loc, y
        return None, None

    def endGameCheckVertical(self, x, y, patternList, order):
        for p in patternList:
            if y < GO_BOARD_X_COUNT - len(p):
                check = True
                for k in range(len(p)):
                    if self.goBoard[x][y + k] != p[k]:
                        check = False
                        break
                if check:
                    loc = p.index(EMPTY)
                    if order == 2:
                        loc += p[loc+1:].index(EMPTY)
                        loc += 1
                    return x, y + loc
        return None, None

    def endGameCheckMainDiag(self, x, y, patternList, order):
        for p in patternList:
            if x < GO_BOARD_X_COUNT - len(p) and y < GO_BOARD_X_COUNT - len(p):
                check = True
                for k in range(len(p)):
                    if self.goBoard[x + k][y + k] != p[k]:
                        check = False
                        break
                if check:
                    loc = p.index(EMPTY)
                    if order == 2:
                        loc += p[loc+1:].index(EMPTY)
                        loc += 1
                    return x + loc, y + loc
        return None, None

    def endGameCheckSubDiag(self, x, y, patternList, order):
        for p in patternList:
            if x >= len(p) and y < GO_BOARD_X_COUNT - len(p):
                check = True
                for k in range(len(p)):
                    if self.goBoard[x - k][y + k] != p[k]:
                        check = False
                        break
                if check:
                    loc = p.index(EMPTY)
                    if order == 2:
                        loc += p[loc+1:].index(EMPTY)
                        loc += 1
                    return x - loc, y + loc
        return None, None

    def endGameCheck(self):
        retx, rety = (None, None)

        for t in self.evaluationSpace:
            x, y = t
            retx, rety = self.endGameCheckHorizontal(x, y, AI_ENDGAME_PATTERN1, 1)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckVertical(x, y, AI_ENDGAME_PATTERN1, 1)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckMainDiag(x, y, AI_ENDGAME_PATTERN1, 1)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckSubDiag(x, y, AI_ENDGAME_PATTERN1, 1)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckHorizontal(x, y, AI_ENDGAME_PATTERN2, 2)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckVertical(x, y, AI_ENDGAME_PATTERN2, 2)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckMainDiag(x, y, AI_ENDGAME_PATTERN2, 2)
            if retx != None and rety != None:
                break
            retx, rety = self.endGameCheckSubDiag(x, y, AI_ENDGAME_PATTERN2, 2)
            if retx != None and rety != None:
                break
        return retx, rety

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

    def placement(self):
        print("Search space size : \n", len(self.searchSpace))
        print("Evaluation space size : \n", len(self.evaluationSpace))

        x, y = self.endGameCheck()
        if x is None and y is None:
            place = self.minmaxWithAlphaBeta(-INF, INF, 2, AI)
            x = place[1]
            y = place[2]

        print("place stone at : ", x, y)
        self.goBoard[x][y] = AI
        self.stoneCnt += 1
        self.resetSearchSpace(x, y)
        self.resetEvaluationSpace(x, y)
        return True

    pass
