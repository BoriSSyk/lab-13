import math


class TRIANGLE():
    def __init__(self, a=0, b=0, c=0, S=0):
        self.Side_a = a
        self.Side_b = b
        self.Side_c = c
        self.Area = S

    def IsSet(self):
        if self.Side_a + self.Side_b > self.Side_c and self.Side_a + self.Side_c > self.Side_b and self.Side_b + self.Side_c > self.Side_a:
            print('Існує')
        else:
            print('Не існує')

    def CalcSquare(self):
        p = (self.Side_a + self.Side_b + self.Side_c)/2

        self.Area = math.sqrt(
            (p*(p-self.Side_a)*(p-self.Side_b)*(p-self.Side_c)))

    def ShowSquare(self):

        print(self.Area)

    def ShowDim(self):
        print(self.Side_a)
        print(self.Side_b)
        print(self.Side_c)

# TRIANGLE(3,5,7)

# TRIANGLE.IsSet()
# TRIANGLE.CalcSquare()
# TRIANGLE.ShowSquare()
# TRIANGLE.ShowDim()
