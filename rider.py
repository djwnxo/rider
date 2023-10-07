from ursina import *
import pygame
import random
app = Ursina()


# 중력 상수 (가속도, m/s^2)
gravity = 9.81

# 물체 생성
ground = Entity(model='cube',scale=(20,1,1),collider='box',position=(0,-1,0))
cube = Entity(model='cube', scale=(2, 1, 5), color=color.blue, texture='white_cube',collider='box')

ground_value = []


# 초기 속도 및 위치 설정
cube.y = 5  # 초기 높이 설정
cube.velocity = Vec3(0, 0, 0)  # 초기 속도
cube.acceleration = Vec3(0, 0, 0)  # 초기 가속도

# 땅에 닿았는지 여부를 나타내는 플래그
on_ground = False

# 키보드 입력 관련 변수
movement_speed = 5  # 이동 속도
jump_speed = 8  # 점프 속도

is_creating_cube = False
count = 0
up_value =[]
rantime = random.randrange(1,1200)
def update():
    global up
    global is_creating_cube
    global on_ground
    global ground
    global count
    global rantime
    # 중력에 의한 가속도 계산
    if not on_ground:
        cube.acceleration.y = -gravity

    # 속도 계산
    cube.velocity += cube.acceleration * time.dt

    # 위치 계산
    cube.position += cube.velocity * time.dt

    cube.velocity.x = cube.velocity.x * 0.90

    camera.position=(cube.position.x,cube.position.y,-20)

    

    if cube.position.y < ground.position.y+1:
        cube.y = ground.position.y+1  # 땅에 닿았으면 물체를 땅 위에 놓고
        cube.velocity.y = 0  # 속도를 0으로 설정
        cube.acceleration.y = 0  # 가속도를 0으로 설정
        on_ground = True
        cube.rotation_z = 0
    else:
        on_ground = False
    
    for ground in ground_value:
        if ground.position.x < cube.position.x-9:
            destroy(ground)
            ground_value.remove(ground)
    for up in up_value:
        if up.position.x < cube.position.x-9:
            destroy(up)
            up_value.remove(up)



    # 키보드 입력 처리
    if held_keys['a']:  # 'a' 키를 누르면 왼쪽으로 이동
        cube.velocity.x = -10
    elif held_keys['d']:  # 'd' 키를 누르면 오른쪽으로 이동
        cube.velocity.x = 10

    if on_ground:
        if held_keys['space']:  # '스페이스' 키를 누르면 점프
            cube.velocity.y = jump_speed
            
    if held_keys['space']:
        cube.rotation_z += -5
    if abs(cube.velocity.x) <0.1:
        is_creating_cube = False
    else : 
        is_creating_cube = True
    
    if is_creating_cube == True:
        ground_value.append(Entity(model='cube',collider = 'box', scale=1,position=(cube.position.x+10,-1,0),texture="rainbow"))
    
    if count == rantime:
        up_value.append(Entity(model='cube',collider = 'box', scale=(1.8,1,1),position=(cube.position.x+10,0,0),texture="rainbow", rotation_z=-45))
        count = 0
        rantime = random.randrange(1,1200)
    count+=1
    

    

app.run()