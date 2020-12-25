'''
    #Summary

In this we will use functools module this module came with the python3 as decorator
In this we will be caching function (cache)

Uses:
      Caching means that we are skipping the same function,
      and storing them as a cache, only some amount of cache can be stored which we have to specify
      this means that those numnber of same function will be stored then the after same function will be called

      We can use this decorator to stop some repeated functions. For some amount of cache,
      then that function will be called again
'''

# * Imports
import time
from functools import lru_cache

# @ Defining

@ lru_cache(maxsize=2)
def BasicFunction(waittime):
    '''
    This is a basic function which will first wait for waittime
    Then print the time
    '''
    print('Waiting.....')
    time.sleep(waittime)
    print('Go!')


# ? Execution
if __name__ == '__main__':
    BasicFunction(3)  # ! This function will be called
    print('--------------------------------------------------------------------------------')

    BasicFunction(3)  # ? This function will be skipped
    print('--------------------------------------------------------------------------------')
    BasicFunction(3)  # ? This function will be skipped
    print('--------------------------------------------------------------------------------')

    BasicFunction(2)  # ! This function will be called
    print('--------------------------------------------------------------------------------')

    BasicFunction(3)  # ? This function will be skipped
    print('--------------------------------------------------------------------------------')
    BasicFunction(3)  # ? This function will be skipped
    print('--------------------------------------------------------------------------------')
