
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
    raise ValueError
except ValueError:
    print("Enter wrong number")    
except ZeroDivisionError:
    print("Can't divide with Zero please provide df number") 
"""


# C two run time error
   

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

"""
try:
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    print(f"The result of {a} and {b} is :{ a /b}")
except Exception as e:
    print("invalid input, please try again")
"""




# finally
"""

"""

"""
try:
    file = open("file1.sh", "r")
    data = file.readline() 
    print(data)
except Exception as e:
    print("file not foud", e)       
finally:
    file.close() 
"""
  

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
"""
   


# try, except and else block
"""
try: The try block for risky code that can throw an exception.
except: The except block to handle error raised in a try block.
else: The else block is executed if there is no exception.
"""


"""
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b 
    print("a/b = %d" % c)

except Exception as e:
    print("Can't divide by zero")
else:
    print("We are in else block ")
"""

    
    


# Raising an Exceptions
# [1,10]
# To calculate interest rate (amount, year , rate) /100

amount = 100
year = 6
rate = 11

try:
    if rate > 10:
        raise ValueError(rate)
    interest = amount * year * rate / 100
    print(interest)
except ValueError:
    print("interest rate is not in rage of 10")    

print("jhello")
