'''
       #Summary goes here
Set another type of variable it is a type of dictinary but without any items

we can make a list and then assign that list as a set or object in js

Some function of in the sets:
1. add() => this will add and item to the set
2. remove() => will remove the param value from the set
3. union() => we use union to copy all the elements from one set 
4. intersection() => we use intersect to copy the element from one set
      execpt the similar element of that set will not be copied

'''


ThisIsSet = set()

print(type(ThisIsSet))
print("-----------------------")

l = [10, 25, 19, 21]
s = set(l)
print("Value of s is ", s)
print("-----------------------")

# To add something to set use Add function
s1 = set()
s1.add(1)
s1.add(2)
print("After adding value is ", s1)
print("-----------------------")

# To delete something to set use Remove function
s1.remove(1)
print("After removing value is ", s1)
print("-----------------------")

# To Copy something to set use Union function
s2 = s1.union({1, 2, 3})
print(s1, s2, "We used Union")
print("-----------------------")

# To Copy something to set but don't copy same item use Intersection function
s3 = s1.intersection({1, 2, 3})
print(s2, s3, "We used Intersection")
print("-----------------------")
