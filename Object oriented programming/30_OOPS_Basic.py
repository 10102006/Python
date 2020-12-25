# BTW OOPS means object-oreinted-programming
# OOP uses DRY concept (Don't not repeat yourself)

# This is my first class of python

# Defining a Class


class Student:
    """
    This is a class for students
    """
    pass

# Executing Class


# Making an Instance
Udit = Student()
Aryan = Student()

# Accessing the variable of Instance
Udit.classStudyingIn = 9
Aryan.classStudyingIn = 9

Udit.section = 'a'
Aryan.section = 'c'

print(Udit, Aryan)
print('-----------------------------------------------')

print(Udit.classStudyingIn, Aryan.classStudyingIn)
print('-----------------------------------------------')

print(Udit.section, Aryan.section)
print('-----------------------------------------------')


class Teacher:
    """
    This is another class but diifrent thing will be inplied in this class
    """
    yearOfExperience = 0
    pass


Sun = Teacher()
Moon = Teacher()

Sun.age = 25
Moon.age = 30

Sun.income = 25000
Moon.income = 30100

# In this class I made a variable which is experience if experience of instance is not changed then the value will be default
print(f'Default years of experience is {Teacher.yearOfExperience}')
print('-----------------------------------------------')

# Here there will be the default value
print(f'Default value of Sun is{Sun.yearOfExperience}')
print('-----------------------------------------------')

# Here there will be the new value
Moon.yearOfExperience = 2
print(f'New value of Moon is{Moon.yearOfExperience}')
print('-----------------------------------------------')

# So this is the function that will be used to get the variable values of the instance of a certain class
print(Sun.__dict__)
print('See that there is no Experince here because we kept he defaut so there is no instance')
print('-----------------------------------------------')

print(Moon.__dict__)
print('-----------------------------------------------')


class Subjects():
    """
    In this class I will use methods/Functions
    """
    difficulty = 50
    fun = 50

    def Docs(self):
        """
        So this is the first Function of this class
        This self means that this function will only perform for the instance
        """
        return f'This Subject {self.difficulty} hard, and this much fun is there {self.fun}'
    pass


Maths = Subjects()
Hindi = Subjects()

Maths.difficulty = 90
Hindi.difficulty = 70

Maths.fun = 40
Hindi.fun = 70

print(Maths.Docs())
print('----------------------------')

print(Hindi.Docs())
print('----------------------------')

# This is the fourth Class
# Here I have used Contructor


class Books:
    """
    This is a constructor beacuse
    I will use param to initialise the variables
    """

    def __init__(self, bookOwner, bookName):
        """
        So this functions makes a class a constructor
        """
        self.owner = bookOwner
        self.name = bookName
    pass


Elon_Musk = Books('Udit', 'Elon Musk')
Rashtriya_Millitary = Books('School', 'Rashtriya_Millitary')

print(Elon_Musk.__dict__, "|||", Rashtriya_Millitary.__dict__)
print('-----------------------------------------------')

# Here I have Used Staic Method


class Marksheet:
    """
    Here I think I will use Staic methods somehow
    To make a function a static we use @staticmethod
    If we don't make a normal function statc the an addtional agrument will be given that is self
    """

    @staticmethod
    def AddFunc(num1, num2):
        return num1 + num2


UditMrk = Marksheet()
UditMrk.marks = 10

print(f'Marks of Udit is {UditMrk.AddFunc(10, 5)}')


# Abstraction and Encapsulation
"""
1. Abstaction means that the methods and variables of class are shortened
2. Encapsulation means that the methods of the class are hidden and are used just for functionality
"""


# Inheritance
"""
This is so simple you first have to make a parent class
then create the children class you want to inherit from parent then put the parent name in the parentesis hence
the children will inherit every thing from the parent including the constructor
"""


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

    def AreaPerRoom(self):
        if self.areaCovered != '' and self.rooms != '':
            print(f'Area of Per room is {self.areaCovered / self.rooms} sq. m')


class RentHouses(Houses):
    """
    This is another class but the diffrence is that I also nees the variables of house also
    so I will use inheritance to make this class a children of house class
    """

    def RentToBePaid(self):
        """
        This function is made so that I can use some function inside the Rent class
        """
        print(f'Rent to be paid is $ {self.rentPaid}')


# So here I have two parent instance
UditHome = Houses('Pune', 1000, 5)
AryanHome = Houses('Mumbai', 3000, 8)

# Here I will use a parent function
AryanHome.AreaPerRoom()
print('-----------------------------------------------')

# Here I have made a child Instance
YachnaHome = RentHouses('Raipur', 400, 2)

# Here I have change a child variable
YachnaHome.rentPaid = 8000

# Here I have used a child function
YachnaHome.RentToBePaid()
print('-----------------------------------------------')

# Here I have used a parent function
YachnaHome.AreaPerRoom()
