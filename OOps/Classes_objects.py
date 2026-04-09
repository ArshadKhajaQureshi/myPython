class Student:
    school_name="Dr rodrigues High School"   # class variable
# common to all objects
# shared across all instances(objects)    
    def __init__(self,name,marks,salary):
        self.name=name
        self.marks=marks
        self._salary=salary

    def display(self):
        print("Name :", self.name, "Marks :  ",self.marks, "School: ", Student.school_name,"Salary:",  self._salary)   

s1=Student("Ars", 85, 450)         
s2=Student("Dan",76, 980)



print(Student.school_name)
print(s1.school_name)

print(s1._salary)
s1._salary=766



Student.school_name="ST Thomas"




s1.school_name="radhaKridhna High School"
s1.display()
s2.display()

print(s1.school_name)
print(Student.school_name)

# A variable defined using single underscore is considered as a protected variable
_rollno=89  # A normal variable