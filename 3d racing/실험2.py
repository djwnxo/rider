import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple 2D Game")

# 색상 정의
white = (255, 255, 255)

# 플레이어 설정
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_speed = 5
player_jump = -10
player_gravity = 1
is_jumping = False

# 장애물 설정
obstacle_width = 50
obstacle_height = 50
obstacle_x = screen_width - obstacle_width
obstacle_y = screen_height - obstacle_height
obstacle_speed = 3

# 점수
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True

    # 점프
    if is_jumping:
        player_y += player_jump
        is_jumping = False
    else:
        player_y += player_gravity

    # 장애물 이동
    obstacle_x -= obstacle_speed

    # 장애물 재생성
    if obstacle_x < 0:
        obstacle_x = screen_width
        score += 1

    # 충돌 검사
    if (
        player_x + player_width > obstacle_x
        and player_x < obstacle_x + obstacle_width
        and player_y + player_height > obstacle_y
    ):
        running = False

    # 그리기
    screen.fill(white)
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, (0, 0, 255), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    score_display = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_display, (10, 10))
    pygame.display.update()

# 게임 종료
pygame.quit()
sys.exit()
