import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("unsupported operand type(s) for +: "
                        f"'{type(self).__name__}' and '{type(other).__name__}'")
    
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        raise TypeError("unsupported operand type(s) for -: "
                        f"'{type(self).__name__}' and '{type(other).__name__}'")
    
    def copy(self):
        return Vector2D(self.x, self.y)
    
    def cross(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
        else:
            raise TypeError("unsupported operand type for *: "
                            f"'{type(self).__name__}' and '{type(other).__name__}'")
            
    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def angle(self, other):
        if isinstance(other, Vector2D):
            return math.acos((self.x * other.x + self.y * other.y) / (self.norm() * other.norm()))
        raise TypeError("unsupported operand type for angle(): "
                        f"'{type(self).__name__}' and '{type(other).__name__}'")
