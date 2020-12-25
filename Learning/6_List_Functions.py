'''
       #Summary goes here

Here I have learned about list type of variable

There are two type of variables:
1. Pure => means that all the elements of the list are of same type
2. Mixed => means that the elemets are of different types

These are the different type of ways to get the list values:
1. Listname[(Any number)]  => means that the element of that index will be returned
2. Listname[0 : 3] => means that from first index to the other index all the element will be returned
3. Listname[0 : 4 : 2] => means that from first index to the other index all the alternate element will be returned

Other function in this class
1. append() => this adds your param to the end of the lisr
2. insert() => this takes two arg 1. index number of your param 2. your param
3. pop() => this deletes the end element of the lsit
4. remove() => this will check if your param is in the list and if yes then remove it

'''

# SEE ALL THE FUNCTIONS OF LIST ON GOOGLE

# This is my first list
# This is a mixed list
firstList = [0, 1.9, "YouDeITea"]
print(firstList)
print("-------------------------")

# In this I had printed only 1 part of list
print(firstList[0])
print("-------------------------")

# In this I used slicing like string slicing
# See there to see the functions
print(firstList[0:1])

print(firstList[::2])
print("-------------------------")

# From here I used the list functions
numbers = []
# Append adds to the end
numbers.append(10)
numbers.append(10)

# Insert takes two argument first index no, and second the value
numbers.insert(2, 15)

numbers.append(21)
numbers.append(19)

# Remove delete the value
numbers.remove(10)

# Pop deletes the last value of the list
numbers.pop()

print(numbers)
print("-------------------------")

# Now I have learned tuple
# There are to type of lists: mutable & immutable
# mutable meaning we can change them and in immutable we cannot change them
# list are mutable []
# tuple are immutable ()

tpL = [1, 2, 3]
tpL[0] = 5
print(tpL)
# Here the code is executable

tpT = (1, 2, 3)
# tpT[0] = 5
print(tpT)
# Here there will be be error so I have commented it out


# Here is the code to swap here value of variables
a = 10
b = 19
print("This value before swap :", a, b)

a, b = b, a
print("This value after swap :", a, b)
