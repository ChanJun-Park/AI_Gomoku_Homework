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

#                          5.          3.                  4.
PLAYER1_7PATTERNS_SCORE = [25, 25, 25, 2000, 2000, 2000, 1000, 1000, 1000, 1000, 1000, 1000]
#                          2.       7.      8.      9.
PLAYER1_6PATTERNS_SCORE = [100000, 25, 25, 50, 50, 5, 5, 5, 5]
#                          1.        6.  10.
PLAYER1_5PATTERNS_SCORE = [1000000, 1010, 3, 3]
#                         11. 12.
PLAYER1_4PATTERNS_SCORE = [2, 1, 1]


AI_7PATTERNS = [[PLAYER1, AI, EMPTY, AI, AI, AI, PLAYER1],  # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
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
AI_6PATTERNS = [[EMPTY, AI, AI, AI, AI, EMPTY],     # 2. 사목
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

#                     5.             3.                4.
AI_7PATTERNS_SCORE = [25, 25, 25, 2000, 2000, 2000, 1000, 1000, 1000, 1000, 1000, 1000]
#                     2.      7.      8.      9.
AI_6PATTERNS_SCORE = [100000, 25, 25, 50, 50, 5, 5, 5, 5]
#                     1.       6.   10.
AI_5PATTERNS_SCORE = [1000000, 1000, 3, 3]
#                    11. 12.
AI_4PATTERNS_SCORE = [2, 1, 1]

# 첫 번째 EMPTY에 착수하면 되는 끝내기 패턴
AI_ENDGAME_PATTERN1 = [[PLAYER1, AI, EMPTY, AI, AI, AI, PLAYER1],  # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                       [PLAYER1, AI, AI, EMPTY, AI, AI, PLAYER1],
                       [PLAYER1, AI, AI, AI, EMPTY, AI, PLAYER1],
                       [PLAYER1, AI, AI, AI, EMPTY, AI, EMPTY],    # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                       [PLAYER1, AI, AI, EMPTY, AI, AI, EMPTY],
                       [PLAYER1, AI, EMPTY, AI, AI, AI, EMPTY],
                       [EMPTY, AI, AI, AI, AI, EMPTY],     # 2. 사목
                       [EMPTY, AI, AI, AI, AI, PLAYER1],   # 7. 상대편 바둑돌이 막고 있는 사목
                       [PLAYER1, AI, AI, AI, AI, EMPTY]]

# 두 번째 EMPTY에 착수하면 되는 끝내기 패턴
AI_ENDGAME_PATTERN2 = [[EMPTY, AI, EMPTY, AI, AI, AI, EMPTY],  # 3. 빈칸 하나 있는 사목
                       [EMPTY, AI, AI, EMPTY, AI, AI, EMPTY],
                       [EMPTY, AI, AI, AI, EMPTY, AI, EMPTY],
                       [EMPTY, AI, AI, AI, EMPTY, AI, PLAYER1],  # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                       [EMPTY, AI, AI, EMPTY, AI, AI, PLAYER1],
                       [EMPTY, AI, EMPTY, AI, AI, AI, PLAYER1]]

# 첫 번째 EMPTY에 착수하면 되는 필수 방어 패턴
AI_DEFENCE_PATTERN1 = [[AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, AI],  # 5. 양쪽에 상대편 바둑돌들이 막고있는 빈칸 하나 있는사목
                       [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                       [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],
                       [AI, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],  # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                       [AI, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],
                       [AI, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY],
                       [EMPTY, PLAYER1, PLAYER1, PLAYER1, PLAYER1, AI],  # 7. 상대편 바둑돌이 막고 있는 사목
                       [AI, PLAYER1, PLAYER1, PLAYER1, PLAYER1, EMPTY]]

# 두 번째 EMPTY에 착수하면 되는 필수 방어 패턴
AI_DEFENCE_PATTERN2 = [[EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY],  # 3. 빈칸 하나 있는 사목
                       [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, EMPTY],
                       [EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, EMPTY],
                       [EMPTY, PLAYER1, PLAYER1, PLAYER1, EMPTY, PLAYER1, AI],  # 4. 상대편 바둑돌이 막고 있고 빈칸 하나 있는 사목
                       [EMPTY, PLAYER1, PLAYER1, EMPTY, PLAYER1, PLAYER1, AI],
                       [EMPTY, PLAYER1, EMPTY, PLAYER1, PLAYER1, PLAYER1, AI]]
