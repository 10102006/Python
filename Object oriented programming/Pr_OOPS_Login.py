'''
    # Summary

This file will contain a class which will contain all the functions
And intialisation for the sign up

Tasks:
      1. Make a sign up system
            => This will take the username, email and password
            => Generate a folder with the username
            => Generate a file to contain the password and email so that we can check in it later

      2. Make a login system
            => This will check for the folder with the username
            => Then read the password and email file in that folder
            => Then this will allow or deny the request

      3. Integrate in such a manner that this file can be used at other places
            =>

'''

# * Imports
import os

# @ Defining


class SignupManager():
    """
          Function in this class

          1. InitialiseInfo() => This will ask the user for the info so that it can intialise this info
          2. IntialiseDatabase() =>
            This will intialise the database if the data is given
            If not then then this will ask for the inialisation
    """

    def __init__(self):
        '''
        This is the constructor of your class
        '''
        self.databasePath = os.path.join(
            "C://Users//udit kumar//Desktop//Coding & Bowsers//Python Codes//Object oriented programming//Database Of Signups")
        os.chdir(self.databasePath)

    def ChangeDatabase(self, path):
        """
              This function will change the database path so that 
              folder can be created in that path
        """
        self.databasePath = path
        os.chdir(self.databasePath)

    def IntialiseInformation(self):
        """
          This is for initialsing the email and password
          in this class so that we can access it later
        """
        username = input('What would be your username: ')
        email = input('Enter your Email: ')
        password = input('Enter your Password: ')

        self.username = username
        self.email = email
        self.password = password

    def IntialiseDatabase(self):
        """
          This function will make the folder with the username
          And store the password and email in a database file
        """

      # ! This will check if the any info is null then it will intialise
        try:
            self.username
            self.email
            self.password

        except:
            self.IntialiseInformation()

        finally:
            pass
         # ! This is the path of the user folder
            UserFolderPath = os.path.join(self.databasePath, self.username)

         # @ This will check is the user folder is taken or not
            try:
               # ! This will make the folder if not made
                os.mkdir(UserFolderPath)
         # * If yes then it will ask to change the info
            except:
                print('Username is taken....')
                self.IntialiseInformation()
                self.IntialiseDatabase()

         # ! This will make the database file
            # * This will change the directory to the folder path so we can make the files in that folder
            os.chdir(os.path.join(self.databasePath, self.username))

         # * This will make the database file with the info
            with open('database', 'w') as database:
                database.write(f'{self.email}\n')
                database.write(f'{self.password}')


class LoginManager(SignupManager):
    """
          This is the class for the login matters
          this will get the path From the SignupManager
    """
    pass
  # @ Here we are retriving the files from the database

    def RetrieveData(self):
        """
          This function will ask what is the username then
          Using this username this will return the password and email in a list
        """
        pass
      # ! This will ask whicj user name should be accessed
        username = input('Enter your user name: ')
      # * This will change the directory to that user name
        os.chdir(os.path.join(self.databasePath, username))

      # * This will open the database file of that user
        with open('database') as database:
            # @ This is getting the ifo with readlines
            email = database.readline()
            password = database.readline()

        # @ We are info in a list and then returning that list
            # ! I am slicing the string so we can subtract the \n
            info = [email[:(len(email) - 1)], password]
            return info


# ? Execution
if __name__ == '__main__':
    pass
    #     signup = SignupManager()
    #     signup.IntialiseDatabase()
    #     login = LoginManager()

    #     info = login.RetrieveData()

    #     print(info)
