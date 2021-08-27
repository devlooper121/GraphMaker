from turtle import Turtle


class Draw(Turtle):
    def __init__(self, points):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("orange")
        self.pensize(2)
        self.points = points
        self.drawgraph()

    def drawgraph(self):
        for x_y in self.points:
            # self.pensize(10)
            x = x_y[0]
            y = x_y[1]

            self.goto(x,y)
            self.pendown()