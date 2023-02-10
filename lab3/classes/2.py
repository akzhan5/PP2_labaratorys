class Shape: 
    def __init__(self): 
        self.ar =0

    def area(self): 
        print(self.ar)

class Square(Shape): 
    def __init__(self, l): 
        self.length = l
        self.ar = l*l


s = Shape()
s.area()

k = Square(5)
k.area() # method is inherited from the class Shape



