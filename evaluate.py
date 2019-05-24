from gomoku_test import EMPTY, PLAYER1, PLAYER2, AI


PLAYER1_7PATTERNS = [[AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, AI], # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                     [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                     [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],]
PLAYER1_6PATTERNS = [[EMPTY, PLAYER1, PLAYER1, PLAYER1, PLAYER1, EMPTY], # 2. 사목
                     [PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],   # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                     [PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                     [PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, AI],
                     [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1],
                     [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1],
                     [AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1],
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, PLAYER1, AI],   # 7. 상대편 바둑돌이 막고 있는 사목
                     [AI, PLAYER1, PLAYER1, PLAYER1, PLAYER1, EMPTY],
                     [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],   # 8. 빈칸 있는 삼목
                     [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],
                     [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],   # 9. 빈칸 있고 상대편 바둑돌이 막고 있는 삼목
                     [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                     [AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],
                     [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],]
PLAYER1_5PATTERNS = [[PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1],     # 1. 오목
                     [PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1],       # 3. 빈칸 하나 있는 사목
                     [PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1],
                     [PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1],
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY],         # 6. 삼목
                     [EMPTY, PLAYER1, PLAYER1, PLAYER1, AI],            # 10. 상대편 바둑돌이 막고 있는 삼목
                     [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY],]
PLAYER1_4PATTERNS = [[EMPTY, PLAYER1, PLAYER1, EMPTY],                  # 11. 이목
                     [EMPTY, PLAYER1, PLAYER1, AI],                     # 12. 상대편 바둑돌이 막고 있는 이목
                     [AI, PLAYER1, PLAYER1, EMPTY]]


AI_7PATTERNS = [[PLAYER1, AI, EMPTY, AI, AI, AI, PLAYER1], # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                     [PLAYER1, AI, AI, EMPTY, AI, AI, PLAYER1],
                     [PLAYER1, AI, AI, AI, EMPTY, AI, PLAYER1],]
AI_6PATTERNS = [[EMPTY, AI, AI, AI, AI, EMPTY], # 2. 사목
                     [AI, AI, AI, EMPTY, AI, PLAYER1],   # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                     [AI, AI, EMPTY, AI, AI, PLAYER1],
                     [AI, EMPTY, AI, AI, AI, PLAYER1],
                     [PLAYER1, AI, AI, AI, EMPTY, AI],
                     [PLAYER1, AI, AI, EMPTY, AI, AI],
                     [PLAYER1, AI, EMPTY, AI, AI, AI],
                     [EMPTY, AI, AI, AI, AI, PLAYER1],   # 7. 상대편 바둑돌이 막고 있는 사목
                     [PLAYER1, AI, AI, AI, AI, EMPTY],
                     [EMPTY, AI, EMPTY, AI, AI, EMPTY],   # 8. 빈칸 있는 삼목
                     [EMPTY, AI, AI, EMPTY, AI, EMPTY],
                     [EMPTY, AI, AI, EMPTY, AI, PLAYER1],   # 9. 빈칸 있고 상대편 바둑돌이 막고 있는 삼목
                     [EMPTY, AI, EMPTY, AI, AI, PLAYER1],
                     [PLAYER1, AI, EMPTY, AI, AI, EMPTY],
                     [PLAYER1, AI, AI, EMPTY, AI, EMPTY],]
AI_5PATTERNS = [[AI, AI, AI, AI, AI],     # 1. 오목
                     [AI, EMPTY, AI, AI, AI],       # 3. 빈칸 하나 있는 사목
                     [AI, AI, EMPTY, AI, AI],
                     [AI, AI, AI, EMPTY, AI],
                     [EMPTY, AI, AI, AI, EMPTY],         # 6. 삼목
                     [EMPTY, AI, AI, AI, PLAYER1],            # 10. 상대편 바둑돌이 막고 있는 삼목
                     [PLAYER1, AI, AI, AI, EMPTY],]
AI_4PATTERNS = [[EMPTY, AI, AI, EMPTY],                  # 11. 이목
                     [EMPTY, AI, AI, PLAYER1],                     # 12. 상대편 바둑돌이 막고 있는 이목
                     [PLAYER1, AI, AI, EMPTY]]



AI_7PATTERNS = [[PLAYER1, AI, EMPTY, AI, AI, AI, PLAYER1],
                [PLAYER1, AI, AI, EMPTY, AI, AI, PLAYER1],
                [PLAYER1, AI, AI, AI, EMPTY, AI, PLAYER1],]