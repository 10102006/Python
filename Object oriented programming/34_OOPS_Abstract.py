
# ? Importing these are required
from abc import ABC, abstractmethod

# ! Abstract method is used to Force any children class of a certain parent to inherit some method

# ? ABC is required

class Shape(ABC):
    """
    This is the base abstract template
    """
# ? @abstractmethod is required
    @abstractmethod
    def GetArea(self):
        self
        pass


class Rectangle(Shape):
    type = 'Quadrilateral'
    sides = 4

    def __init__(self, len, hgt):
        '''
        This is constructor is for making shapes
        '''
        self.length = len
        self.height = hgt

# ? At last defining this abstract method is required and the name should be same but the methods can be different
    def GetArea(self):
        """
        This is the function which will print the area using len and hgt
        """
        return f'Area is {(self.length * self.height)}'


rect1 = Rectangle(158, 7)
print(rect1.GetArea())
