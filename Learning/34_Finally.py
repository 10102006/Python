'''
    #Summary
    
Ealier I have learned about the try and exception check that for more info
These also have more things to it

Defination:
      1. Finally => This will excute after all the code in the try will run
      2. Else => This code will run if the exception has not run then the code in this will run

Syntax:
      1. We need to use try to use these

'''

# ? Execution
if __name__ == '__main__':
    try:
        # ! This code will not run
        file1 = open('This file does not exist.txt')
    except Exception as e:
        # * This code will if there is an error
        print('This is the error')
        print(e)
    else:
        # ! This will not run because the code in the exception has run
        print('This code will run when is error is not there')
        print('There is no error')

        # ? This will close the file if the file will open with the try
        file1.close()
        pass
    finally:
        # * This code will run any way because this is useful for cleaning up the code
        print('This code will run.....')
