'''
       #Summary

This is a file for the sequence for the previous file which was on for loops,
For loops can mostly be used for iteration of lists and dictinaries but,
The while loops can be used for a tons of stuff.

The while loop syntax explained:
      1. The while loop loop will have an arguement
      2. This arguement means for how long or till what should the code should run
      3. The code will run till the param given is proved false
      4. If the arguement is true the while loop will run forever

But the While loop also has certain function to ensure that the while loop is not run forever:
      1. Break => This will directly break out of the loop or the next code will be run
      2. Countinue => This is quite tricky this will not the run the current loop but the next loop will run
                      I mean the if this is given in an condition then the code after this inside the while loop will be skipped 
                      but in the next looping of the while loop is continue is not called then the code inside the while will run perfectly
                      
Uses of Break and Continue:
      1.(Break) => This can be used to break out of a loop when the loop is running like a forever loop
      2.(Continue) => This can used to leave to code from the begining but when the condition is met then the code will rerun                      
                      
** While loop can be also used as a for loop but in this we have to make our own iterator outside the loop
** and also increase or decrease the iterator over time

Forever loop can be used to make the program always active to respond to the user                      
                      
'''


i = 0

# This will loop till the condition is met
print('Normal while')
while(i < 21):
    print(i, end=" ")
    i = i + 1

print('')
print('---------------------------')

j = 0

# @ Here I have used Break statement
print('Break while')
while(True):
    print(j, end=' ')
    if j == 5:
        break
    j = j + 1

print('')
print('---------------------------')

n = 0
# @ Here I have used continue statement
print('Continue while')
while(True):
    n = n + 1

    if n < 5:
        continue
    print(n, end=' ')

    if n == 10:
        break


print('')
print('---------------------------')

# ? Quiz directions
# * Take input
# * If input if less than 100 ask again
# * If input is greater then print win

print('To start the game press enter')
enter = input()
num = int(input('Your number please: '))

while num < 100:
    print('Your input is incorrect!')
    print('')
    num = int(input('Try again: '))

print('Your answer is correct :)')
