from ursina import *

app = Ursina()
cube = Entity(model='cube')
# 카메라 설정
camera.position = (0, 1, -5)  # 초기 카메라 위치
original_fov = camera.fov
fov_speed = 5.0

boost_on = False  # boost_on 변수 추가 및 초기화
movement_speed = 5.0  # 움직임 속도 설정
rotation_speed = 100.0  # 시점 변환 속도 설정

# 움직임 관련 변수
current_velocity = Vec3(0, 0, 0)
max_speed = 10.0
acceleration = 5.0
deceleration = 10.0

# 컨트롤 키 누른 후 지난 시간
ctrl_pressed_time = 0
ctrl_hold_duration = 2.0  # 컨트롤 키를 꾹 눌렀을 때 FOV가 변하고 원래대로 돌아올 때까지의 시간

boost_time = 0
def update():
    global boost_on, current_velocity, ctrl_pressed_time, boost_time

    if held_keys['control'] and not boost_on:
        boost_on = True
        boost_time = 3  # 컨트롤 키 누른 시간 기록

    if boost_on:
        camera.fov = lerp(camera.fov, original_fov - 20, fov_speed * time.dt)
    else:
        # 컨트롤 키를 누르고 일정 시간이 지난 경우 FOV를 원래대로 돌립니다.
        if boost_time - ctrl_pressed_time > ctrl_hold_duration:
            camera.fov = lerp(camera.fov, original_fov, fov_speed * time.dt)
            while boost_time == 0:
                boost_time -= 1
    if not held_keys['control'] and boost_on:
        boost_on = False

    camera.rotation_x -= mouse.velocity[1] * rotation_speed * time.dt
    camera.rotation_y += mouse.velocity[0] * rotation_speed * time.dt

    if held_keys['w']:
        current_velocity += camera.forward * acceleration * time.dt
    if held_keys['s']:
        current_velocity -= camera.forward * acceleration * time.dt
    if held_keys['a']:
        current_velocity -= camera.right * acceleration * time.dt
    if held_keys['d']:
        current_velocity += camera.right * acceleration * time.dt

    current_velocity = lerp(current_velocity, Vec3(0, 0, 0), deceleration * time.dt)
    current_velocity = clamp(current_velocity, -max_speed, max_speed)
    camera.position += current_velocity * time.dt

app.run()
