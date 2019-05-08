import pygame, sys              # 모듈이름을 명시하고 함수 사용
from pygame.locals import *     # 모듈이름을 명시하지 않고도 상수나 함수 사용

pygame.init()                   # Pygame 함수를 호출하기 전에 반드시 호출해야하는 함수
DISPLAYSURF = pygame.display.set_mode((400, 300))       # 윈도우의 대한 pygame.Surface객체 반환
pygame.display.set_caption('Hello World!')              # 윈도우의 캡션 지정
while True:                     # Main game loop
    for event in pygame.event.get():                    # pygame.event.Event 객체 반환, 이전 get() 함수 호출
        if event.type == QUIT:                          # 이후의 event 들이 반환된다.
            pygame.quit()                               # pygame 라이브러리 종료
            sys.exit()
        pygame.display.update()