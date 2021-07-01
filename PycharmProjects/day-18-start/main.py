from turtle import *

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("black")
# forward(1)
# left()
# forward(300)
color('red', 'yellow')
begin_fill()
while True:
    for i in range(1):
        penup()
        forward(10)
        pendown()
        forward(10)
    left(10)
    if abs(pos()) < 1:
        break
end_fill()
done()

screen = Screen()
screen.exitonclick()
