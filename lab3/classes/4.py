class Point: 
    def __init__(self, x,y): 
        self.x = x 
        self.y = y
    
    def show(self): 
        print(self.x, self.y)

    def move(self, l, m): 
        self.x = l
        self.y = m

    def dist(self, other):
        d = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        print(round(d, 3))


A = Point(2,3)
B = Point(5,6)

A.show()
B.show()
A.dist(B)
A.move(5,6)
B.dist(A)





