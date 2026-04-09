class Employee:  #parent class or Super class
    company="Koenig"
    def __init__(selfie,emp_id,name, salary):
        selfie.id=emp_id
        selfie.name=name
        selfie.salary=salary


    def display(self):
        print("the id no :  ", self.id, "  the nam is",self.name, "  salary:", self.salary , " Company:  ", Employee.company)

# method resolution order
class Developer(Employee):
    def __init__(selfie, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        selfie.language=language

    def display(self):    
        super().display()
        print("Language : ", self.language)


e1=Developer(101, "dan",67000,"Python")   
e1.display()     


class Manager(Employee):
    def __init__(selfie, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        selfie.team_size=team_size

    def display(self):    
        super().display()
        print("Team Size : ", self.team_size)


m1=Manager(102, "John",99000,25)   
m1.display()  

# method resolution order

class A:
    def show(self):
        print("Class A")

class B(A):
    def show2(self):
        print("Class B")

class C(A):
    def show3(self):
        print("Class C")     

class D(B, C):  #Multiple Inheritance and Multilevel inheritance
    def show1(self):
        print("Class D")           

d=D()
d.show()       # D-->B-->C-->A #Method resolution order

A
    
B ,C

D