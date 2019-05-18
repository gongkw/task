from employer import Person
from abc import ABCMeta,abstractmethod

class Employee(Person):
    # def __init__(self, first, last, staffnum):
    #      Person.__init__(self,first, last)
    #      self.staffnumber = staffnum


    __metaclass__=ABCMeta

    @abc.abstractmethod
    def  height(self): pass


y = Employee("Homer", "Simpson", "1007")
print y.staffnumber,y.firstname,y.lastname, y