class Test:
    x = 10

t1 = Test()
t2 = Test()

t1.x = 20   # creates INSTANCE variable

print(t1.x)  # 20
print(t2.x)  # 10
print(Test.x) # 10

class A:
    x = 5   # declared + initialized here

class A:
    def __init__(self):
        self.y = 10   # declared + initialized at runtime    

# Important Insight
# Class variables → defined once at class creation
# Instance variables → defined each time object is created

# What is __dict__?
# A dictionary that stores attributes of:
# object OR
# class

class A:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = A()
print(obj.__dict__)

class A:
    x = 100
    
    def method(self):
        pass

print(A.__dict__)
a1=A()
print(a1.__dict__)

# A.__dict__ contains:
# class variables → x
# methods → method
# internal attributes → __dict__, __weakref__, etc.