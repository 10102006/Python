'''
	#SUMMARY

Here are some more pro-stuffs

Stuffs:
	1. Sorting =>
			Make a function which will sort your list or dictinary
			And how to run this function on a list is given bellow
	2. Lambda =>
			Lambda are one-liner function this can be directly written were we want
			Lambda is useful when we need a function once and that is very short
'''

# @ Here is the Sorting function

def a_first(a):
     '''
        This function will return the second value of the list
     '''
     return a[1]

# @ Making a list to sort it
sortList = [[1, 4], [5, 6], [3, 11]]

# * Using the class sort to pass our function
# ! This will overwrite the list so be careful

sortList.sort(key=a_first)
print(sortList)
print('-----------------------------------------------')

# @ Here is the sorting function by Lambda

sortList.sort(key=lambda x: x[0])
print(sortList)
print('-----------------------------------------------')

# ! Another way to define lambda function
# Name of function is multiplyByTen
# x is the parameter
# Then 10 * x is the return value
multiplyByTen = lambda x: 10 * x
print(multiplyByTen(5))

print('-----------------------------------------------')