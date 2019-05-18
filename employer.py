class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + "lallala   " + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
         Person.__init__(self,first, last)
         self.staffnumber = staffnum


x = Person("Marge", "Simpson")
# print x.firstname,x.lastname,x
y = Employee("Homer", "Simpson", "1007")
print y.staffnumber,y.firstname,y.lastname, y
