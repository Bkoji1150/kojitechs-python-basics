# In this article, you will learn error and exception handling in Python.

# By the end of the article, you’ll know:
try:
    import boto2
except ModuleNotFoundError as e:
    print(e)
'''
How to handle exceptions using the try, except, and finally statements
'''
try:
    guess = input("Enter name: ")
    name = bello
    print("my name is koji {name}, user {guess}")
except Exception as e:
    print(e)

print(" i love python.")    
'''
How to create a custom exception
'''
try:
    guess = input("Enter name: ")
    name = bello
    print("my name is koji {name}, user {guess}")
except Exception as e:
    print(e)

'''
How to raise an exceptions
'''


'''
How to use built-in exception effectively to build robust Python programs
'''

'''

Table of contents
What are Exceptions?
Why use Exception
What are Errors?
Syntax error
Logical errors (Exception)
Built-in Exceptions
The try and except Block to Handling Exceptions
Catching Specific Exceptions
Handle multiple exceptions with a single except clause
Using try with finally
Using try with else clause
Raising an Exceptions
Exception Chaining
Custom and User-defined Exceptions
Customizing Exception Classes
Exception Lifecycle
Warnings

What are Exceptions?
An exception is an event that occurs during the execution of programs that disrupt the normal flow of execution (e.g., KeyError Raised when a key is not found in a dictionary.) An exception is a Python object that represents an error..
'''
# Types of exceptions.
'''
FileNotFoundException
ImportError
RuntimeError
NameError
TypeError
'''

'''
Why use Exception
'''
'''
tandardized error handling: Using built-in exceptions or creating a custom exception with a more precise name and description, you can adequately define the error event, which helps you debug the error event.
Cleaner code: Exceptions separate the error-handling code from regular code, which helps us to maintain large code easily.
Robust application: With the help of exceptions, we can develop a solid application, which can handle error event efficiently
'''