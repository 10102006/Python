'''
       #Summary goes here

Dicinary is a another type of variable, which can store another variable with it's assocaites
The first value is the (key) and the second value is the (item)

I can also make the (key)s another dicinary or list

Some of the functions related to the dicinary are:
1. del => which can delete any (key) and repective (item) of the given dicinary variable
2. copy() => This function will make a copy of any dictinary and then we can assign it to another variable dictinary
3. get() => In this we will take the (key)(first element) as param and then it will return the (item)(second element of the (item))
4. update() => This is the function which we will use to add in any dictinary
5. (key)s() => This function will return all the (key)s or the first value
6. (item)s() => This will return all the (item)s the second values of the dictinary

'''


# Dictinary is a list with Curly Brackets
DictinaryOfUdit = {
    "Class": 9,
    "Language": "Hindi",
    "City": "Pune"
}
print(type(DictinaryOfUdit))

print(DictinaryOfUdit)
print("-------------------------------------------------")

# In this dictinary I will add more thing outside the dictinary
SecondDictinary = {
    "Udit": {"Password": 10102119, "PhoneNO": 1919456578},
    "Mom": 9975177395,
    "Dad": 8275244009
}
SecondDictinary["Yachna"] = 25092009
SecondDictinary["RMS"] = {"Password": 555511, "PhoneNO": 15151565}

# Use this function to delete an (item)
del SecondDictinary["Udit"]

print(SecondDictinary)
print("-------------------------------------------------")

# DICTINARY FUNCTIONS

# First function is copy function
D3 = SecondDictinary.copy()

del D3["RMS"]

print(D3)
print("-------------------------------------------------")

# Here I will use other functions

# Get
# Here we will get what is the value given to the following
print(D3.get("Mom"))
print("-------------------------------------------------")

# Update
D3.update({"Udit": "1010102119"})
print(D3)
print("-------------------------------------------------")

# (key)s
# Here we will get all the first values
print(D3.keys())
print("-------------------------------------------------")

# (item)s
# Here we will get the assigned values
print(D3.items())
print("-------------------------------------------------")
