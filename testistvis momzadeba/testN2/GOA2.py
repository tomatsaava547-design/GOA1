import turtle


screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


t.penup()
t.goto(0, -100)
t.pendown() 
t.color("black")
t.begin_fill()
t.circle(150)
t.end_fill()


t.penup()
t.goto(-80, -20)


t.color("white")
t.write("G", font=("Arial", 60, "bold"))


t.goto(-20, -20)
t.color("green")
t.write("O", font=("Arial", 60, "bold"))

t.goto(40, -20)
t.color("white")
t.write("A",font=("Arial", 60, "bold"))



screen.mainloop()


