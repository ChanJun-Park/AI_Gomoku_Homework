from gomoku_constant import *


PLAYER1_7PATTERNS = [[AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, AI],  # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                     [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                     [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],
                     [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY],  # 3. 빈칸 하나 있는 사목
                     [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],  # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                     [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                     [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, AI],
                     [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],
                     [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],
                     [AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY]]
PLAYER1_6PATTERNS = [[EMPTY, PLAYER1, PLAYER1, PLAYER1, PLAYER1, EMPTY],   # 2. 사목
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, PLAYER1, AI],   # 7. 상대편 바둑돌이 막고 있는 사목
                     [AI, PLAYER1, PLAYER1, PLAYER1, PLAYER1, EMPTY],
                     [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],   # 8. 빈칸 있는 삼목
                     [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],
                     [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],   # 9. 빈칸 있고 상대편 바둑돌이 막고 있는 삼목
                     [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                     [AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],
                     [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY]]
PLAYER1_5PATTERNS = [[PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1],     # 1. 오목
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY],         # 6. 삼목
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, AI],            # 10. 상대편 바둑돌이 막고 있는 삼목
                     [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY]]
PLAYER1_4PATTERNS = [[EMPTY, PLAYER1, PLAYER1, EMPTY],                  # 11. 이목
                     [EMPTY, PLAYER1, PLAYER1, AI],                     # 12. 상대편 바둑돌이 막고 있는 이목
                     [AI, PLAYER1, PLAYER1, EMPTY]]

PLAYER1_7PATTERNS_SCORE = [23, 23, 23, 100, 100, 100, 50, 50, 50, 50, 50, 50]
PLAYER1_6PATTERNS_SCORE = [1000, 27, 27, 20, 20, 10, 10, 10, 10]
PLAYER1_5PATTERNS_SCORE = [10000, 30, 6, 6]
PLAYER1_4PATTERNS_SCORE = [2, 1, 1]


AI_7PATTERNS = [[PLAYER1, AI, EMPTY, AI, AI, AI, PLAYER1], # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                [PLAYER1, AI, AI, EMPTY, AI, AI, PLAYER1],
                [PLAYER1, AI, AI, AI, EMPTY, AI, PLAYER1],
                [EMPTY, AI, EMPTY, AI, AI, AI, EMPTY],  # 3. 빈칸 하나 있는 사목
                [EMPTY, AI, AI, EMPTY, AI, AI, EMPTY],
                [EMPTY, AI, AI, AI, EMPTY, AI, EMPTY],
                [EMPTY, AI, AI, AI, EMPTY, AI, PLAYER1],  # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                [EMPTY, AI, AI, EMPTY, AI, AI, PLAYER1],
                [EMPTY, AI, EMPTY, AI, AI, AI, PLAYER1],
                [PLAYER1, AI, AI, AI, EMPTY, AI, EMPTY],
                [PLAYER1, AI, AI, EMPTY, AI, AI, EMPTY],
                [PLAYER1, AI, EMPTY, AI, AI, AI, EMPTY]]
AI_6PATTERNS = [[EMPTY, AI, AI, AI, AI, EMPTY], # 2. 사목
                [EMPTY, AI, AI, AI, AI, PLAYER1],   # 7. 상대편 바둑돌이 막고 있는 사목
                [PLAYER1, AI, AI, AI, AI, EMPTY],
                [EMPTY, AI, EMPTY, AI, AI, EMPTY],   # 8. 빈칸 있는 삼목
                [EMPTY, AI, AI, EMPTY, AI, EMPTY],
                [EMPTY, AI, AI, EMPTY, AI, PLAYER1],   # 9. 빈칸 있고 상대편 바둑돌이 막고 있는 삼목
                [EMPTY, AI, EMPTY, AI, AI, PLAYER1],
                [PLAYER1, AI, EMPTY, AI, AI, EMPTY],
                [PLAYER1, AI, AI, EMPTY, AI, EMPTY]]
AI_5PATTERNS = [[AI, AI, AI, AI, AI],                    # 1. 오목
                [EMPTY, AI, AI, AI, EMPTY],              # 6. 삼목
                [EMPTY, AI, AI, AI, PLAYER1],            # 10. 상대편 바둑돌이 막고 있는 삼목
                [PLAYER1, AI, AI, AI, EMPTY]]
AI_4PATTERNS = [[EMPTY, AI, AI, EMPTY],                  # 11. 이목
                [EMPTY, AI, AI, PLAYER1],                # 12. 상대편 바둑돌이 막고 있는 이목
                [PLAYER1, AI, AI, EMPTY]]

AI_7PATTERNS_SCORE = [23, 23, 23, 33, 33, 33, 32, 32, 32, 32, 32, 32]
AI_6PATTERNS_SCORE = [70, 27, 27, 7, 7, 3, 3, 3, 3]
AI_5PATTERNS_SCORE = [10000, 10, 6, 6]
AI_4PATTERNS_SCORE = [2, 1, 1]


DEFENCE_7PATTERNS = [[AI,PLAYER1, EMPTY,PLAYER1,PLAYER1,PLAYER1, AI], # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                     [AI,PLAYER1,PLAYER1, EMPTY,PLAYER1,PLAYER1, AI],
                     [AI,PLAYER1,PLAYER1,PLAYER1, EMPTY,PLAYER1, AI]]
DEFENCE_6PATTERNS = [[EMPTY,PLAYER1,PLAYER1,PLAYER1,PLAYER1, EMPTY],   # 열린 사목
                     [PLAYER1,PLAYER1,PLAYER1, EMPTY,PLAYER1, AI],     # 상대편이 막고있고 빈칸 하나 있는 사목
                     [PLAYER1,PLAYER1, EMPTY,PLAYER1,PLAYER1, AI],
                     [PLAYER1, EMPTY,PLAYER1,PLAYER1,PLAYER1, AI],
                     [AI,PLAYER1,PLAYER1,PLAYER1, EMPTY,PLAYER1],
                     [AI,PLAYER1,PLAYER1, EMPTY,PLAYER1,PLAYER1],
                     [AI,PLAYER1, EMPTY,PLAYER1,PLAYER1,PLAYER1],
                     [EMPTY,PLAYER1,PLAYER1,PLAYER1,PLAYER1, AI],      # 상대편이 막고있는 사목
                     [AI, PLAYER1, PLAYER1, PLAYER1, PLAYER1, EMPTY],
                     [EMPTY,PLAYER1, EMPTY,PLAYER1,PLAYER1, EMPTY],  # 8. 빈칸 있는 삼목
                     [EMPTY,PLAYER1,PLAYER1, EMPTY,PLAYER1, EMPTY]]
DEFENCE_5PATTERNS = [[PLAYER1, EMPTY,PLAYER1,PLAYER1,PLAYER1],         # 빈칸 하나 있는 사목
                     [PLAYER1,PLAYER1, EMPTY,PLAYER1,PLAYER1],
                     [PLAYER1,PLAYER1,PLAYER1, EMPTY,PLAYER1],
                     [EMPTY,PLAYER1,PLAYER1,PLAYER1, EMPTY]]            # 삼목


def e_function(board):
    score = 0

    for x in range(0, GO_BOARD_X_COUNT):
        for y in range(0, GO_BOARD_Y_COUNT):
            # → 체크
            if x < GO_BOARD_X_COUNT - 7:
                for z in range(len(AI_7PATTERNS)):
                    check = True
                    for k in range(7):
                        if board[x + k][y] != AI_7PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_7PATTERNS_SCORE[z]
            if x < GO_BOARD_X_COUNT - 6:
                for z in range(len(AI_6PATTERNS)):
                    check = True
                    for k in range(6):
                        if board[x + k][y] != AI_6PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_6PATTERNS_SCORE[z]
            if x < GO_BOARD_X_COUNT - 5:
                for z in range(len(AI_5PATTERNS)):
                    check = True
                    for k in range(5):
                        if board[x + k][y] != AI_5PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_5PATTERNS_SCORE[z]
            if x < GO_BOARD_X_COUNT - 4:
                for z in range(len(AI_4PATTERNS)):
                    check = True
                    for k in range(4):
                        if board[x + k][y] != AI_4PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_4PATTERNS_SCORE[z]

            # ↘ 체크
            if x < GO_BOARD_X_COUNT - 7 and y < GO_BOARD_Y_COUNT - 7:
                for z in range(len(AI_7PATTERNS)):
                    check = True
                    for k in range(7):
                        if board[x + k][y + k] != AI_7PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_7PATTERNS_SCORE[z]
            if x < GO_BOARD_X_COUNT - 6 and y < GO_BOARD_Y_COUNT - 6:
                for z in range(len(AI_6PATTERNS)):
                    check = True
                    for k in range(6):
                        if board[x + k][y + k] != AI_6PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_6PATTERNS_SCORE[z]
            if x < GO_BOARD_X_COUNT - 5 and y < GO_BOARD_Y_COUNT - 5:
                for z in range(len(AI_5PATTERNS)):
                    check = True
                    for k in range(5):
                        if board[x + k][y + k] != AI_5PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_5PATTERNS_SCORE[z]
            if x < GO_BOARD_X_COUNT - 4 and y < GO_BOARD_Y_COUNT - 4:
                for z in range(len(AI_4PATTERNS)):
                    check = True
                    for k in range(4):
                        if board[x + k][y + k] != AI_4PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_4PATTERNS_SCORE[z]

            # ↓ 체크
            if y < GO_BOARD_Y_COUNT - 7:
                for z in range(len(AI_7PATTERNS)):
                    check = True
                    for k in range(7):
                        if board[x][y + k] != AI_7PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_7PATTERNS_SCORE[z]
            if y < GO_BOARD_Y_COUNT - 6:
                for z in range(len(AI_6PATTERNS)):
                    check = True
                    for k in range(6):
                        if board[x][y + k] != AI_6PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_6PATTERNS_SCORE[z]
            if y < GO_BOARD_Y_COUNT - 5:
                for z in range(len(AI_5PATTERNS)):
                    check = True
                    for k in range(5):
                        if board[x][y + k] != AI_5PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_5PATTERNS_SCORE[z]
            if y < GO_BOARD_Y_COUNT - 4:
                for z in range(len(AI_4PATTERNS)):
                    check = True
                    for k in range(4):
                        if board[x][y + k] != AI_4PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_4PATTERNS_SCORE[z]

            # ↙ 체크
            if x >= 7 and y < GO_BOARD_Y_COUNT - 7:
                for z in range(len(AI_7PATTERNS)):
                    check = True
                    for k in range(7):
                        if board[x - k][y + k] != AI_7PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_7PATTERNS_SCORE[z]
            if x >= 6 and y < GO_BOARD_Y_COUNT - 6:
                for z in range(len(AI_6PATTERNS)):
                    check = True
                    for k in range(6):
                        if board[x - k][y + k] != AI_6PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_6PATTERNS_SCORE[z]
            if x >= 5 and y < GO_BOARD_Y_COUNT - 5:
                for z in range(len(AI_5PATTERNS)):
                    check = True
                    for k in range(5):
                        if board[x - k][y + k] != AI_5PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_5PATTERNS_SCORE[z]
            if x >= 4 and y < GO_BOARD_Y_COUNT - 4:
                for z in range(len(AI_4PATTERNS)):
                    check = True
                    for k in range(4):
                        if board[x - k][y + k] != AI_4PATTERNS[z][k]:
                            check = False
                            break
                    if check:
                        score += AI_4PATTERNS_SCORE[z]

    return score
