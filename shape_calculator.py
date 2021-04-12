import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * (self.height + self.width)
    
    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** .5
    
    def get_picture(self):
        if(self.height < 50 and self.width < 50):
            pic = ""
            for i in range(self.height):
                for j in range(self.width):
                    pic += "*"
                pic += "\n"
            return pic
        else : return "Too big for picture."
        
    def get_amount_inside(self, oth):
        return math.floor((self.height * self.width) / oth.get_area())

class Square(Rectangle):
    
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side
    
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
    
    def set_side(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side
        
    def set_height(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side
        
    def set_width(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side

    


