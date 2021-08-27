from turtle import Turtle, Screen, numinput, textinput

from coordinate import CoordinateAxis
from equations import Equation

from draw import Draw

from trigo import Trigonometry

screen = Screen()
screen.setup(1600, 1000)
screen.title("graph")

self = Turtle()
self.speed(0)
screen.tracer(0)

degree = numinput("What is max power of polynomial(x)", "e.g x^3 + x + c  --> n = 3")
constant = []
co = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
for i in range(int(degree + 1)):
    value = numinput("constant", f"{co[i]}")
    constant.append(value)
eq = Equation(constant, degree)
# eq = Trigonometry()
# eq.sin()
print(eq.co_ordinates)
draw = Draw(eq.co_ordinates)


def doted_x():
    # print("fff")
    y = -480

    for _ in range(51):
        self.penup()
        self.goto(-800, y)
        # print("1st")
        for _ in range(160):
            self.pendown()
            self.pencolor("light green")
            self.fd(10)
            self.up()
            self.fd(2)
            # print("2nd")
        y += 20


graph = CoordinateAxis()
doted_x()
graph.doted_y()
graph.points()
is_p = True

while is_p:
    screen.update()



screen.exitonclick()
