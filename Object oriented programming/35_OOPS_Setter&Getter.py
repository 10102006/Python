class Employee(object):
    """
    This is a basic employee class class
    """

    def __init__(self, fname, lname):
        '''
        This is the constructor of your class
        '''
        self.name = f'{fname}{lname}'
        self.email = f'{self.name}@gmail.com'

#! If we want to not use this as method then with this we can do that @property
    @property
    def Email(self):
        self.email = f'{self.name}@gmail.com'

# ! This is the SETTER read the doc-string
    @Email.setter
    def Email(self, string):
        """
        This is a setter if this is there and then I can't change the email because I have used the @ property
        """
        self.name = string.split('@')[0]
        print('Setting now...', self.name)

        self.email = f'{self.name}@gmail.com'

# ? Here I have used the above code

    @property
    def Explain(self):
        """
        This method will tell the employee name
        """
        print(f'Hello my name is {self.name}! And my email is {self.email}.')

# ? This is the deleter function
    @Email.deleter
    def Email(self):
        """
        This is a deleter for the email 
        We don't delete this but set the email none
        """
        self.email = f'{None} (Email is not present please set the email)'


udit = Employee('Udit', 'Kumar')
aryan = Employee('Aryan', 'Jagtap')

# ? Here I have implemented the above @property
# ? See I have not used the brackets
aryan.Explain

# ! Here I have called the setter
# ? This is the way we call the setters
aryan.Email = 'UditKumar'
print('-----------------------------------------------')
aryan.Explain

# ! Here I have called the deleter
# ? We have to use this del in front
del aryan.Email
print('-----------------------------------------------')
aryan.Explain

# ! Here I have called the setter
aryan.Email = 'MomNishad'
print('-----------------------------------------------')
aryan.Explain
