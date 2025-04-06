#creating a CLASS
class Student:
    
    #class Variable  {Value will remain te same for all the objects}
    grade = 8
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
#Creating OBJECT
indradip = Student("IndraDiddy", 12)
nooria = Student("Nooria", 13)

print(f"Student Grade = {indradip.grade}")
print(f"Students Grade = {nooria.grade}\n\n")

print(f"Students name : {indradip.name}\nStudents age : {indradip.age}\n\n")
print(f"Student name : {nooria.name}\nStudents age : {nooria.age}\n\n")    