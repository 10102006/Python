'''
    # Summary

Defination:
    Scope is a term we use to tell the variable state and where it is defined

Types of scope variable:
    1. Local variable => This refers to variable that is defined in a function or other instance this variable is only accessible from the function.
    2. Global varaible => This variable is defined in the main code so it is accessible from anywhere from the code this variable is able accessible to other variable

Uses of scope:
    1. Storing a variable reference which can't be changed globally but this will be stored.
    2. This is useful for storing variable whcih will we accessible from any where

Addition Method:
    1. Global => 
                The method is useful beacuse when we define a global variable can't change that global variables values local
                Thus to change the value of the global variable locally we have we have to use this  method
                This method can also make a global variable if the specified variable is not defined

'''

# ! Local var 
# Here pr is a is in local scope
# Means that lv will be only applicable in func1


def func1(lv):
    # lv is Local
    print('Local var lv = ', lv)


# ! Global var 
# Here gv is a global var so it is applicable to all
gv = 10  # Global


def func2():
    gv = 65  # It is Local
    #  This means that the Global var gv will not be change
    print('Local var gv = ', gv)


func1(15)
func2()
print('Global var gv = ', gv)
print('-----------------------------------------------')

# ! Global Keyword 
# Previous we saw that gv can't change inside a funciton
# So we use Global to change the global var
gv2 = 30


def func3():
    global gv2
    gv2 = 15


print('Before calling the func the global var is same', gv2)
func3()
print('After calling the func the global var has changed', gv2)
print('-----------------------------------------------')

# ! Here I used nested function

def ParFunc():
    dn = 7

    def ChildFunc():
      #   Here this Global will make a global var
        global dn
        dn = 15
    ChildFunc()
    print(dn)


ParFunc()
# After calling the func we had made a global var dn hence dn is printed
print(dn)
