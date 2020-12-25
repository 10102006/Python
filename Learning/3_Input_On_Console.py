"""
   # SUMMARY

This is mostly use for practice purpose***

As we can see that we can get an input from the user via console:
	1. The keyword used is input() => this will stop the console from running the program it will wait till it gets an output from the user
	2. This input by the user can be stored in program via variables
	3. Point to remember that this input by the user will be a string type
	4. So to store this as another type of variable we have to first covert that input as that type of variable 
	5. We can directly store this input as a desired variable by type method eg given bellow

"""
# @ defining
print("Enter your input no:")

# Here I Took The input and stored it in a var
myinput = input()

print("Enter your test no:")

# Here I Took The input and stored it in a var
mynumber = int(input())

# ? Execution
print(type(myinput))
print(type(mynumber))