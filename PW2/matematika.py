import turtle

screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.title("Graph: y = x/5 + 27")

screen.setworldcoordinates(-120, -40, 120, 80)

def draw_axes():
    axes = turtle.Turtle()
    axes.speed(0)
    axis.color("black")
    axis.pensize(2)

    # Draw x-axis
    axes.penup()
    axes.goto(-120, 0)
    axes.pendown()
    axes.goto(120, 0)

    # Draw y-axis
    axes.penup()
    axes.goto(0, -40)
    axes.pendown()

    # x axis labels
    for x in range(-100, 121, 20):
        axes.penup()
        axes.goto(x, -2)
        axes.pendown()
        axes.goto(x, 2)

        axes.penup()
        axes.goto(x, -6)
        axes.write(str(x), align="center", font=("Arial", 10, "normal"))

    # y axis labels
    for y in range(-40, 81, 10):
        axes.penup()
        axes.goto(-3, y)
        axes.pendown()
        axes.goto(3, y)

        if y != 0:  # Avoid writing 0 twice
            axes.penup()
            axes.goto(-10, y -2)
            axes.write(str(y), align="right", font=("Arial", 10, "normal"))

    axes.hideturtle()









