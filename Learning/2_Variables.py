"""
   # SUMMARY

In this I have I learned about variables types

I can also get the  type of the variable in the console using type() method

Also I can change the variable type using the same type of methods like:
	int() => this can turn a float or string into an int given that the value of string in numeric
	string() => this can turn any thing into a string
	float() => this can a turn a int into a floating num and a string also

Apart from this I have also learned about variable CONCATINATION:
	1. Int concatination => using opreration(+, -, *, /) on two or more int vaiables
	2. Float concatination => same as about but with more accuracy in the division
	3. String concatination => in this we use operations on string mostly addition and multiplication
	   3.1 we can add two or more string variable or simple string to form one string
	   3.2 we can also add two or more type of variable to from a single string but we have to use the string() method to make them method first
	   3.3 lastly as I have learned we can also multiply string two get multiple string but the multiplying number must be a int or float


"""

# Defining a variable
var1 = "Udit"
var2 = "Kumar"
number1 = 10
num2 = 21.19

print("***********************")

# Printing a variable
print(var1, var2, number1, num2)

print("***********************")

# Concatinating
# This is a Number addition
print(number1 + num2)

# This is a String addition
print(var1 + var2)
print(var1 + number1)

print("***********************")

# Finding the Variable type
print(var1, "is", type(var1), end=" ")
print(var2, "is", type(var2))
print(number1, "is", type(number1), end=" ")
print(num2, "is", type(num2))

print("***********************")

# Changing the variable type
"""
    # The functions
str()
int()
float()
"""

# Variable type change

print(number1, " = ", type(float(number1)))
print("number1 which is an Integer has changed to float")

print("***********************")
