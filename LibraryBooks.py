import datetime

class Book:
    def __init__(self, Title, Author, ISBN, DateAcquired):
        self._Title = Title
        self._Author = Author
        self._ISBN = ISBN
        self._DateAcquired = DateAcquired
        self._OnLoan = False
    
    def SetOnLoan(self):
        self._OnLoan = True
    
    def DisplayDetails(self):
        print(f'Title {self._Title}, Author {self._Author}, ISBN {self._ISBN}')
    
    def ReturnLoan(self):
        self._OnLoan = False
        