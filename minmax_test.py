from gomoku_test import GO_BOARD_X_COUNT, GO_BOARD_Y_COUNT, EMPTY, PLAYER1, PLAYER2, AI , CONTINUE, DRAW


class Node:
    def __init__(self):
        self.bestvalue = 0
        self.child = list()
    pass


# s_x_y - s: state, x: →↘↓↙ y: 상태번호
# →, 오목 체크, 5개 체크
def check_s_1_1(board, x, y):
    for i in range(5):
        if board[x + i][y] != AI:
            return 0
    return 100


# →, 열린 사목 체크, 6개 체크
def check_s_1_2(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == EMPTY:
        return 70
    return 0


# →, 빈칸 하나 있는 사목, 7개 체크
def check_s_1_3(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == EMPTY:
        return 33
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == EMPTY:
        return 33
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == EMPTY \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == EMPTY:
        return 33
    return 0


# →, 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목, 7개 체크
def check_s_1_4(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == PLAYER1:
        return 32
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == PLAYER1:
        return 32
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == EMPTY \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == PLAYER1:
        return 32

    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == EMPTY:
        return 32
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == EMPTY:
        return 32
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == EMPTY \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == EMPTY:
        return 32
    return 0


# →, 양쪽에 상대편 바둑돌이 막고있고 빈칸 하나있는 사목, 7개 체크
def check_s_1_5(board, x, y):
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == PLAYER1:
        return 23
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == PLAYER1:
        return 23
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == EMPTY \
            and board[x + 5][y] == AI \
            and board[x + 6][y] == PLAYER1:
        return 23
    return 0


# →, 삼목, 5개 체크
def check_s_1_6(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == EMPTY:
        return 10
    return 0


# →, 상대편 바둑돌이 막고 있는 사목, 6개 체크
def check_s_1_7(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == PLAYER1:
        return 27
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == EMPTY:
        return 27
    return 0


# →, 빈칸 있는 삼목, 6개 체크
def check_s_1_8(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == EMPTY:
        return 7
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == EMPTY:
        return 7
    return 0


# →, 빈칸이 있고 상대편 바둑돌이 막고 있는 삼목, 6개 체크
def check_s_1_9(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == PLAYER1:
        return 3
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == PLAYER1:
        return 3

    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == EMPTY \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == EMPTY:
        return 3
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == EMPTY \
            and board[x + 4][y] == AI \
            and board[x + 5][y] == EMPTY:
        return 3
    return 0


# →, 상대편 바둑돌이 막고 있는 삼목, 5개 체크
def check_s_1_10(board, x, y):
    if board[x][y] == EMPTY \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == PLAYER1:
        return 6
    if board[x][y] == PLAYER1 \
            and board[x + 1][y] == AI \
            and board[x + 2][y] == AI \
            and board[x + 3][y] == AI \
            and board[x + 4][y] == EMPTY:
        return 6
    return 0


# →, 이목, 4개 체크
def check_s_1_11(board, x, y):
    if board[x][y] == EMPTY\
        and board[x + 1][y] == AI\
        and board[x + 2][y] == AI\
        and board[x + 3][y] == EMPTY:
        return 2
    return 0


# →, 상대편 바둑돌이 막고 있는 이목, 4개 체크
def check_s_1_12(board, x, y):
    if board[x][y] == EMPTY\
        and board[x + 1][y] == AI\
        and board[x + 2][y] == AI\
        and board[x + 3][y] == PLAYER1:
        return 1
    if board[x][y] == PLAYER1\
        and board[x + 1][y] == AI\
        and board[x + 2][y] == AI\
        and board[x + 3][y] == EMPTY:
        return 1
    return 0


def e_function(board):
    score = 0

    # → 체크
    for x in range(0, GO_BOARD_X_COUNT):
        for y in range(0, GO_BOARD_Y_COUNT):
            if x < GO_BOARD_X_COUNT - 6:
                score += check_s_1_3(board, x, y)
                score += check_s_1_4(board, x, y)
                score += check_s_1_5(board, x, y)
            elif x < GO_BOARD_X_COUNT - 5:
                score += check_s_1_2(board, x, y)
                score += check_s_1_7(board, x, y)
                score += check_s_1_8(board, x, y)
                score += check_s_1_9(board, x, y)
            elif x < GO_BOARD_X_COUNT - 4:
                score += check_s_1_1(board, x, y)
                score += check_s_1_6(board, x, y)
                score += check_s_1_10(board, x, y)
            elif x < GO_BOARD_X_COUNT - 3:
                score += check_s_1_11(board, x, y)
                score += check_s_1_12(board, x, y)