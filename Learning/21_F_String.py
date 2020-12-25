'''
       #Summary goes here

Defination:
      F-String are speacil string type where we can store a variable inside the string
      We can store variable in a string with string concatination but that is not effcient so we use f-strings to concatinate the string with an object

Syntax:
      1. Defining => To define a f-string we need to put f in front of a string
      2. Including var => To include any variable we need to include that variable in side curly brackets

'''

# ? String Concatination
var1 = "Udit"
concatinatedString = 'This is %s' % var1

print(concatinatedString)
print('-----------------------------------------------')


# @ F-Strings usage
var2 = 15
fstring = f"{var1}'s' favourite number is {var2}"

print(fstring)
print('-----------------------------------------------')
