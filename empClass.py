# this command write the file automatically
# has to be the top of the code chunk, the first line
# codes to write follows below
class Employee:
    def __init__(self, first_name, last_name, emp_number): # attributes
        self._first_name = first_name # _first_name is a private variable
        self._last_name = last_name
        self._emp_number = emp_number 
        
    # getter
    @property # decorator for getter
    def first_name(self):
        return self._first_name + "123"
    @property
    def last_name(self):
        return self._last_name
    @property
    def emp_number(self):
        return self._emp_number
    # create more functions
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    # setter
    @first_name.setter # the setter allows you to "set" values
    def first_name(self, newName):
        self._first_name = newName
    @last_name.setter
    def last_name(self, newLName):
        self._last_name = newLName
    @emp_number.setter
    def emp_number(self, newNum):
        self._emp_number = newNum
