class House:
    """
    This is a class in which I will use Inheritance
    """
# ? This is also a dunder method but Init

    def __init__(self, location, areaCovered, numberOfRooms):
        """
        So this functions makes a class a constructor
        """
        self.location = location
        self.areaCovered = areaCovered
        self.rooms = numberOfRooms

# * This is a basic function
    def AreaPerRoom(self):
        if self.areaCovered != '' and self.rooms != '':
            print(f'Area of Per room is {self.areaCovered / self.rooms} sq. m')

# ? This is a Dunder add Method
    def __add__(self, other):
        """
        This is an add methods
        """
        return self.areaCovered + other.areaCovered

    def Details(self):
        """
        This is the functions returning the details
        """
        detail = f'Loaction of house is {self.location}, total area covered is {self.areaCovered} and the total number of rooms are {self.rooms}'
        return detail

# * This is the for getting information about the class
    def __repr__(self):
        return self.Details()

# * __str__ has more priority over the repr hence this will we displayed
    def __str__(self):
        """
        This has more priority over repr
        """
        return f'House: {self.location}, {self.areaCovered} sq m, {self.rooms} '

# ! This is the site for more dunder method
# * https://holycoders.com/python-dunder-special-methods/
# * https://docs.python.org/2.4/lib/operator-map.html

udit = House('Pune', 800, 4)
aryan = House('Mumbai', 2000, 10)

#! if ther is no dunder add method then this will be error

totalArea = udit + aryan
print('Combined area is ', totalArea)

print('-----------------------------------------------')

# ? Here This class will print str
print(udit)
print('-----------------------------------------------')

# ? Here the class will print repr because I have called
print(repr(aryan))
