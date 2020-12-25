'''
       #Summary goes here
Introspection means to get the information about the class speacfied
Most of the things in python is object

There are two ways to get information:
1. type({NameOfClass}) => this will tell what is the type of the class eg: string, int, float etc.
2. id({NameOfClass}) => this will return a specifc set of number through which the computer recognises it
3. dir({NameOfClass}) => this will return a  list of all the function we can perform with that class

'''

# *  This is the module required for the inspection
import inspect


class Student:
    """
    This is a Class which will have student varaibles.

     Funtions are :
     1. Constructor
     2. StudentBio() prints the values in the class
    """
# * Constructor

    def __init__(self, nameofstudent, rollnumber, classstudyingin):
        '''
        This is the constructor of your class
        '''
        self.rollNumber = rollnumber
        self.name = nameofstudent
        self.classStudyingIn = classstudyingin
        pass

# ? A basic function printing the bio data
    def StudentBio(self):
        """
        This is a basic funciton for student
        """
        print(
            f'My name {self.name}. I am studing in class {self.classStudyingIn} and my roll number is {self.rollNumber}')


if __name__ == "__main__":
    aryan = Student("Aryan", 4, 8)
    aryan.StudentBio()
    print('--------------------------------------------------------------------------------')
    print('The type is', type(aryan))
    print('--------------------------------------------------------------------------------')
    print('Id is ', id(aryan))
    print('--------------------------------------------------------------------------------')
    print(dir(aryan))
    print('--------------------------------------------------------------------------------')

# @ Here I have used the inspect module to get member of the class
    print(inspect.getmembers(aryan))
