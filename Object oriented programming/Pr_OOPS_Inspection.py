'''
    #Summary
So this is the program where I have to use a module inspect

Tasks:
1. Use the Module to gather the information about a certain class
** Make this into a function **
1_1. Atributes
1_2. Class variables
1_3. Instance variables

2. Make a function which will take this junk and return a f-string
3. Print That f-string
'''
# * This is the module I have learned about in 36 File
import inspect

# @ Defining


class Houses:
    """
    This is a class in which I will use Inheritance
    """

    def __init__(self, location, areaCovered, numberOfRooms):
        """
        So this functions makes a class a constructor
        """
        self.location = location
        self.areaCovered = areaCovered
        self.rooms = numberOfRooms

    floors = 4

    def AreaPerRoom(self):
        if self.areaCovered != '' and self.rooms != '':
            print(f'Area of Per room is {self.areaCovered / self.rooms} sq. m')


def GetInstanceVariables():
    """
    This is the method which will only return the variables of the House class
    """
    variablesOfInstanceClass = vars(mulan)
    print(variablesOfInstanceClass)


def GetClassVariables():
    """
    This is the method which will only return the variables of the House class
    """
    variablesOfHouseClass = vars(House)
#     if '' in variablesOfHouseClass:
    print(variablesOfHouseClass)


# ? Execution
mulan = Houses('Pune', 15000, 10)

GetInstanceVariables()
GetClassVariables()
# print(inspect.getmembers(mulan))
# if __name__ == '__main--':
