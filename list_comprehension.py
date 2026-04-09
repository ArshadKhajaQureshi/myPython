l1=[2,3,4, "String1",True, False,{"name":"Raj","div":5}]

# indexing starts with zero

# list comprehension
squares=[x*x for x in range(1,10)] #create a list and whatever is the value returne from for loop is stored
print(squares)

squares_new=[]
for x in range(1,10):
    squares_new.append(x*x) #attach the value to the list [1,4,9....]


print(squares_new)    

# Conditional list Comprehension
# even numbers in the range 1 to 21

evens=[x for x in range(1,21) if x%2==0]
# loop through numbers
# keep only those numbers where the condition is True
print(evens)

evens2=[]
 
for x in range(1,21): #1, 2, 3, 4
    if x%2==0:
        evens2.append(x)  
 
print(evens2)  

#convert strings to uppercase
words=["hello","world","Germany","France"]
uppercase_words=[i.upper() for i in words]
print(uppercase_words)

list1=[1,2,3,4]
list2=["A","B","C","D"]

#nested for loop inside list comprehension
pairs=[(x,y) for x in list1 for y in list2]
print(pairs)

# tuple is another datatype of python
# Immutable (cannot change values)
# written using parantheses ()

# nested list comprehension
matrix=[[j for j in range(3)]   for i in range (4)] #0,1,2
print(matrix)

square=lambda x:x**2 #lambda is a keyword x is the input, the expresn after : will be returned
print(square(5))

# def square(x):
#     return x**2

# square(5)

nums=[1,2,3,4]
squares=list(map(lambda x:x**2, nums))
print("square from map",squares)

squares1=[x**2 for x in nums] #create a list and whatever is the value returne from for loop is stored
print(squares1)

#filter function
# used to select elements from a list based on some condition

numbers=[1,2,3,4,5,6]
evens=list((76,"98","raj"))
print(evens)
print(type(evens))

numbers2=[1,2,3,4,5,6,7]
evens=list(filter(lambda x:(x%2==0), numbers2))

print(evens)

words=["hi","hello","cat","python"]
result=list(filter(lambda x:len(x)>3, words))

print(result)

print(len(numbers2))
print(len("germany"))

# dictionar comprehension
squares_dict={x:x**2 for x in range (10)}
print(squares_dict)

