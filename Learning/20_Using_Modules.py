'''
       #Summary goes here

This file is teaching the most useful and important thing in python
That is modules

Defination:
      1. Modules =>
                   Modules are other file made by the python team which is useful difficult
                   These file are saved as a module so these can be assessed as a class from the desired file

Uses:
      1. Easy => Main reason to use is to make coding easy because difficult things that we might need is given in these module
      2. Reusabillity => These code is written in a way that it can be used for multiple of things not one
      3. Not to rewrite them => If we don't use these then we have to make these functions and classes again and those function will not be that good as modules

Syntax:
      1. We need (import) keyword to include the module in our code
      2. Then the name of the module
      **Optional**
      3. (as) keyword means the name of the var through which we will access the file code
      4. (from) keyword is used for specifing the place from which the module should be accesed
      4. (from) keyword is also used for importing only a specific class from the module file
      
'''

# import pandas => 1
import random as rd # => (as) will name the variable for use to (rd)
from datetime import datetime as dt # => (from) will import (datetime class) from (datetime) module (as) will rename it as dt

print(f'Time is {dt.time()}')
print('--------------------------------------------------------------------------------')

randNum = rd.randint(0, 15)

print('Your random number is: ', randNum)
print('-----------------------------------------------')

rand = rd.random() * 100
print('Your random float is: ', rand)
print('-----------------------------------------------')

lst = ['docTest', 'keyWord', 'calendar', 'timeIt', 'pwd']
print(rd.choice(lst))
print('-----------------------------------------------')


# @ TASK use any random 2 Modules and use the 2 functions of these modules

# ! These are function for getting the various varaible of the file

# * Learn about the variable in 17_Variable_Scope.py

# ? dir() => This will return all the variables of the current file as a dictinary
# ? globals() => This will return the global variables of the curt. file as a list
# ? locals() => This will return the local variables of the curt. file as a list
