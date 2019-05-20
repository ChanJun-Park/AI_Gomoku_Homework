##그냥 실행시키면 됩니다! 실행 후 반드시 Depth에 숫자를 넣고 enter를 누른 후 클릭하세요. 2 이상은 느릴 수 있습니다.
import simplegui
import random

WIDTH = 520
HEIGHT = 520
scale = 40
board = [[0 for x in range(0, 14)] for y in range(0, 14)]
turn = 1


class Node:
    def __init__(self):
        self.bestvalue = 0
        self.child = list()


### Minmax 알고리즘
def minimax(node, depth, player):
    if depth == 0 or node.child == None:
        return Heuristic(node.currentboard)
    if player == 2:
        for a in range(0, 14):
            for b in range(0, 14):
                if node.currentboard[a][b] == 0:
                    childnode = Node()
                    childnode.currentboard = list()
                    for i in range(0, 14):
                        temp = list()
                        for j in range(0, 14):
                            if node.currentboard[i][j] == 0:
                                temp.append(0)
                            elif node.currentboard[i][j] == 1:
                                temp.append(1)
                            elif node.currentboard[i][j] == 2:
                                temp.append(2)
                        childnode.currentboard.append(temp)
                    # childnode.currentboard = copy.deepcopy(node.currentboard)
                    childnode.currentboard[a][b] = player
                    childnode.xmove = a
                    childnode.ymove = b
                    node.child.append(childnode)
                else:
                    pass
        bestvalue = float("-inf")
        for i in node.child:
            i.bestvalue = minimax(i, depth - 1, 1)
            bestvalue = max(bestvalue, i.bestvalue)
        return bestvalue
    elif player == 1:
        for a in range(0, 14):
            for b in range(0, 14):
                if node.currentboard[a][b] == 0:
                    childnode = Node()
                    childnode.currentboard = list()
                    for i in range(0, 14):
                        temp = list()
                        for j in range(0, 14):
                            if node.currentboard[i][j] == 0:
                                temp.append(0)
                            elif node.currentboard[i][j] == 1:
                                temp.append(1)
                            elif node.currentboard[i][j] == 2:
                                temp.append(2)
                        childnode.currentboard.append(temp)
                    # childnode.currentboard = copy.deepcopy(node.currentboard)
                    childnode.currentboard[a][b] = player
                    childnode.xmove = a
                    childnode.ymove = b
                    node.child.append(childnode)
                else:
                    pass
        bestvalue = float("inf")
        for i in node.child:
            i.bestvalue = minimax(i, depth - 1, 2)
            bestvalue = min(bestvalue, i.bestvalue)
        return bestvalue


###Heuristic 함수
###Heuristic 함수
def Heuristic(board):
    score = 0
    for x in range(0, 11):
        for y in range(0, 11):
            ### 맨 위쪽 가장자리
            if x == 0:
                ##세로
                if board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1 and board[x + 3][y] == 1:
                    if board[x + 4][y] == 0:
                        score = score - 1000
                    elif board[x + 4][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 0 and board[x + 2][y] == 1 and board[x + 3][y] == 1:
                    if board[x + 4][y] == 0:
                        score = score - 1000
                    elif board[x + 4][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 0 and board[x + 3][y] == 1:
                    if board[x + 4][y] == 0:
                        score = score - 1000
                    elif board[x + 4][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1:
                    score = score - 1000

                ##가로
                if board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and board[x][y + 3] == 1:
                    if board[x][y + 4] == 0:
                        score = score - 1000
                    elif board[x][y + 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 0 and board[x][y + 2] == 1 and board[x][y + 3] == 1:
                    if board[x][y + 4] == 0:
                        score = score - 1000
                    elif board[x][y + 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 0 and board[x][y + 3] == 1:
                    if board[x][y + 4] == 0:
                        score = score - 1000
                    elif board[x][y + 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1:
                    score = score - 1000

                ###대각선
                if board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and board[x + 3][
                    y + 3] == 1:
                    if board[x + 4][y + 4] == 0:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 1 and board[x + 3][
                    y + 3] == 1:
                    if board[x + 4][y + 4] == 0:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 1:
                    if board[x + 4][y + 4] == 0:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1:
                    score = score - 1000

                ### AI말의 유리한 경우
                ##세로
                if board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and board[x + 3][y] == 2:
                    if board[x + 4][y] == 0:
                        score = score + 1000
                    elif board[x + 4][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 0 and board[x + 2][y] == 2 and board[x + 3][y] == 2:
                    if board[x + 4][y] == 0:
                        score = score + 1000
                    elif board[x + 4][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 0 and board[x + 3][y] == 2:
                    if board[x + 4][y] == 0:
                        score = score + 1000
                    elif board[x + 4][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2:
                    score = score + 1000

                ##가로
                if board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and board[x][y + 3] == 2:

                    if board[x][y + 4] == 0:
                        score = score + 1000
                    elif board[x][y + 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 0 and board[x][y + 2] == 2 and board[x][y + 3] == 2:
                    if board[x][y + 4] == 0:
                        score = score + 1000
                    elif board[x][y + 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 0 and board[x][y + 3] == 2:
                    if board[x][y + 4] == 0:
                        score = score + 1000
                    elif board[x][y + 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2:
                    score = score + 100

                ###대각선
                if board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2:
                    if board[x + 4][y + 4] == 0:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2:
                    if board[x + 4][y + 4] == 0:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 2:
                    if board[x + 4][y + 4] == 0:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2:
                    score = score + 1000

            ###맨 아래쪽 가장자리
            elif x == 10:
                if board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1 and board[x + 3][y] == 1:
                    if board[x - 1][y] == 0:
                        score = score - 1000
                    elif board[x - 1][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 0 and board[x + 2][y] == 1 and board[x + 3][y] == 1:
                    if board[x - 1][y] == 0:
                        score = score - 1000
                    elif board[x - 1][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 0 and board[x + 3][y] == 1:
                    if board[x - 1][y] == 0:
                        score = score - 1000
                    elif board[x - 1][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1:
                    score = score - 1000

                ##가로
                if board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and board[x][y + 3] == 1:

                    if board[x][y - 1] == 0:
                        score = score - 1000
                    elif board[x][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 0 and board[x][y + 2] == 1 and board[x][y + 3] == 1:
                    if board[x][y - 1] == 0:
                        score = score - 1000
                    elif board[x][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 0 and board[x][y + 3] == 1:
                    if board[x][y - 1] == 0:
                        score = score - 1000
                    elif board[x][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1:
                    score = score - 1000

                ###대각선
                if board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and board[x + 3][
                    y + 3] == 1:
                    if board[x - 1][y - 1] == 0:
                        score = score - 1000
                    elif board[x - 1][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 1 and board[x + 3][
                    y + 3] == 1:
                    if board[x - 1][y - 1] == 0:
                        score = score - 1000
                    elif board[x - 1][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 1:
                    if board[x - 1][y - 1] == 0:
                        score = score - 1000
                    elif board[x - 1][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1:
                    score = score - 1000

                ### AI말이 유리한 경우
                if board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and board[x + 3][y] == 2:
                    if board[x - 1][y] == 0:
                        score = score + 1000
                    elif board[x - 1][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 0 and board[x + 2][y] == 2 and board[x + 3][y] == 2:
                    if board[x - 1][y] == 0:
                        score = score + 1000
                    elif board[x - 1][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 0 and board[x + 3][y] == 2:
                    if board[x - 1][y] == 0:
                        score = score + 1000
                    elif board[x - 1][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2:
                    score = score + 1000

                ##가로
                if board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and board[x][y + 3] == 2:

                    if board[x][y - 1] == 0:
                        score = score + 1000
                    elif board[x][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 0 and board[x][y + 2] == 2 and board[x][y + 3] == 2:
                    if board[x][y - 1] == 0:
                        score = score + 1000
                    elif board[x][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 0 and board[x][y + 3] == 2:
                    if board[x][y - 1] == 0:
                        score = score + 1000
                    elif board[x][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2:
                    score = score + 1000

                ###대각선
                if board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2:
                    if board[x - 1][y - 1] == 0:
                        score = score + 1000
                    elif board[x - 1][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2:
                    if board[x - 1][y - 1] == 0:
                        score = score + 1000
                    elif board[x - 1][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 2:
                    if board[x - 1][y - 1] == 0:
                        score = score + 1000
                    elif board[x - 1][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2:
                    score = score + 1000

            #### 나머지 경우
            else:
                if board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1 and board[x + 3][y] == 1:
                    if board[x + 4][y] == 1 or board[x - 1][y] == 1:
                        score = score - 1000
                    elif board[x + 4][y] == 0 and board[x - 1][y] == 0:
                        score = score - 1000
                    elif board[x + 4][y] == 2 and board[x - 1][y] == 2:
                        score = score + 1500
                    elif board[x + 4][y] == 2 or board[x - 1][y] == 2:
                        score = score + 500
                elif board[x][y] == 1 and board[x + 1][y] == 0 and board[x + 2][y] == 1 and board[x + 3][y] == 1:
                    if board[x + 4][y] == 0 and board[x - 1][y] == 0:
                        score = score - 1000
                    elif board[x + 4][y] == 2 and board[x - 1][y] == 2:
                        score = score + 1000
                    elif board[x + 4][y] == 2 and board[x - 1][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 0 and board[x + 3][y] == 1:
                    if board[x + 4][y] == 0 and board[x - 1][y] == 0:
                        score = score - 1000
                    elif board[x + 4][y] == 2 and board[x - 1][y] == 2:
                        score = score + 1000
                    elif board[x + 4][y] == 2 or board[x - 1][y] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1:
                    if board[x + 3][y] == 2 or board[x - 1][y] == 2:
                        score = score + 1000
                    else:
                        score = score - 1000

                ##가로
                if board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and board[x][y + 3] == 1:
                    if board[x][y + 4] == 1 or board[x][y - 1] == 1:
                        score = score - 1000
                    elif board[x][y + 4] == 0 and board[x][y - 1] == 0:
                        score = score - 1000
                    elif board[x][y + 4] == 2 and board[x][y - 1] == 2:
                        score = score + 1500
                    elif board[x][y + 4] == 2 or board[x][y - 1] == 2:
                        score = score + 500
                elif board[x][y] == 1 and board[x][y + 1] == 0 and board[x][y + 2] == 1 and board[x][y + 3] == 1:
                    if board[x][y + 4] == 0 and board[x][y - 1] == 0:
                        score = score - 1000
                    elif board[x][y + 4] == 2 and board[x][y - 1] == 2:
                        score = score + 1000
                    elif board[x][y + 4] == 2 or board[x][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 0 and board[x][y + 3] == 1:
                    if board[x][y + 4] == 0 and board[x][y - 1] == 0:
                        score = score - 1000
                    elif board[x][y + 4] == 2 and board[x][y - 1] == 2:
                        score = score + 1000
                    elif board[x][y + 4] == 2 or board[x][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1:
                    if board[x][y + 3] == 2 or board[x][y - 1] == 2:
                        score = score + 1000
                    else:
                        score = score - 1000

                ###대각선
                if board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and board[x + 3][
                    y + 3] == 1:
                    if board[x + 4][y + 4] == 1 or board[x - 1][y - 1] == 1:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 0 and board[x - 1][y - 1] == 0:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2 and board[x - 1][y - 1] == 2:
                        score = score + 1500
                    elif board[x + 4][y + 4] == 2 or board[x - 1][y - 1] == 2:
                        score = score + 500
                elif board[x][y] == 1 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 1 and board[x + 3][
                    y + 3] == 1:
                    if board[x + 4][y + 4] == 0 and board[x - 1][y - 1] == 0:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2 and board[x - 1][y - 1] == 2:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 2 or board[x - 1][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 1:
                    if board[x + 4][y + 4] == 0 and board[x - 1][y - 1] == 0:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2 and board[x - 1][y - 1] == 2:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 2 or board[x - 1][y - 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1:
                    if board[x + 3][y + 3] == 2 or board[x - 1][y - 1] == 2:
                        score = score + 1000
                    else:
                        score = score - 1000

                ###AI말이 유리한 경우
                if board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and board[x + 3][y] == 2:
                    if board[x + 4][y] == 0 or board[x - 1][y] == 0:
                        score = score + 1000
                    elif board[x + 4][y] == 1 or board[x - 1][y] == 1:
                        score = score - 1000
                    elif board[x + 4][y] == 2 or board[x - 1][y] == 2:
                        score = score + 1500
                elif board[x][y] == 2 and board[x + 1][y] == 0 and board[x + 2][y] == 2 and board[x + 3][y] == 2:
                    if board[x + 4][y] == 0 or board[x - 1][y] == 0:
                        score = score + 1000
                    elif board[x + 4][y] == 1 or board[x - 1][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 0 and board[x + 3][y] == 2:
                    if board[x + 4][y] == 0 or board[x - 1][y] == 0:
                        score = score + 1000
                    elif board[x + 4][y] == 1 or board[x - 1][y] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2:
                    score = score + 1000

                ##가로
                if board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and board[x][y + 3] == 2:
                    if board[x][y + 4] == 0 or board[x][y - 1] == 0:
                        score = score + 1000
                    elif board[x][y + 4] == 1 or board[x][y - 1] == 1:
                        score = score - 1000
                    elif board[x][y + 4] == 2 or board[x][y - 1] == 2:
                        score = score + 1500
                elif board[x][y] == 2 and board[x][y + 1] == 0 and board[x][y + 2] == 2 and board[x][y + 3] == 2:
                    if board[x][y + 4] == 0 or board[x][y - 1] == 0:
                        score = score + 1000
                    elif board[x][y + 4] == 1 or board[x][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 0 and board[x][y + 3] == 2:
                    if board[x][y + 4] == 0 or board[x][y - 1] == 0:
                        score = score + 1000
                    elif board[x][y + 4] == 1 or board[x][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2:
                    score = score + 1000

                ###대각선
                if board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2:
                    if board[x + 4][y + 4] == 0 or board[x - 1][y - 1] == 0:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 1 or board[x - 1][y - 1] == 1:
                        score = score - 1000
                    elif board[x + 4][y + 4] == 2 or board[x - 1][y - 1] == 2:
                        score = score + 1500
                elif board[x][y] == 2 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2:
                    if board[x + 4][y + 4] == 0 or board[x - 1][y - 1] == 0:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 1 or board[x - 1][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 2:
                    if board[x + 4][y + 4] == 0 or board[x - 1][y - 1] == 0:
                        score = score + 1000
                    elif board[x + 4][y + 4] == 1 or board[x - 1][y - 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2:
                    score = score + 1000

    ###여기서부터 남은 다른 대각선 하나 확인함.
    for x in range(0, 10):
        for y in range(4, 14):
            ### 맨 위쪽 가장자리
            if x == 0:
                ##마지막 방향
                if board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 1 and board[x + 3][
                    y - 3] == 1:
                    if board[x + 4][y - 4] == 0:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 0 and board[x + 2][y - 2] == 1 and board[x + 3][
                    y - 3] == 1:
                    if board[x + 4][y - 4] == 0:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 0 and board[x + 3][
                    y - 3] == 1:
                    if board[x + 4][y - 4] == 0:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 1:
                    score = score - 1000

                ### AI말의 유리한 경우
                if board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 2 and board[x + 3][
                    y - 3] == 2:
                    if board[x + 4][y - 4] == 0:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 0 and board[x + 2][y - 2] == 2 and board[x + 3][
                    y - 3] == 2:
                    if board[x + 4][y - 4] == 0:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 0 and board[x + 3][
                    y - 3] == 2:
                    if board[x + 4][y - 4] == 0:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 2:
                    score = score + 1000

            ###맨 아래쪽 가장자리
            elif x == 10:
                if board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 1 and board[x + 3][
                    y - 3] == 1:
                    if board[x - 1][y + 1] == 0:
                        score = score - 1000
                    elif board[x - 1][y + 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 0 and board[x + 2][y - 2] == 1 and board[x + 3][
                    y - 3] == 1:
                    if board[x - 1][y + 1] == 0:
                        score = score - 1000
                    elif board[x - 1][y + 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 0 and board[x + 3][
                    y - 3] == 1:
                    if board[x - 1][y + 1] == 0:
                        score = score - 1000
                    elif board[x - 1][y + 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 1:
                    score = score - 1000

                ### AI말이 유리한 경우
                if board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 2 and board[x + 3][
                    y - 3] == 2:
                    if board[x - 1][y + 1] == 0:
                        score = score + 1000
                    elif board[x - 1][y + 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 0 and board[x + 2][y - 2] == 2 and board[x + 3][
                    y - 3] == 2:
                    if board[x - 1][y + 1] == 0:
                        score = score + 1000
                    elif board[x - 1][y + 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 0 and board[x + 3][
                    y - 3] == 2:
                    if board[x - 1][y + 1] == 0:
                        score = score + 1000
                    elif board[x - 1][y + 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 2:
                    score = score + 1000

            #### 나머지 경우
            else:
                if board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 1 and board[x + 3][
                    y - 3] == 1:
                    if board[x + 4][y - 4] == 1 or board[x - 1][y + 1] == 1:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 0 and board[x - 1][y + 1] == 0:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2 and board[x - 1][y + 1] == 2:
                        score = score + 1500
                    elif board[x + 4][y - 4] == 2 or board[x - 1][y + 1] == 2:
                        score = score + 500
                elif board[x][y] == 1 and board[x + 1][y - 1] == 0 and board[x + 2][y - 2] == 1 and board[x + 3][
                    y - 3] == 1:
                    if board[x + 4][y - 4] == 0 and board[x - 1][y + 1] == 0:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2 and board[x - 1][y + 1] == 2:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 2 or board[x - 1][y + 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 0 and board[x + 3][y] == 1:
                    if board[x + 4][y - 4] == 0 and board[x - 1][y + 1] == 0:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2 and board[x - 1][y + 1] == 2:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 2 or board[x - 1][y + 1] == 2:
                        score = score + 1000
                elif board[x][y] == 1 and board[x + 1][y - 1] == 1 and board[x + 2][y - 2] == 1:
                    if board[x + 3][y - 3] == 2 and board[x - 1][y + 1] == 2:
                        score = score + 1000
                    else:
                        score = score - 1000

                ###AI말이 유리한 경우
                if board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 2 and board[x + 3][
                    y - 3] == 2:
                    if board[x + 4][y - 4] == 0 or board[x - 1][y + 1] == 0:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 1 or board[x - 1][y + 1] == 1:
                        score = score - 1000
                    elif board[x + 4][y - 4] == 2 or board[x - 1][y + 1] == 2:
                        score = score + 1500
                elif board[x][y] == 2 and board[x + 1][y - 1] == 0 and board[x + 2][y - 2] == 2 and board[x + 3][
                    y - 3] == 2:
                    if board[x + 4][y - 4] == 0 or board[x - 1][y + 1] == 0:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 1 or board[x - 1][y + 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 0 and board[x + 3][y] == 2:
                    if board[x + 4][y - 4] == 0 or board[x - 1][y + 1] == 0:
                        score = score + 1000
                    elif board[x + 4][y - 4] == 1 or board[x - 1][y + 1] == 1:
                        score = score - 1000
                elif board[x][y] == 2 and board[x + 1][y - 1] == 2 and board[x + 2][y - 2] == 2:
                    score = score + 1000

    ###final 위의 조건이 전혀 해당되지 않을 경우에 대해서.
    ###주위의 말들을 보고
    ### 가장 많은데에 연결된것을 score를 준다.
    for a in range(1, 13):
        for b in range(1, 13):
            if (board[a][b] == 0):
                pass
            else:
                if (board[a - 1][b - 1] == 2):
                    score = score + 1
                if (board[a][b - 1] == 2):
                    score = score + 1
                if (board[a + 1][b - 1] == 2):
                    score = score + 1
                if (board[a - 1][b] == 2):
                    score = score + 1
                if (board[a + 1][b] == 2):
                    score = score + 1
                if (board[a - 1][b + 1] == 2):
                    score = score + 1
                if (board[a][b + 1] == 2):
                    score = score + 1
                if (board[a + 1][b + 1] == 2):
                    score = score + 1
    return score


def input_handler(get_depth):
    global depth
    depth = get_depth
    depth_label2.set_text("You input the depth:")
    depth_label3.set_text(depth)
def mouse_handler(position):
    global count_label, turn
    x = int(round(position[0] / scale))
    y = int(round(position[1] / scale))
    if (turn == 3):
        pass
    elif (board[x][y] == 0):
        board[x][y] = 1
        turn = 2
        if (turn == 2):
            count_label.set_text('Your turn')
    else:
        pass
####승리체크함수 – Rulebased에서 사용
def finishcheck(canvas):
    global count_label, turn
    for x in range(0, 10):
        for y in range(0, 10):
            if (board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and board[x + 3][
                y + 3] == 1 and board[x + 4][y + 4] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and board[x + 3][
                y + 3] == 2 and board[x + 4][y + 4] == 2):
                turn = 4
    for x in range(0, 10):
        for y in range(0, 10):
            if (board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1 and board[x + 3][y] == 1 and
                    board[x + 4][y] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and board[x + 3][y] == 2 and
                  board[x + 4][y] == 2):
                turn = 4
    for x in range(0, 14):
        for y in range(0, 10):
            if (board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and board[x][y + 3] == 1 and
                    board[x][y + 4] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and board[x][y + 3] == 2 and
                  board[x][y + 4] == 2):
                turn = 4
    for x in range(4, 14):
        for y in range(0, 10):
            if (board[x][y] == 1 and board[x - 1][y + 1] == 1 and board[x - 2][y + 2] == 1 and board[x - 3][
                y + 3] == 1 and board[x - 4][y + 4] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x - 1][y + 1] == 2 and board[x - 2][y + 2] == 2 and board[x - 3][
                y + 3] == 2 and board[x - 4][y + 4] == 2):
                turn = 4
    return turn
#### simplegui 함수입니다. 건드릴 필요 없습니다.
def draw(canvas):
    global turn
    depth = int(depth_label3.get_text())
    for y in range(int(HEIGHT / scale)):
        canvas.draw_line((0, y * scale), (WIDTH, y * scale), 1, "Gray")
    for x in range(int(WIDTH / scale)):
        canvas.draw_line((x * scale, 0), (x * scale, HEIGHT), 1, "Gray")
    for x in range(0, 14):
        for y in range(0, 14):
            if (board[x][y] == 1):
                canvas.draw_circle(((x) * 40, (y) * 40), 10, 1, 'red', 'red')
            elif (board[x][y] == 2):
                canvas.draw_circle(((x) * 40, (y) * 40), 10, 1, 'white', 'white')
    check = finishcheck(canvas)
    if (check == 3):
        count_label.set_text('Player win')
        turn = 3
    elif (check == 4):
        count_label.set_text('AI win')
        turn = 3
    else:
        ###실제 실행하는 부분입니다.
        if turn == 2:
            currentnode = Node()
            currentnode.currentboard = board
            currentnode.bestvalue = minimax(currentnode, depth, 2)
            xmove = 0
            ymove = 0
            for i in currentnode.child:
                if currentnode.bestvalue == i.bestvalue:
                    xmove = i.xmove
                    ymove = i.ymove
            board[xmove][ymove] = 2
            turn = 1


depth = 0
frame = simplegui.create_frame("Connect 5", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)
count_label = frame.add_label(str('Your turn'))
line = frame.add_label("")
depth_label = frame.add_label("Depth - write the number and press enter")
depth_input = frame.add_input("", input_handler, 20)
depth_label2 = frame.add_label("Put your Depth in number")
depth_label3 = frame.add_label("")
frame.start()