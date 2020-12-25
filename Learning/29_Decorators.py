'''
      **Summary**

Decorator is a type of class which is used for cleaning up a function or decorating it.

Two ways to use a decorator is following:
  *** Make a function which takes an arguement function. Format the param function inside that main function.(decorator)
  *** Make another function which needs to decorated. (decoratee)

  1. In this way call the decorator and put the decoratee as the param.
  2. In this way before making the decoratee put ( @Decorator_name ) above it.

'''


def Function1():
    print('Hi there')


Function2 = Function1  # * Here I am just assigning a variable to this above function

# ? This (del) class is used to delete any function inside the code
del Function1

Function2()
print('-----------------------------------------------')


def FunctionReturn(num):
    '''
      In this function I am returning a print and int respectively
      as of the param this print and int are class 
    '''
    if(num == 0):
        return print  # ? This is the print class
    elif(num == 1):
        return int  # ? This is the int class


AssignedClass = FunctionReturn(0)
print(AssignedClass)
print('-----------------------------------------------')


def ExecuteFunction(func):
    """
      This function will execute the function given to it as a parameter
      also we can pass function as a parameter
    """
    func('I print class this function was given as parameter')


ExecuteFunction(AssignedClass)
print('-----------------------------------------------')

# ! THE CONCEPT OF DECORATORS


# @ This is the Decorator function
def DecoratorFunction(func1):
    """
        In this function I have first defined a function NowExecute()
        Then I have called the function in this
    """
    def NowExecute():
        print('* * * * * * * * * *')
        func1()
        print('* * * * * * * * * *')

    NowExecute()


def SimpleFunction():
    print('10 + 15 = 25')


# * First way
SimpleFunction = DecoratorFunction(SimpleFunction)
print('-----------------------------------------------')


# * Second way
# ! Just add @DecoratorName

@DecoratorFunction
def SimpleFunc2():
    print('Udit is a good boys')
