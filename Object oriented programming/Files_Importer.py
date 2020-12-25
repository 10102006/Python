'''
    #Summary

This file is very important so that I can use my python files as module

Tasks:
      1. This will be present in all the main parent folder
      2. This will make a seperate folder in all of those parent folder
      3. This folder will contain the files which we have to import
      4. Then in the importing file we will copy the file in that folder

'''
# * Imports
import os

currentdirectory = os.path.join(os.getcwd(), 'Object oriented programming')

# @ Defining


def CopyFile(foldername, filename):
    """
      This method will first open the file in the specified folder
      Then copy the file in the imports folder
    """
#     try:
#         os.mkdir(os.path.join(currentdirectory, 'Imports'))
#     except:
#         pass
    os.chdir(os.path.join(os.getcwd(), foldername + filename))
    print(os.path.join(os.getcwd(), foldername + filename))


# ? Execution
if __name__ == '__main__':
    CopyFile(1, 1)
