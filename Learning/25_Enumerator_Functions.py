'''
       #Summary goes here
       
Defination:
      1. Enumerator are like iterators but I know use of this only in for loop
         This is useful if we need to sort a contaner var with the index of the item   

Syntax:
      1. Make to variable in the for loop first for the iterator and second for the item var
      2. Inclose the list inside the enumerate() method to specify that we are using enumerator
      3. Do what you want to do with the iterator in the for loop like make the index or if statement

'''

# ! This is use of enumeration in without enumerate
list1 = ["To buy", "Not to buy", 'To buy', 'Not to buy']

# * Making an iterator manually an assigning its value
i = 1
for item in list1:

    # * Doing operation with that iterator
    if i % 2 != 0:
        print(f'We have to buy {item} {i}')

    # * We have to manually increase or decrease its value in the for loop
    i += 1
print('-----------------------------------------------')

# ! This is the using iterators with enumerate method

# * j is iterator
for j, item2 in enumerate(list1):

    # * Performing operations with that iterator
    if j % 2 == 0:
        print(f'By enumeratorFunctions have to buy {item2} {j}')
    # * At the end the iterator j will increase automatically
