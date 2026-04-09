try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")    


x = 2

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")    
# This works
# ✔ But it's a generic exception (base class)

if x < 0:
    raise ValueError("No numbers below zero")
# ✔ Better than generic Exception
# ✔ More meaningfuls




class NegativeNumberError(Exception):
    pass

if x < 0:
    raise NegativeNumberError("No numbers below zero")


class AgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise AgeError("You must be at least 18")

print("Access granted")





# Advanced Version (Real Use Case)
class AgeError(Exception):
    def __init__(self, age, limit):
        self.age = age
        self.limit = limit
        super().__init__(f"Age {age} is below required {limit}")


try:
    raise AgeError(15, 18)
except AgeError as e:
    if e.age < 10:
        print("Very young user")
    elif e.age<16:
        print(" young user")
        
    
    print(e)          # message
    print(e.age)      # 15
    print(e.limit)    # 18



class BalanceError(Exception):
    def __init__(self, balance, withdraw):
        self.balance = balance
        self.withdraw = withdraw
        super().__init__(f"Balance {balance} is less than withdraw {withdraw}")


def withdraw_money(balance, amount):
    if amount > balance:
        raise BalanceError(balance, amount)
    return balance - amount

try:
    withdraw_money(1000, 2000)
except BalanceError as e:
    print(e)



# 5. Custom Exception Hierarchy (Very Important for Exams)

# You can create a base exception class and derive others:
class AppError(Exception):
    pass

class LoginError(AppError):
    pass

class PaymentError(AppError):
    pass
try:
    raise LoginError("Invalid login")
except AppError:
    print("Application error occurred")


# 6. Using else and finally with Custom Exceptions    
try:
    raise AgeError("Invalid age")
except AgeError:
    print("Custom exception caught")
else:
    print("No error")
finally:
    print("Always executes")






# 1. Order of except blocks (MOST COMMON TRAP)
class A(Exception):
    pass

class B(A):
    pass

try:
    raise B()
except A:
    print("A caught")
except B:
    print("B caught")    


# 1. Multiple Exceptions in ONE except (Tuple)

# This is very common in PCAP.    
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Handled")