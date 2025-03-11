
class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def greet(self): #class method
        print("Thanks for joining our company".format(self.name))

emp = Employee("jay", 3452)

# print('name: ', emp.name)
# print('ID: ', emp.empid)
# emp.greet()

emp.name = 'jack' # modify object
print(emp.name)

del emp.empid #delete object
# print(emp.empid)

#############################
# inheritacnce

class person: # parent class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def PersonInfo(self):
        print('name: ', format(self.name))
        print('age: ', format(self.age))
        print('gender: ', format(self.gender))

class student(person):
    def __init__(self, name, age, gender, ID, fees):
        person.__init__(self, name, age, gender)
        self.ID = ID
        self.fees = fees

    def StudentInfo(self):
        print('ID: ', format(self.ID))
        print('fees:', format(self.fees))

class teacher(person):
    def __init__(self, name, age, gender, empID, salary):
        person.__init__(self, name, age, gender)
        self.empID = empID
        self.salary = salary

    def TeacherInfo(self):
        print('empID: ', format(self.empID))
        print('salary: ', format(self.salary))

stud = student('jay', 17, 'male', 3452, 1000)
print('student details')
print('--------------------')
stud.PersonInfo()
stud.StudentInfo()


tech = teacher('alex', 35, 'male', 243, 3000)
print('employee details')
print('--------------------')
tech.PersonInfo()
tech.TeacherInfo()
