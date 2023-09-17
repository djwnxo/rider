from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

player = FirstPersonController(model='cube')
camera.z = -5

original_fov = camera.fov

zoomed_in = False

def update():
    global zoomed_in
    if held_keys['w'] and not zoomed_in:
        camera.fov+= 1000 * time.dt
        zoomed_in = True
        
    if not held_keys['w'] and zoomed_in:
            camera.fov = original_fov  # 원래 FOV 값으로 되돌림
            zoomed_in = False
app.run()