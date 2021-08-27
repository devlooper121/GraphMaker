from turtle import Turtle


class CoordinateAxis(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.axis()
        # self.points()
        # self.doted_x()

    def axis(self):
        self.pensize(3)
        self.goto(-800, 0)
        self.pendown()
        self.fd(1600)

        self.penup()
        self.goto(0, -500)
        self.lt(90)
        self.pendown()
        self.fd(1000)

    def points(self):
        x = -800
        for _ in range(81):
            self.penup()

            self.goto(x, 0)
            self.color("blue")
            self.dot(5)
            self.goto(x, -20)
            self.write(f"{x/20}", align="left", font=("Arial", 5, "normal"))
            x += 20
        y = -500
        for _ in range(51):
            self.penup()

            self.goto(0, y)
            self.color("red")
            self.dot(5)
            self.goto(20, y)
            self.write(f"{y/20}", align="right", font=("Arial", 5, "normal"))
            y += 20

    def doted_y(self):
        x = -800

        for _ in range(81):
            self.penup()
            self.goto(x, -500)
            self.setheading(90)
            for _ in range(100):
                self.pendown()
                self.pencolor("light green")
                self.fd(10)
                self.up()
                self.fd(2)
            x += 20

