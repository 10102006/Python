'''
       #Summary goes here

For loop is used for looping through an iterator 
and increasing the iterator each itreration.

Things that can be done with for loops:
      1. Looping through list for print each of the list items
      2. Looping through list but using the iterator to check if the iterator is the desired item
      3. Looping through list but using two iterators
      4. We can also loop through a string also two get and check them with an if statement

'''

# ! FOR IN LOOP

list1 = [10, 21, 19, 6]
list2 = [["Udit", 10], ["Dad", 21], ["Mom", 19], ["Yachna", 6]]

# @ Basic loop
for item in list1:
    # * This will print each of the list items, following is the way how it works
    # * First the iterator item will be 0 and then each time the iterator is increased by one
    print(item)

# @ Using iterators with the if statement
for item in list2:
    # ? This will do the same as above just one thing it will check if the item is same then it will print that item
    if item == ["Udit", 10]:
        print(item)


# @ Here I will use two var for getting the second list elment
for name, age in list2:
    # ? In this two iterator will be iterated except one
    if age > 20:
        print("Age of", name, "is", age)


# @ Using dictinary with Loop
dict1 = dict(list2)
print("Family menbers are: ")

for item in dict1:
    # ? Because of this we know that we can also iterate through dictinary also
    print(item)

# @ For using Two var you need to use item() to dict1
for name, age in dict1.items():
    # ! But the thing is that if we have to use two iterator with dictinary we have to use item()
    print(name, "is", age, "years old")

# ? QUIZ
# ? Only get the number then the greater less than 6

list3 = ["Udit", 10, 5.5, "Kumar", 19, 2]

for item in list3:
    '''
        1. Here I have first typecasted all the elements of the list3 in string
        2. Then using the isNumeric() function to check if the string is number
        3. After this I am also checking if the item is less than 6 (As asked)
    '''
    if str(item).isnumeric() and item > 6:
        print(item)
