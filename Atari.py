from ursina import *

game = Ursina()

skybox_image = load_texture("black.png")
Sky(texture=skybox_image)
window.fps_counter.enabled = False

dx = -0.02
dy = -0.02
score = 0
dead = False

#scoring thing
scoring = []
destroy1=[]
brick=Entity(model="cube",texture="blue",scale=(1,0.5,0.5), position = (-5.5, 3),collider="box")
scoring.append(brick)
for i in range(-4,6,2):
    scoring.append(duplicate(brick, x = (i + 0.5)))

brick2=Entity(model="cube", color=color.yellow,texture="orange",scale=(1,0.5,0.5), position = (-4.5, 2),collider="box")
scoring.append(brick2)

for i in range(-2,5,2):
    scoring.append(duplicate(brick2, x = (i-0.5)))

brick=Entity(model="cube", color=color.yellow,texture="yellow",scale=(1,0.5,0.5), position = (-5.5, 1),collider="box")
scoring.append(brick)

for i in range(-4,6,2):
    scoring.append(duplicate(brick, x = (i + 0.5)))


walls = []

hitter=Entity(model="cube", texture="paddle",scale=(2,0.5,0.5), position = (0, -3),collider="box")
destroy1.append(hitter)
surface = []


surface_top=Entity(model="cube",texture="black",scale=(1,0.5,0.5), position = (-7, 4),collider="box")
for i in range(-7,+8):
    walls.append(duplicate(surface_top, x=i))
surface2=[]
surface_left=Entity(model="cube",texture="black",scale=(0.5,1,0.5), position = (-7, 4),collider="box")
for i in range(-7,+8):

    surface2.append(duplicate(surface_left, y=i))

surface_right=Entity(model="cube",texture="black",scale=(0.5,1,0.5), position = (7, 4),collider="box")
for i in range(-7,+8):
    surface.append(duplicate(surface_right, y=i))

circle=Entity(model="sphere", color=color.green,scale=(0.2,0.2,0.2),  position= (0,0),collider="box")

def update():
    global dx,dy,score,dead
    if score == 17:
        print_on_screen("You win")
        for i in surface:
                destroy(i)
        for i in walls:
            destroy(i)
        for i in scoring:
            destroy(i)
            destroy(brick2)
            destroy(brick)
        destroy(surface_left)
        destroy(surface_right)
        destroy(surface_top)
        for i in surface2:
            destroy(i)
        destroy(hitter)
        destroy(circle)
    elif dead == False:
        if circle.y <= -4:
            dead=True
        circle.x += dx 
        circle.y += dy
        hit_info = hitter.intersects()
        if hit_info.entity in surface:
            hitter.x -= ( held_keys["left arrow"]) * time.dt * 5
        elif hit_info.entity in surface2:
            hitter.x += (held_keys["right arrow"]) * time.dt * 5
        else:
            hitter.x += (held_keys["right arrow"] - held_keys["left arrow"]) * time.dt * 5
        hit_info = circle.intersects()
        if hit_info.hit:
            if hit_info.entity == hitter:
                if abs(circle.y - hitter.y) >= 0.32:
                    dy = -dy
                    dx = dx
                else:
                    dx = -dx
                    dy = dy
            if hit_info.entity in walls:
                dy = -dy
                dx = dx
            if hit_info.entity in surface:
                dy = dy
                dx = -dx
            if hit_info.entity in surface2:
                dy = dy
                dx = -dx
            if hit_info.entity in scoring:
                
                score += 1
                if abs(circle.y - hit_info.entity.y) >= 0.32:
                    dy = -dy
                else:
                    dx = -dx
                destroy(hit_info.entity)
        print_on_screen(f"Score: {score} ", position=(-0.81,0.445))
    else:
        for i in surface:
                destroy(i)
        for i in walls:
            destroy(i)
        for i in scoring:
            destroy(i)
            destroy(brick2)
            destroy(brick)
        destroy(surface_left)
        destroy(surface_right)
        destroy(surface_top)
        for i in surface2:
            destroy(i)
        destroy(hitter)
        destroy(circle)
        print_on_screen(f"YOU LOST", position=(-0.01,0.05)) 
        print_on_screen(f"Score: {score}", position=(0,0))      
EditorCamera()
game.run()
