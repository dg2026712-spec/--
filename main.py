Web VPython 3.2
import random

sphere(size = vec(150,150,20), pos = vec (500,-40,50), opacity = 1, color = color. white)
sphere(size = vec(150,150,20), pos = vec (500,-200,50), opacity = 1, color = color. yellow)

box(size = vec(800,330,15), texture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtDcZA0DD0CSfz4etaHUismgenTXa9HmvknE0k4a1LEg&s")

ball = sphere(pos=vec(-380,20,0), radius=10, color=color.cyan, make_trail=True)
g = vec(0,-9.8,0)
ball.v = vec(3,0,0)
dt = 0.01


colors = [color.cyan, color.red, color.green, color.orange, color.yellow, color.magenta]

bounce_patterns = [vec(10, 55, 0), vec(10, 14, 0), vec(10, 15, 0), vec(10, 4, 0)]

pattern_index = 0 

while True:
    rate(200)
    ball.pos = ball.pos + ball.v * dt
    ball.v = ball.v + g * dt
    
    if ball.pos.y <= bounce_patterns[0].y:
        sleep(1)
        ball.color = random.choice(colors)
        ball.trail_color = ball.color

        ball.v = bounce_patterns[pattern_index]
        
        pattern_index = pattern_index + 1
        
        if pattern_index >= len(bounce_patterns):
            pattern_index = 0
        
