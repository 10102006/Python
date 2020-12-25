
'''
       #Summary goes here

Defination:
    Conditions are the method which will only run under a certain circumstance otherwise the code will be skipped
    Condition have some extensions these are the alternative of skipping the code

Syntax:
    1. First is the main if statement this is the first code which will run
    2. Then there is the condition which will be tested by the code if the condition is true then the code given will run
    3. The main execution code which will be executed once the condition is true
    4. The if statement can end there only if the identation is changed

Exetension:
    1. Elif =>
                This method has to be in the same indentation of the the if which we want to add the extension
                This code will run if the if(main) statement is false and this condition is true
    2. Else => 
                This should be the last extension of the if(main) statement
                This code will be the alternative of the skipping the code meaning if the code in if(main) and elif are false then this will run

'''


num1 = 5
num2 = 20

num3 = int(input("Guess if your number is greater: "))


# Here I used If statement
if num3 > num2:
    print("Your number is Greater than num2")
# Here I used Else if function
elif num3 == num2:
    print("Your number is Equals to num2")
# Here I used Else function
else:
    print("Your number is Lesser than num2")

# ! Here are some ternary conditional operators
# ! Also known as shorthand operators
print('your num great') if 4 < 5 else print('num less bro')

# Here I used the LIST check function
list1 = [10, 21, 19]
print("Guess if your number is in the list")
num4 = int(input())

if num4 in list1:
    print("Your number is in list!")
else:
    print("Your number is not in list!")
    print("Try again!")
    num5 = int(input())
    if num5 in list1:
        print("Your number is in list")
    else:
        print("Sorry")
