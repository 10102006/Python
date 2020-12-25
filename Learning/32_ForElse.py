'''
    #Summary
    
In this I have learned that we can use else with a forloop:

Uses:
      This is used when we have to use extra code, if the loop is fully run. But not to run this when the loop is breaked


This is the in which the for loop will work:
      1. else will only work only when the iterable object is over ****
      2. This will not work if the for loop ends with break statement ****

'''

# @ Defining
lis1 = ['udit', 'kumar', 'nishad']


def CheckForWord(itemname):
 # ? This is the functioning list we will be using
    list2 = ['yo', 'my', 'name', 'udit']

 # * For Loop statement
    for item in list2:

      # ! if the item is found then the loop will break saving processing and stopping the else because it is also breaked
        if item == itemname:
            print('Your word is present')
            break
   # ! See this will only work if the word is not because if the word is found then the loop will break thus breaking the else
    else:
      # @ thus this is the output if nothing is found
        print('Your word is not found')


# ? Execution
if __name__ == '__main__':

    # @ Explanation
    for item in lis1:
        print(item)

     # ! This is the condition that will make this else staement not run
        if item == 'n':
            # ? Because as I said break will also break the else
            break

   # ? This is the way using the else with for loop
    else:
        print('For loop ended properly')

    print('--------------------------------------------------------------------------------')
# ! Use of this else with for
   # * In this case the else will be called because this is not present in the list
    CheckForWord('u')

   # ! In this case the else will break because this is present in the list
    CheckForWord('yo')
