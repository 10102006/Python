'''
    #Summary

Defination:
      OS is a build in module abbreviation for operating system

Uses:
      1. getcwd() => This will return the directry we are working on currently
      2. chdir() => This is will change directory of the program
      3. listdir() => This method will get all the items in a specific directory that is given to it
      4. mkdir() => This method will make a folder in our current directory
      5. makedirs() => This will make directories and can also make tree folders
      6. rename() => This will rename the first param file to the second param name
      7. environ (*class) => This class important for getting, setting environment variables.
            1. get() => This will get the path with it's names
      8. path (*class) => This class will contain all the path, dir, file related methods
            1. join() => This is a proper way to make directory so we don't get the slashes wrong
            2. exists() => This is function which will check if the path/ directory exists or not
            3. isfile() => This will check if the path is given is a file or not
            4. isdir() => This will check if the path is a dir or not

'''
# * Importing
import os

# ! These are the classes we will use
from os import environ
from os import path

# ? Execution
if __name__ == '__main__':
    pass
# ! Use of getcwd()
    currentdirectory = os.getcwd()
    print(f'We are currently working in {currentdirectory}')
    print('--------------------------------------------------------------------------------')

# ! Use of chdir()
    os.chdir('C://')
    print(f'We have changed the directory to {os.getcwd()}')
    print('--------------------------------------------------------------------------------')

    os.chdir(currentdirectory)

# ! Use of listdir()
    print(os.listdir('C://'))
    print('--------------------------------------------------------------------------------')

# ! Use of mkdir() and makedirs()
    # * I am commenting this to not make folder uncomment to see
    # ? os.mkdir('Soldier prettify my folder')

    # * This will make folder info and another folder inside Info it will make udit folder
    # ? os.makedirs('Info/Udit')

# ! Here I am making a folder for a project in the projects folder
    os.chdir(
        'C://Users//udit kumar//Desktop//Coding & Bowsers//Python Codes//Projects')
    try:
        os.mkdir('Soldier Prettify My Folder')
        print('Folder made...')
    except Exception as exception:
        print('Folder is alredy made...')

    os.chdir(currentdirectory)

# ! Using environ class
    print('Path for node is', environ.get('node'))
    print('--------------------------------------------------------------------------------')

# ! Using path class
  # *  Here we are joining the C:// directory with /udit
    joinedpath = path.join('C://', '/udit')
    print(joinedpath)
    print('--------------------------------------------------------------------------------')

  # * Here we are checking teh existence of Projects folder
    if path.exists(path.join(currentdirectory, 'Projects')):
        print('Yes the folder exists')
    else:
        print('Folder does not exists or error')
    print('--------------------------------------------------------------------------------')

  # * I will check if the path is file or not
    isfile = path.isfile(
        'C://Users//udit kumar//Desktop//Coding & Bowsers//Python Codes//Projects//2_Javis.py')
    print(f'Jarvis is a file {isfile}')
    print('--------------------------------------------------------------------------------')

  # * Here I am checking if there is a path for node
    isdir = path.isdir(environ.get('node'))
    print(f'There is a node path {isdir}')
    print('--------------------------------------------------------------------------------')
