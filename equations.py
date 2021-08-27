class Equation:
    def __init__(self, constants, degree):

        self.const = constants
        self.degree = degree
        self.co_ordinates = []
        self.points()

    def points(self):
        n = self.degree
        coef = []
        for i in self.const:
            k = i/(20**(n-1)) # 20 is pixel difference for one unit graph in coordinate.py
            coef.append(k)
            n -= 1

        for x in range(-800,800):
            n = self.degree
            y = 0
            for i in coef:
                y += i*(x**n)
                n -= 1
            x_y = (x, round(y))
            self.co_ordinates.append(x_y)
