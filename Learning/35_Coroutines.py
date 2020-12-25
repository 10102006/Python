'''
    #Summary
    
Defination:
      Coroutines are the code which on initialising this takes time but when we re-run it again then that the same long initialising will run again

Syntax:
      1. 

'''

# @ Defining


def PasswordCoroutine():
    """
      This is a coroutine function first the long initialising will run then the searching will begin
    """
    # * This code is like initialising
    import time
    password = '10102006'
    print('Initialising.......')

    time.sleep(3)
    # * Above code will wait for 3 seconds

    # ! This is the main searching code that is the coroutine
    while True:
        givenPassword = (yield)

        if givenPassword == password:
            print('Your password is correct bro!')
        else:
            print('Sorry bro wrong!')



# ? Execution
if __name__ == '__main__':
    # ! To define a coroutine we need to make it as a varaible
    passwordmanager = PasswordCoroutine()

    # * This is Initialising of the coroutine so this will take time
    next(passwordmanager)

    # ? From here we can run the coroutine without the initialising

    # * This will send the coroutine the password to check
    input('Press enter: ')
    passwordmanager.send('1010200')

    # ? The initialising will end here so the coroutine will stop here
    # ! This will close the coroutine

    input('Press enter: ')
    passwordmanager.close()

    try:
        passwordmanager.send('10102006')
    except Exception as e:
        print('Sorry the coroutine stopped!')
