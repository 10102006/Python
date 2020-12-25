'''
       #Summary goes here
In this I have learned about the string type variables
So I know that we have to use quotes to declare a string var

Also I have learned about string slicing :
1. [0 : 5] => This means that 012345(character of the string) will be returned

2. [: 5] => This means that 012345(of the string) will be returned beacuse
	 first empty means that it will be taken as 0

3. [5 :] => This means that 56789..end(character of the string) will be returned beacuse
	 second empty means that it will be taken as the len() of the string
	 
4. [0 : 10: 2] => This means that 0246810(of the string) will be returned beacuse
	 two colon means that it will be taken the alternate character the string chosen(0 : 10)

'''



str1 = 'this uses string function'
# This is a basic sentence
print(str1)
print('------------------------')

# To get the length of the string
print("Length of str1 is ", len(str1))
print("")

# In this I have included string slicing

# First character string
# In this no before colon is first character and after colon is the last minus one character

print(str1[0: 5])
print('------------------------')

# Default of the colons
# empty before colon is set zero
print(str1[:10])
print("")

# Empty after colon is set length of string
print(str1[5:])
print('------------------------')

# This is Advanced string slicing

# In this I can print alternate letter
# Empty colon means full string
# Double colon means alternate start
print(str1[::2])

