box(size = vec(800,330,15), texture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtDcZA0DD0CSfz4etaHUismgenTXa9HmvknE0k4a1LEg&s")

ball = sphere(pos=vec(-10,20,0), radius=20, color=color.cyan, make_trail=True)
g = vec(0,-9.8,0)
ball.v = vec(10,0,0)
dt = 0.01

while ball.pos.y > 0:
    rate(100)
    ball.pos = ball.pos + ball.v * dt
    ball.v = ball.v + g * dt
