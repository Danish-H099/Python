class Powers:
    def square(self):
        print(f'Square of {self.num} is {self.num**2}')
    def cube(self):
        print(f'Cube of {self.num} is {self.num**3}')
    def squareRoot(self):
        print(f'SquareRoot of {self.num} is {self.num**0.5}')

n=Powers()
n.num=3
n.square()
n.squareRoot()
n.cube()
