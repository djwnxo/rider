import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
WHITE = (255, 255, 255)

# 플레이어 설정
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height

# 이동 속도
player_speed = 5

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 화면 지우기
    screen.fill(WHITE)

    # 플레이어 그리기
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))

    # 화면 업데이트
    pygame.display.update()

# 게임 종료

pygame.quit()
sys.exit()
