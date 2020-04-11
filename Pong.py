import turtle

t = turtle.Screen()
t.title("PyPong")
t.bgcolor("lightblue")
t.setup(width=800, height=600)
t.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("Blue")
paddle_a.shapesize(stretch_len=1, stretch_wid=6)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B


# Main game loop
while True:
    t.update()
