'''
    #Summary

JSON: Javascript object notation

Uses:
      JSON is used for storing and sharing data through web

Functions and Class:
      1. loads() => This function make a data into a json format then we can store this data in a variable
      *TASK 2. load() => 
      3. 

'''
# * Import
import json

# @ Defining

# ! This data will be parsed
Jsondata = '{"name":"Udit", "age": 14}'

# ? This will make the data into a json format or dici
parsedData = json.loads(Jsondata)

# ? Execution
if __name__ == '__main__':
    print('Normal data')
    print(Jsondata)

    print('-------------------------------------------------------------------------------')

    print('Parsed data!')
    print(parsedData)

    # ! When parse some json format data then it will work as a dict
    # @ Here I have got the value of name with the key value pair
    print(f'This is the name of the parsed data "{parsedData["name"]}"')
