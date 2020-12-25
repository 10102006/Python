'''
       #Summary goes here
       
Defination:
      Map is a method in the list class
      This method Iterate through a list items then it will perform a function
      on each of those item that is given to this method

Synatx:
      1. List => You have to specify that we are using list class
      2. map() => Map is the method we will be using
            2.1 This param will contain the function that the map will perform on all the items
            2.2 This is name of the list whose item will be altered
            2.3 This is not override so we need to store this in a variable

Usages:
      1. Easy to perform a function on all list item quickly
      2. Synatx is easy this is a pro move.
       
'''

# @ Defining list whose items will altered
lst = ['21', '19', '13', '10']

# * Printing that list for confirmation
print('Without map function')
print(lst)

print('-----------------------------------------------')

# ! Here I have used int() method to make all the items of the lst into int
mapedlist = list(map(int, lst))
# * int function makes the string, float into an int

# * Printing the container var
print('With map function using int()')
print(mapedlist)
print('-----------------------------------------------')


# ! Here I am using a lambda function about which I have learned
squareOfNum = list(map(lambda n: n**2, mapedlist))
# * This labda will take param (n => item of the list) then squaring it
# * We can make a seperate function to do this instead of lambda but this is i=the pro move

print(lst)
print(f"{squareOfNum} => These are the squared values of above list!")
