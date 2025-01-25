from ursina import *
from random import *
app = Ursina()

Sky(texture="")
camera.orthographic = True

da = 0.07
dead = False
offset = 0

background= Entity(model="quad" , scale=(80,40), texture="sky", z=0.1)
tetris = Animation("ezgif.com-gif-maker",position=(-20,0), scale=(5,5), collider = "box")


def update():
    global da, dead, offset
    tetris.y -= (da)
    if dead == False:
        offset += time.dt * 0.3
        setattr(background, "texture_offset" ,(offset,0))
        for i in pipes:
            i.x -= 0.08
        
        hit_info = tetris.intersects()
        if hit_info.hit:
            if hit_info.entity in pipes:
                dead=True
    else:
        for i in pipes:
            i.x += 0
        da = 0.5
        panel=Entity(model="quad", color=color.white, position=(0,0), scale=(50,20),z=-.2)
        panel2=Entity(model="quad", texture="268-2680778_flappy-bird-game-over-png-transparent-png-removebg-preview", position=(0,0), scale=(50,20),z=-.3)
def input(space):
    if space == 'space':
        tetris.y += 4


pipes=[]
pipe1 = Entity(model="quad", texture="pipe2-removebg-previe", scale=(3,30), collider="box", position=(10,14))
pipe2 = Entity(model="quad", texture="pipe2-removebg-preview (1)", scale=(3,30), collider="box", position=(10,-30))
pipes.append(pipe1)
pipes.append(pipe2)
pipe3 = Entity(model="quad", texture="pipe2-removebg-previe", scale=(3,30), collider="box", position=(50,30))
pipe4 = Entity(model="quad", texture="pipe2-removebg-preview (1)", scale=(3,30), collider="box", position=(50,-14))
pipes.append(pipe3)
pipes.append(pipe4)
for i in range(90,410,40):
    a=randint(12,30)
    pipes.append(duplicate(pipe3,x=i,y=a))
    pipes.append(duplicate(pipe4,x=i,y=a-44))

EditorCamera()
app.run()
