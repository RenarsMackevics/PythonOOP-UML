import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def draw_star(points):

    for _ in range(points):
        t.forward(100)
        t.right(144)


draw_star(8)