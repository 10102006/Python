""" 
      #SUMMARY

Operators are basically the symbols and what is there meaning in python,
these operators are divide by the use of them.

This is all the types of operators in python:
      1. Arithematic Oprerators =>
                   As the name suggest operators for numbers like addition(+), subtraction(-) and extra like exponent(**) etc.
                   
      2. Assignment Operators =>
                   These are the operator used for assigining the value of certain variable like = for equatting this is very important
                   These also include operators where we are first using the Arithematic operators and also assigning that to a variable
                   
      3. Comparison Oprerators =>
                   These operators are meant for if statement when we compare something and do the work accordingly
                   These operators return bools if the statement with is true then true vis-virsa

      4. Logical Oprerators =>
                   This is an extension to the comparision operator because these are also addition conditions
                   But these are keywords not symbols which are used in other languages
                  
      5. Membership Oprerators =>
                   This is third an extension to the comparision operator because these are also addition conditions
                   But these are keywords used for check if the first variable is connected to the other variable
                  
      6. Bitwise Oprerators  =>
                   These are the operations used in the machine learning and binary conversation
                  
"""

# ! Arithematic operators

print('-------------------------------')
print('Arithematic operators')

num1 = 8
num2 = 3

# @ Self Explainatory 
print('num1 + num2 =', num1 + num2)
print('num1 - num2 =', num1 - num2)
print('num1 * num2 =', num1 * num2)
print('num1 / num2 =', num1 / num2)

# @ These are extra operations
print('num1 // num2 =', num1 // num2) # ? Here I will get approximate int value of dividing the variables
print('num1 ** num2 =', num1 ** num2) # ? Exponentitonal operator power
print('num1 % num2 =', num1 % num2) # ? Modules operator

# ! Assignment Operator 

print('-------------------------------')
print('Assignment Operator')

num3 = 20 # ?   This is used for assigning the value
print(num3)
num3 += 136 # ? This is used for int and float where the assigned the value is added to the variable then the obtained value is assigned to the variable
print(num3)
num3 -= 136 # ? This is used for int and float where the assigned the value is subtracted from the variable then the obtained value is assigned to the variable
print(num3)
num3 *= 136 # ? Here the variable is multiplied by the assigned number then that is stored in the variable
print(num3)

# ! Comparison operators 

print('-------------------------------')
print('Comparison operators')

num4 = 34

# ! Excalmation can be used to make the statement opposite of its current state
print('Is num4 = 5,', num4 == 5) # ?  This will check if, first item is same as or equal to second item.
print('Is num4 < 5,', num4 < 5) # ?   This will check if, first item is greater second item.
print('Is num4 > 5,', num4 > 5) # ?   This will check if, first item is less second item.
print('Is num4 <= 5,', num4 <= 5) # ? This will check if, first item is less or equal second item.
print('Is num4 >= 5,', num4 >= 5) # ? This will check if, first item is greater or equal second item.
print('Is num4 != 5,', num4 != 5) # ? This will check if, first item is not equal second item.

# ! Logical operators 

print('-------------------------------')
print('Logical operators')

t = True  # ! assume as +
f = False  # ! assume as -

# @ This can be also used as this var1 == 1 and var2 == 2 (This means that the output will be true only when the both are true)
print(t and f) # ?            (+) + (-) = false(-) 

# @ This can be also used as this var1 == 1 or var2 == 2 (This means that the output will be true if any one is true)
print(t or f) # ?             (+) - (-) = true(+) 

# @ This also means != in the above one This is for less symbol user
print(num1 is not num2) # ?   (+) - (-) = true(+) 

# @ This means == as above This is also for less symbols user
print(num3 is num4) # ?       (+) + (-) = false(-) 

# ! Membership operators

print('-------------------------------')
print('Membership operators')

AList = [0, 1, 2, 3, 4, 5, 6]
print(0 in AList) # ?      This will check if the first value is in the given storage variable
print(10 not in AList) # ? This will check if the first value is not in the given storage variable

# ! Bitwise operators

print('-------------------------------')
print('Bitwise operators')

# @ Binary numbes
"""
0 = 00
1 = 01
2 = 10
3 = 11
"""

print(1 & 2) # and
print(2 | 11) # or
