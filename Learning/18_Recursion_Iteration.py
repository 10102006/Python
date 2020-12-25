'''
    #Summary

Definination:
	1. Iterative => Loop where we define a variable and assign its value the change it's values to get the desierd value
	2. Recursive => Repeating the same thing again an again and change some value till the desired value is met.

Uses:
	* I will mostly use Iterative

	Iterative => In this we call a function which is iterative and assign it the value that will increase or decrease
	Recursive => In this we make a function the call the same function until the requirement is met
'''


def Fatorials_Iterative(n):
    """
   		# Explaination

   	So first I have defined a variable fac = 1
   	Then inside a for loop I have defined a var (i) this (i) will increase with each iteration
    
    Then in each iteration fac is multiplied with (i)
    This will run till (i) is equal to (n)

    Then when the final value is defined then that number is returned
    """

    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


num = int(input('Enter your factorial number: '))

print('-----------------------------------------------')
print("Your answer with Iterative aproach :", Fatorials_Iterative(num))


def Fatorial_Recursive(n):
    """
    	# Explaination

    This function is a little difficult!
	First the (n) which is the param is checked if that is 1 then nothing will happen
	
	but if not then
	
	It will check if the (n - 1) is 1 if yes the it will (n) * (n - 1)
	But if not then it will keep reapting the function to which will (n - 1) 
	and then check if the n = 1 then it will stop 

    """
    if n == 1:
        return 1
    else:
        return n * Fatorial_Recursive(n - 1)


print('-----------------------------------------------')
print("Your answer with Recursive aproach :", Fatorial_Recursive(num))
