import turtle

screen = turtle.Screen()

# only works with odd numbers of points!!
def draw_star(points, color=None):

    t = turtle.Turtle()

    if color:
        t.color("black", color)
        t.begin_fill()
    else:
        t.color("black")

    for _ in range(points):
        t.forward(100)
        t.right(360 * 2 / points)
       

    t.end_fill()


points = int(input("Enter the number of points for the star (odd number only): "))


if points % 2 == 0:
    print("Please enter an odd number of points.")
else:
   color = input("Enter the color for the star(leave empty for default): ")

   if color == "":
       draw_star(points)
   else:
         draw_star(points, color)

turtle.mainloop()