'''
       #Summary goes here

Defination:
      Joining means appending the string and list I think

Syntax:
      1. Defining => Define a varible that will contain the joined string
      2. Join() => Use the (.) after the string that you want to connect the list items to

Usage:
      1. Easy fofr joining the item with a string with a simple syntax

'''


# Here I have learned about joined functions

# If we have to print all the element of this list in one line the this is the previous method
lst = ['Udit', 'Mom', 'Dad', 'Yachna', ]

for it in lst:
    print(f'{it} and', end=' ')

print('and other family members')
print('-----------------------------------------------')

# This is using the joined function
# First name a list, then write the other joining in the string

fam = ' and '.join(lst)

print(fam)
print('-----------------------------------------------')

dict = {
    'Udit': 'Kumar',
    'Yachna': 'Nishad'
}

name = 'Name :'.join(dict)
print(name)



