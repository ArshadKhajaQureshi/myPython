# class Student:
#     school_name="Dr rodrigues High School"   # class variable
# # common to all objects
# # shared across all instances(objects)    
#     def __init__(self,name,marks,salary):
#         self.name=name
#         self.marks=marks
#         self._salary=salary  #protected variable with single underscore

#     def display(self):
#         print("Name :", self.name, "Marks :  ",self.marks, "School: ", Student.school_name,"Salary:",  self._salary)   

# s1=Student("Ars", 85, 450)         
# s2=Student("Dan",76, 980)

# s1.display()
# s2.display()



class Student:
    __school_name="Dr rodrigues High School"   # class variable
# common to all objects
# shared across all instances(objects)    
    def __init__(self,name,marks,salary):
        self.name=name
        self.marks=marks
        self.__salary=salary #private variable with double underscore

    def display(self):
        print("Name :", self.name, "Marks :  ",self.marks, "School: ", Student.__school_name,"Salary:",  self.__salary)   

s1=Student("Ars", 85, 450)         
s2=Student("Dan",76, 980)


s1.__salary=690  #creates a new variable for s1
s1.display()
s2.display()

print(s1._Student__salary) #name mangling in OOP
# this is discouraged way of working according to the guidelines (PEP guidelines)

print(Student._Student__school_name)

print(s1.__salary)             # 990
