import turtle

screen = turtle.Screen()

# only works with odd numbers of points!!
def draw_star(points, color):

    t = turtle.Turtle()

    t.color("black" , color)
    t.begin_fill()

    for _ in range(points):
        t.forward(100)
        t.right(360 * 2 / points)
       

    t.end_fill()


points = int(input("Enter the number of points for the star (odd number only): "))
color = input("Enter the color for the star: ")

if points % 2 == 0:
    print("Please enter an odd number of points.")
else:
    draw_star(points, color)
    turtle.mainloop()