Web VPython 3.2
import random

box(size = vec(800,330,15), texture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtDcZA0DD0CSfz4etaHUismgenTXa9HmvknE0k4a1LEg&s")

ball = sphere(pos=vec(-380,20,0), radius=8, color=color.cyan, make_trail=True)
g = vec(0,-9.8,0)
ball.v = vec(30,60,0)
dt = 0.01

colors = [color.cyan, color.red, color.green, color.orange, color.yellow, color.magenta]

while True:
    rate(200)
    ball.pos = ball.pos + ball.v * dt
    ball.v = ball.v + g * dt
    
    if ball.pos.y <= 20:
        sleep(1)
        ball.color = random.choice(colors)

        random_vx = random.uniform(15, 50)
        random_vy = random.uniform(40, 85)
        
        ball.v = vec(random_vx, random_vy, 0)
import time
import winsound


