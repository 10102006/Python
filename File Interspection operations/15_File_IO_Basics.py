'''
       #Summary goes here

This is file where I have learned how we can make file and edit them inside our python code

Uses:
      1. Open files => This is basics for file io we need to open some file to edit that we can open the file in a certain mode to do more stuff
      2. Close files => We must close the file if we open it this is to save memory do this after all the things have been done
      3. Write files => We can write file using python but we need the write mode enabled
      4. Read files => We can read the content of the files but the file must be open with the read type
      5. With function =>
                   This function is mostly used beacuse this function will open the file
                   Run the code inside it's indentation
                   Then this will close the file so we don't need to close the file manually and the code related to that file is seperated.

File Modes:
      1. Read mode(r) = Open file for reading - default
      2. Write mode(w) = Open file for editing
      3. exclusive(x) creation = creates a file if no file of that name is there
      4. Append mode(a) = adding to the end of the file
      5. Text mode(t) = to view the file as a text - default
      6. Binary mode(b) = view the file in binary digit
       
'''


# @ How to open a file then close that file
file = open("First2.txt")
file.close()

# @ How to read files
file1 = open("First2.txt")

content = file1.read(30)
 # * The input is the number of character that should be read 
print(content)
print('-----------------------------------------------')

 # * This is the code to print the whole file content
for line in file1:
    print(line)
    
print('-----------------------------------------------')
 # * How to read the file line by line

file2 = open("Dummy_File.txt")

line1 = file2.readline() # ? First line of the file
line2 = file2.readline() # ? Second line of the file
line3 = file2.readline() # ? Third line of the file
print(line1)
print(line2)
print(line3)

file1.close()

print('-----------------------------------------------')

# @ Editting the files

# ! Writing in the files
 # * To write in the file we must open the files with w mode
 # * When we write file then we override its content into a new content
 # ! Writing can be also used to make file if the file is not made previously then the code will generate a file with the given name
file3 = open("Dummy_File2.txt", "w")

content = file1.write('Udit is a good boy \nAnd this is a dummy file \n')

file1.write('\n')
print('This many text elements are present :', content)
file1.close()

print('-----------------------------------------------')

# Append only addes at the end the of the file
file1 = open("Dummy_File2.txt", "a")
file1.write('Udit is a bad boy \nAnd this is a real file \n')
file1.write('\n')
file1.close()

# r+ Handles read and write both
file4 = open("Dummy_File2.txt", "r+")
# Here I have the read the file and printed it
content3 = file4.read()
print(content3)
print('')

# Here I have then Edited the File
file4.write('This is fake \nAnd this world is bad \n')

file4.close()
print('-----------------------------------------------')

# More Functions 

# Here I used TEll functions we use this to the position where we are
file4 = open("Dummy_File.txt", 'r')

print(file4.readline())
print(file4.tell())

# SEEK is the function where the position is reseted
print('')
print(file4.readline())
file4.seek(11)

file4.close()
print('-----------------------------------------------')

# Using Block to Open the file 

with open("Dummy_File.txt") as f4:
    a = f4.read(12)
    print(a)
