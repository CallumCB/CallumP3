import random
import turtle

badList=['Sorry to hear that',
         'Hope you feel better',
         'lol shitter',
         'Is there anything I can do to help, wait, im a computer',
         "What's wrong?"]
         

window=turtle.Screen()
smile=turtle.Turtle()

myInput=input("Hello, how are you feeling?  (good, bad)  ")

if myInput=='':
    print("What was that?")

if myInput=='good':
    print("That's good")
    for x in range(360):
        turtle.forward(1)
        turtle.right(1)
    turtle.penup()
    turtle.goto(-20,-50)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.goto(20, -50)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.goto(-20, -80)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(20, 180)

if myInput=='bad':
    print(random.choice(badList))
    for x in range(360):
        turtle.forward(1)
        turtle.right(1)
    turtle.penup()
    turtle.goto(-20,-50)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.goto(20, -50)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.goto(20, -80)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(20, 180)
else:
    print("good or bad please, actually too late, you have to restart the code now. Definetly not because my programer doesn't know how to use 'return' properly.")


