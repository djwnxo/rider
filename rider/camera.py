from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player=FirstPersonController()
ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))

#def update():
#    character.x=character.x+time.dt
#    camera.position=(character.x,0,-20)
    


character = Entity(model='asstets/bikes/scene.gltf', scale=10,collider='mesh',postion=(0,10,0))
cube_2 = Entity(model='cube', scale=(1,2,5), position=(0,-2,0))
Sky()
app.run()