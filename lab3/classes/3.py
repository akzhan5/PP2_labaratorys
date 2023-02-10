class Shape: 
    def __init__(self): 
        self.ar = 0
    
    def area(self): 
        print(self.ar)


class Rectangle(Shape): 
    def __init__(self, l, w): 
        self.length = l
        self.width = w
        self.ar = self.length * self.width 
    #not necessary - area() is inherited from the Shape() parent class
    def area(self): 
        print(self.width*self.length)

    
r = Rectangle(5,4)
r.area()
