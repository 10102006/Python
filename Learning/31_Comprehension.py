'''
    # Summary
here I have learned about Comprehensions
This is is shorthand for:
      1. Getting the values within the a storage variable
      2. Using this we loop through the containerto get specific variables of that container

'''

# @ Defining

# * If we want to get all the numbers divisible by 3 till 100 we will use
# * This is the syntax for comprehension

# * We can use this comprehension for initialisizing to the list

list1 = [i for i in range(100)]

# * We can use this comprehension check for checking for the variable with condition
# ! If this condition is true then that variable will only be intialisized
list2 = [i for i in range(100) if i % 3 == 0]

# * We can also initialise this attributes to a dicitinary
# ! The syntax for this is:
dict1 = {
    i: f'items{i}'for i in range(26)
}

# * We can initialise only a certian attributes to a dicitinary
# ! So in this only certain variables will initialise
dict2 = {
    j: f'items{j}'for j in range(26) if j % 5 == 0
}

# * We can also reverse the items from this dictinary using this
# * I will make a new dictinary which will oposite of previous dict
# ! Here I will first take the items & values then I will set the items = value vise-virsa
dict3 = {value: key for key, value in dict2.items()}


# * This is set-comprehension this is almost like lis-dict
# ! With this only unique key value will only be returned

names = {name for name in [
    'nam1',
    'nam1',
    'nam2',
    'nam2',
    'nam1',
]
}

# * This is comprehension for Generators
# ! Recap generator will only return the value one time when asked
odds = (i for i in range(50) if i % 2 != 0)
# ! since this is a generator we have to use __next__()
# ! To iterate through the variable

# ? Execution
if __name__ == '__main__':
    print(list1)
    print('--------------------------------------------------------------------------------')

    print(list2)
    print('--------------------------------------------------------------------------------')

    print(dict1)
    print('--------------------------------------------------------------------------------')

    print(dict2)
    print('--------------------------------------------------------------------------------')

    print(dict3)
    print('--------------------------------------------------------------------------------')

    print(names)
    print('--------------------------------------------------------------------------------')

    print(odds.__next__())
    print('--------------------------------------------------------------------------------')


# @ QUIZ
'''
Task:
      1. Take input for type(First)
      2. Amount of the items
      3. Type of the container (list, dict or set)
'''


def ComprehensionMaker():
    type = int(
        input('What type of container would you like [1:(list), 2:(dict)]: \n'))

    firstName = input('What should be the place holder:\n')
    amtOfItems = int(input('What should be the amount of items:\n')) + 1
    if type == 1:

        result = [f'{firstName}.{item}' for item in range(amtOfItems)]
    elif type == 2:

        result = {
            item: f'{item}' for item in range(amtOfItems)
        }
    else:

        result = 'Sorry there is error'

    print(result)


if __name__ == "__main__":
    ComprehensionMaker()
