import math

class shape:
    def area(self):
        raise NotImplementedError("this method must be overridden")
        
class rectangle(shape):
    def __init__(self, L, W):
        self.L = L
        self.W = W
        
    def area(self):
        return self.L*self.W
    
class circle(shape):
    def __init__(self, R):
        self.R = R
        
    def area(self):
        return math.pi*self.R**2
    
Rectangle = rectangle(3, 8)
Circle = circle(7)

print(f"area of rectangle: {Rectangle.area()}")
print(f"area of circle: {Circle.area()}")
