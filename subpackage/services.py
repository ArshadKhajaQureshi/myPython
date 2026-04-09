def greet(y):
    print("hello Everyone")
    x=y  # xis a local variable as it is defined inside the function
    return x

def hello():
    print("hello python") 
    return "hello everyone"

x=9
y=88
print(__name__)  #__main__ or services

if (__name__ == "__main__"):  #true
    print("Running module directly")
    greet("Arshad")

