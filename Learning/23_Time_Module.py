'''
       #Summary goes here

Defination:
      !This is not a defination but about time & datetime module
      1. Time : Module contains class that can calulate time and stuff related to that
      2. Datetime : This contains class to take care to stuff related to months, days and years.

Usages(These only some of the things that I knew at that time) :
      1. Time:
            1. time() => This will return the how to time has been passed after making of python** or something
            2. sleep() => This will freeze the program for the given number of time(seconds)
      2. Datetime:
            1. datetime => This class I have specially imported from the datetime module this contains all the functions
            2. now() => This will return all the information of the time we can also add extensions to this to include only some information
                  2.1 time() => This will only return olny the time of the now
                  2.2 date() => This will return all the date stuff like day:month:year or som format
                  2.3 Class that will return just one stuff are: day, month, year, hour etcetra.. 
'''


import time
from datetime import datetime

# ? Time Module
print('-----------------------------------------------')

# ! Using time() Method
# * Here I will use the time module to get the execution amount of the for loop

# @ This will store the time at the begining of the loop
initialtime = time.time()
for i in range(10):
    """
      This loop will run normally for 10 iteration
    """
    print(f'For loop Udit {i}')
finaltime = time.time()

# @ This will print subtract the time after the loop from the initial time to get the run this method can used with anything
print('The time required to perform the for loop is :', finaltime - initialtime)
print('-----------------------------------------------')

# * Here I will use the time module to get the execution amount of the while loop

k = 0

initial2 = time.time()
while k < 10:
    print(f'While loop Udit {k}')
    k += 1
finaltime = time.time()

print('The time required to perform the While loop is :', finaltime - initial2)
print('-----------------------------------------------')

# ! This is the function which will calculate the execution time of any function


def ReturnExecutionTime(FunctionToRun):
    """
      This function will calcualte the execution time of the function passed as an arguement
    """
    initialtime = time.time()
    FunctionToRun()
    finaltime = time.time()

    return finaltime - initialtime


# ! Code for getting the current tine with time module
localTime = time.asctime(time.localtime(time.time()))
print(localTime)


# ! There is another function for time
print('Time is stopped for 5 seconds......')
time.sleep(5)

# ? Datetime module

# ! This will also get the current time
# * But the things like the format will be different
# * Also we can get only certain info like date day or month

print(f' The total time info is : {datetime.now()}')

print('--------------------------------------------------------------------------------')
print(f' The time is : {datetime.now().time()}')
print(f' The date is : {datetime.now().date()}')
print(f' The month is : {datetime.now().month}')
