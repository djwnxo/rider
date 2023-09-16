from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

def update():
    character.x=character.x+time.dt
    camera.position=(character.x,0,-20)
    


character = Entity(model='cube', scale=1,collider='box',postion=(0,10,0))
cube_2 = Entity(model='cube', scale=(1,2,5), position=(0,-2,0))
Sky()
app.run()