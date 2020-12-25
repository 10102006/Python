

class Student:
    """
    This is a Class which will have student varaibles
    """
# * Constructor

    def __init__(self, nameofstudent, rollnumber, classstudyingin):
        '''
        This is the constructor of your class
        '''
        self.rollNumber = rollnumber
        self.name = nameofstudent
        self.classStudyingIn = classstudyingin

# ? A basic function printing the bio data
    def StudentBio(self):
        """
        This is a basic funciton for student
        """
        return f'My name {self.name}. I am studing in class {self.classStudyingIn} and my roll number is {self.rollNumber}'


class Player:
    """
    This is another class which is related to student 
    and this is all related to student
    """
    gamePlaying = ''
# * constructor

    def __init__(self, name, gameplaying):
        '''
        This is the constructor of the player class
        '''
        self.name = name
        self.gamePlaying = gameplaying

# ? Functions
    def PlayerBio(self):
        """
        This is a basic funciton for player
        """
        return f'I am a {self.gamePlaying} player'
    pass


class CoolStudent(Student, Player):
    """
    This is the iherited class of student and player
    """

    def CoolBio(self):
        """
        This is the funciton which use both the functions of the above class
        """
        return (f'{self.StudentBio()} also {self.PlayerBio()}')

    pass


deepak = Student("Deepak", 15, 9)
aryan = Player("Aryan", "Football")

udit = CoolStudent("Udit", 5125, 9)

print(deepak.StudentBio(), aryan.PlayerBio())

print('-----------------------------------------------')

udit.gamePlaying = "Football"
udit.name = "Udit"
print(udit.CoolBio())

#! This is mulilevel inheritance


class GrandFather:
    """
    This is the top level of the inheritance
    """
    danceTimes = 0
    pass


class Dad(GrandFather):
    """
    This class is inheriting from gradfather class
    """
# ? Here I have made a function

    def Dance():
        print(f"Yes I like to dance {GrandFather.danceTimes}!")


class Son(Dad):
    """
    This class is inheriting from dad which is inheriting from grandfather class
    """
    danceTimes = Dad.danceTimes
# ? Here I have over written a function in the parent class

    def Dance():
        print(f'I dont like to dance {Dad.danceTimes}!')


# * Code execution
Udit = GrandFather
Aryan = Dad
Ellon = Son

Udit.danceTimes = 5

Aryan.Dance()
Ellon.Dance()

# * This is an example of Polymorphsis
# ? Polymorphsis simply means that we have changed the var type hence the output is changed

print('-----------------------------------------------')

print(10 + 5)
print('0' + '5')

#! Overwriting
print('-----------------------------------------------')

# * This is Variable overwriting


class A:
    # ? This is the first var
    #! This is var will ber inconsideration if there is no overwriting
    classvar1 = 'I am in class A'

# ? This is the constructor

    def __init__(self):
        '''
        This is the constructor of your class
        '''
        self.var1 = 'I am a inside As constructor'
      #   ! Here I have overwritten the classvar1
      #   ! Here classvar1  is an INSTANCE hence it is first priorty
        self.classvar1 = 'I am Instance of class A'
        pass


class B(A):
    """
    This is inheriting from A
    """
    #! Here if there is no INSTANCE var then this var wil be taken in consideration
    classvar1 = 'I am in class B'
    pass


a = A()
b = B()

print(b.classvar1)

# * Overwriting Methods
print('-----------------------------------------------')


class C:
    def __init__(self):
        '''
        This is the constructor of your class
        '''
        self.var1 = 'I am in C'
        self.var2 = '21'
        self.special = 'Special'
        pass
    pass


class D(C):
    def __init__(self):
        '''
        This is the constructor of your class
        '''
      #!   I can access the The init of the parent using SUPER
      #!   We can also use SUPER to call any other function of the Parent which is overwritten
      #!   If I don't do this then I can't Access the variables in the Parent
        super().__init__()

      #!   Here I have overwritten the init of the parent
        self.var1 = "I am in D"
        self.var2 = "19"
        pass
    pass


c = C()
d = D()

print(d.var1)
print(d.var2)

print('-----------------------------------------------')
print(d.special)
