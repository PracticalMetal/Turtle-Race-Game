from turtle import Turtle, Screen
import random

tim=Turtle()
tim.hideturtle()
screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle do you bet on?")

colour=["red", "yellow", "green", "violet", "orange", "purple"]

tim.penup()
y_axis=-175

all_turtle=[]

for i in range(6):
    new_obj=Turtle()
    new_obj.color(colour[i])
    new_obj.penup()
    new_obj.shape("turtle")

    new_obj.goto(x=-230,y=y_axis)
    y_axis+=70
    all_turtle.append(new_obj)

start_game=False

if user_bet:
    start_game=True

while start_game:

    for turtle in all_turtle:
        forward_pace=random.randint(1,10)
        turtle.forward(forward_pace)
        if turtle.xcor() >= 240:
            winner=turtle
            start_game=False
            break

if user_bet==winner.color():
    print(f"Congrats! You won, {winner.color()[0]} turtle won.")

else:
    print(f"You lost, {winner.color()[0]} turtle won.")

screen.exitonclick()
