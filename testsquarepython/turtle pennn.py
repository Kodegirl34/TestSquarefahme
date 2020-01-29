import turtle

window = turtle.Screen()
turtle.speed(5)
turtle.pensize(5)

# Draw the outline of a square
turtle.penup()
turtle.goto(-350, 100)
turtle.pendown()
turtle.color("black")

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.penup()

# Draw the outline of a square using a For loop
turtle.goto(-175, 100)
turtle.color("magneta")
turtle.pendown()
for i in range (4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Multi-Coloured Stroke Square
turtle.goto(0, 100)
turtle.pendown()
for colours in ["yellow", "red", "purple", "blue"]:
    turtle.color(colours)
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Filled square with stroke
turtle.goto(175, 100)
turtle.color("orange", "yellow")
turtle.pendown()
turtle.begin_fill()

for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

window.exitonclick()






    
