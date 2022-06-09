
"""
try :
    # statements in try block
except Exception as e:
    # executed when exception occured in try block
"""

"""
a = 10
b = 0

c = a / b

print(f"{a} / {b} is = {c}")
"""
# ZeroDivisionError
# To handle this 

"""
try:
    a = 10
    b = 0
    c = a / b
    print(f"{a} / {b} is = {c}")
except:
    print("Can't divide with Zero please provide df number")   

print("I love python.") 
"""

"""
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print(f"{a} / {b} is = {c}")
except ValueError:
    print("Enter wrong number")    
except ZeroDivisionError:
    print("Can't divide with Zero please provide df number") 
"""
# Catch two run time error
   

# Enhance this code by 
"""
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print(f"{a} / {b} is = {c}")
except (ValueError, ZeroDivisionError):
    print("Please enter valid value") 

"""



# finally
"""
try:
    # block code 
    # anothoth
    
finally:
       # block of code 
       # This will be executed 
       # also 

"""
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Please enter valid value")
finally:
    print("Inside finally block")     

