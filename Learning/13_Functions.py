'''
       #SUMMARY

Firstly Functions == Methods they mean the damn same thing!

Defination:
      Function/Method is a way to for storing some complex piece of code as a shortform
      which can be called as many time we want. With certain change that will be predefined by the author
      
Syntax:
      1. We the keyword def for defining the function
      2. Then comes the name of the shorthand that we will use to call this function
      3. We can then pass some variation we want in our code this is optional when we want the are called(Parameter/Arguement)
      4. The colon tell that the code is started
      5. Change the indentation of the code outside to exit the function
       
More features (Optional):
      1. Return => This means that we can given main code something we got from the method
                   Like in add() method we will return the sum
      2. Docstring => This is the summary of the method which we write inside the method 
                      This can displayed with a method methodname.__doc__() This will return the the docstring defined
                      This is very useful for big progect for quickly finding what the method does
                      
'''


num1 = int(input('num1 '))
num2 = int(input('num2 '))

# ? Return function
def ReturningAverageFunc(num1, num2):
    avrg = (num1 + num2) / 2
    return avrg
print(ReturningAverageFunc(num1, num2))

# ? Doctring function
def DocString():
    """ I made this function so that I learn how doc stings work """
    return
print(DocString.__doc__)


# ? Complex function which will print the given number of times
def Repeat(text, noTimes):
    i = 0
    while i <= noTimes:
        print(text)
        i += 1

Repeat('Hello world!', 2)
