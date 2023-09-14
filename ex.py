from ursina import *

app = Ursina()

# 중력 상수 (가속도, m/s^2)
gravity = 9.81

# 물체 생성
cube = Entity(model='cube', scale=(2, 1, 5), color=color.blue, texture='white_cube')

# 초기 속도 및 위치 설정
cube.y = 5  # 초기 높이 설정
cube.velocity = Vec3(0, 0, 0)  # 초기 속도
cube.acceleration = Vec3(0, 0, 0)  # 초기 가속도

# 땅에 닿았는지 여부를 나타내는 플래그
on_ground = False

# 키보드 입력 관련 변수
movement_speed = 5  # 이동 속도
jump_speed = 8  # 점프 속도

def update():
    global on_ground

    # 중력에 의한 가속도 계산
    if not on_ground:
        cube.acceleration.y = -gravity

    # 속도 계산
    cube.velocity += cube.acceleration * time.dt

    # 위치 계산
    cube.position += cube.velocity * time.dt

    cube.velocity.x = cube.velocity.x * 0.90
    # 땅에 닿았는지 확인
    if cube.y <= 0:
        cube.y = 0  # 땅에 닿았으면 물체를 땅 위에 놓고
        cube.velocity.y = 0  # 속도를 0으로 설정
        cube.acceleration.y = 0  # 가속도를 0으로 설정
        on_ground = True
    else:
        on_ground = False  # 땅에 닿지 않았으면 플래그를 False로 설정

    # 키보드 입력 처리
    if held_keys['a']:  # 'a' 키를 누르면 왼쪽으로 이동
        cube.velocity.x = -10
    elif held_keys['d']:  # 'd' 키를 누르면 오른쪽으로 이동
        cube.velocity.x = 10

    if on_ground:
        if held_keys['space']:  # '스페이스' 키를 누르면 점프
            cube.velocity.y = jump_speed
            
    if held_keys['space']:
        cube.rotation_z += 5
app.run()
