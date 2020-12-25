'''
       #Summary

Try and Exception is a very pro method of writing code

Defination:
      Try => 
            This is class(class is further to learn) which will first run the code inside it which we will give
            If the code runs properly then we the code will carry on 
            But if there is an error then the this code will be skipped and the code inside the exception will run
     Exception =>
            This class is additional to the try class when the code inside the try is faulty we can
            skip it to continue excuting the code.
            But we can use the exception to get what is wrong with the code this will be stored in a varible
       
'''


num1 = int(input("Enter numb1: "))
num2 = input("Enter numb2: ")

# ! Here this will not be executed if the sentence is wrong
try:
    print('Sum of your number is :',
          num1 + num2)

# ? e here is the description of the error causing the trouble
except Exception as e:
    print(e)
print('-----------------------------------------------')


print('')
print('This is line very important')
print('-----------------------------------------------')