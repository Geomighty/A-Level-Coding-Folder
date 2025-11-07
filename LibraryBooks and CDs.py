import datetime

class Item:
    def __init__(self, Title, DateAcquired):
        self._Title = Title
        self._DateAcquired = DateAcquired
        self._OnLoan = False
    
    def SetTitle(self, NewTitle):
        self._Title = NewTitle
    
    def GetTitle(self):
        print(f'Title: {self._Title}')
    
    def SetDateAcquired(self, NewDate):
        self._DateAcquired = NewDate
    
    def GetDateAcquired(self):
        print(f'Date Acquired: {self._DateAcquired}')

    def SetLoan(self):
        self._OnLoan = True
    
    def ReturnLoan(self):
        self._OnLoan = False

    def GetLoanStatus(self):
        print(f'Loan Status: {self._OnLoan}')

class Book(Item):
    def __init__(self, Author, ISBN, Title, DateAcquired):
        super().__init__(Title, DateAcquired)
        self._Author = Author
        self._ISBN = ISBN
    
    def SetAuthor(self, NewAuthor):
        self.Author = NewAuthor