'''
       #Summary goes here

Really I don't what is the usage of *args ot **kwargs
 I have learned how to use them how use them if someone askes

In a normal arguement in a function we can't pass a list
So we use *(paramenterName) and **(KW Argument name)

One more convention with this is that these are optional

This is the previous method
       
'''



def func1(param1, param2, param3):
    print(
        f'First param is {param1}, Second param is {param2}, Third param is {param3}')


func1(12, 5, 'Udit')

# ! *args is used here

print('----------------------------------------------------')


def func2(*args1):

    for i in args1:
        print(i, end=' ')


lst = [12, 5, 'Udit\n-']
func2(*lst)

print('-----------------------------------------------')

# ! Here is the usage of **Kwargs
# ? **Kwrg is used for handling dictinary

forKw = {
    'Udit': 10,
    'Yachna': 25,
    'Mom': 3,
    'Dad': 9,
}


def func3(**kwargs):
    for j, d in kwargs.items():
        print(f'Birthday of {j} is on {d}')


func3(**forKw)
print('-----------------------------------------------')
