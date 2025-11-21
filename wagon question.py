class Wagon:
    def __init__ (self, owner_name):
        self.owner_name = owner_name
    
    def __str__ (self):
        return f'<Wagon: {self.owner_name}>'

class OpenWagon(Wagon):
    def __init__ (self):
        super().__init__(self.owner_name)

class ClosedWagon(Wagon):
    def __init__ (self):
        super().__init__(self.owner_name)

class Siding:
    def __init__(self):
        self._top_of_stack = -1
        self._wagon_array = [None] * 30
    
    def push_wagon(self, wagon):
        self._top_of_stack += 1
        self._wagon_array[self._top_of_stack] = wagon
    
    def pop_wagon(self):
        if self._top_of_wagon > -1:
            wagon = self._wagon_array[self._top_of_stack]
            self._top_of_stack -= 1
            return wagon
        else:
            raise Exception("No wagon found in this siding")
    
    def get_siding_details(self):
       wagon_order = []
       for i in range(self._top_of_stack):
           print(f"{self._wagon_array[i]} - wagon question.py:36")
           print(f'hello - wagon question.py:37')