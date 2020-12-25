'''
    # Summary
In this we have to create a Library using class :
Tasks:

*Class
=> in the constructor we define a library()
      with:
      1. publisher name
      2. library name

1. Add book function
=> take two param :
      1. Library name => (it will check if the library name is taken or not)
      2. Book name to add => this can be as a list (This param of th constructor will be optional if we only want to create a library)

2. Display book function (Returns a book)
=> this will display the info of the book:
      like:
      1. Book name
      2. Author name(Optional)
      3. Publisher name of the book
      5. Date published library
      6. Info of the lenders (if any)

=> take two param:
      1. Library name => (this function will only work if the library is defined)
      2. Book name

3. Lend a book function
=> this function will provide the lender with the copy of the book
=> this function will also assign the date of return

=> Take two param
      1. lender name

=> Will return
      1. The book and (will activate the assign-date function)

'''
# * Imports
from Pr_OOPS_Login import SignupManager

signup = SignupManager()
signup.ChangeDatabase(
    'C:/Users/udit kumar\Desktop\Coding & Bowsers\Python Codes\Object oriented programming\Library\Database')
signup.IntialiseDatabase()

# @ Defining


class Library():
    """
    This the main class where all the books and perons will be stored
    things which will be stored:
          1. Library instances
          2. Books in those libraries
          3. Publishers, Lenders names

    This is the tree scematics of the library
      DATABASE{
          library_name:
          {
              Publisher_Info :
              {
                    name : *
                    age : *optional*
                    profession : *optional*
                    other : *optional*
              },
                  Books_Added :
                  {
                        Book:
                        {
                           name : *,
                           publisher: *,
                           copy : *pdf*
                        }

                        **Other books**
                  },
                  Books_Lended :
                  {
                        Book_Name : Lender_Name,
                  }
          },

          ** Other lib based on above **
      }
    """
    Database = {}
    UserStats = {
        'id': '',
        'password': ''
    }

    def __init__(self, p_name, p_age='Unknown', p_job=''):
        '''
        This is the ctor class which will make libraries and store it in a dictinary
        '''
        self.p_name = p_name.lower()
        self.p_age = p_age
        self.p_job = p_job.lower()

    def Make_NewLibrary(self, lib_name):
        """
        This function will make the a library inside the publisers data
        """
        self.Database.update({
            lib_name: {
                'Publisher_Info': {
                    'Name': f'{self.p_name}',
                    'Age': f'{self.p_age} years',
                    'Job': f'{self.p_job}',
                },
                'Books_Added': {},
                'Books_Lended': {},
            }
        }
        )

    def Add_Book(self, libraryname, bookname, author='unknown'):
        """
        This function will search for the library and then add the book name in the added_books dictinary
        """
        database = self.Database.keys()
        for lib in database:
            if lib == libraryname:
                self.Database.get(lib).get('Books_Added').update(
                    {bookname: author})
                print(f'Your book {bookname} is saved at {libraryname}')

    def Get_Book(self, libraryname, bookname, AddedOrLended=2):
        """
        This function will print the info about the book searched
        """

        if self.Database.get(libraryname):
            if AddedOrLended == 1:
                database = self.Database.get(libraryname).get('Books_Lended')
                whatHasBeenAcessed = 'Lended books:'
            else:
                database = self.Database.get(libraryname).get('Books_Added')
                whatHasBeenAcessed = 'Added books:'

            for books in database.keys():
                if books == bookname:
                    book = database.get(books)
                    print(f'{whatHasBeenAcessed} {bookname} : publisher {book}')

    def Lend_Book(self, otherdatabase, selflibraryname, otherlibraryname, bookname):
        """
        This function will add a object in the lend dict
        and remove this book from database
        """
        if otherdatabase.Database.get(otherlibraryname):
            selfdatabase = self.Database.get(
                selflibraryname).get('Books_Added')

            selfdatabase.update(
                {
                    bookname: otherdatabase.p_name,
                }
            )
            print(f'Book {bookname} is lended to {otherdatabase.p_name}')

    def SetUserStats(self, ID, password):
        """
         This will set the library and password
        """
        self.UserStats.update({'id': f'{ID}'})

        self.UserStats.update({'password': f'{password}'})

        print('--------------------------------------------------------------------------------')
        print(self.UserStats)
        print('--------------------------------------------------------------------------------')


# # ? Execution
# lib1 = Library('Udit', 14, 'Student')
# lib2 = Library('Aryan', 13, 'Teacher')
# lib3 = Library('Deepak', 21, 'Librarian')

# if __name__ == '__main__':
#     lib1.Make_NewLibrary('lib1')
#     lib2.Make_NewLibrary('lib2')
#     lib3.Make_NewLibrary('lib3')
#   #! Main

#     lib1.Add_Book('lib1', 'Udit-bio', 'Karan')
#     lib2.Lend_Book(lib1, 'lib1', 'lib2', 'Udit-bio')

#     print('hello world my name is udit')
#     lib2.Get_Book('lib2', 'Udit-bio', 1)
#     lib2.SetUserStats(15, 1010)
#     print(lib2.Database.get('lib2'))
