from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
tim.shape('turtle')
tim.color('red')
clear=False
def move_upward():
    tim.left(90)
    tim.forward(30)
def move_downward():
    tim.right(90)
    tim.forward(30)
def move_forward():
    tim.forward(30)
def move_backward():
    tim.backward(30)
def clears():
    tim.clear()
screen.listen()
screen.onkey(key="c",fun=clears)
screen.onkey(key="w",fun=move_upward)
screen.onkey(key="s",fun=move_downward)
screen.onkey(key="a",fun=move_backward)
screen.onkey(key="d",fun=move_forward)
screen.exitonclick()
