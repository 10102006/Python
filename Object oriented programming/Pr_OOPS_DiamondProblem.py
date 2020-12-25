
#! This is a a famous problem which is
#! in Object orented programming because of multiple inheritence

class A:

    @staticmethod
    def Info():
        """
        This is a basic fucntion
        """
        print('This is class A')


class B(A):
    @staticmethod
    def Info():
        """
        This is a basic fucntion
        """
        print('This is class B')


class C(A):
    @staticmethod
    def Info():
        """
        This is a basic fucntion
        """
        print('This is class C')


class D(B, C):
    pass

# @ Execution
if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    d = D()

    d.Info()

'''
So here is the problem
If we change the orientation in the param of D then
output will be 'This is class C'
'''
