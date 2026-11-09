import turtle

screen = turtle.Screen()

# only works with odd numbers of points!!
def draw_star(points):

    t = turtle.Turtle()

    for _ in range(points):
        t.forward(100)
        t.right(360 * 2 / points)
       



draw_star(11)