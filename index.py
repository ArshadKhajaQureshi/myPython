# import services 
# services is the name of the file and not type the extension

# services.greet()
# from services import * #all the functions and the variables
# from services import greet as gt

# gt(3)

# import services as ser #alias

# print(ser.greet(7))

from subpackage import services as srv

srv.greet(56)

from subpackage.services import greet

import math

result=math.sqrt(25)

finalresult=result+99

import random
random_number=random.randint(1,9) #random number between 1 and 9
print(random_number)

print(help(math.sqrt))

print(help("if"))