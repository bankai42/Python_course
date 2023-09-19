class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_square(self):
        return self.width*self.height
    
    def calculate_perimeter(self):
        return 2*(self.width+self.height)
    