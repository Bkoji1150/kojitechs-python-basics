
"""We can can use a global variable inside a function
"""


def add(arg1, arg2):
    '''This function sum up two expected argumenst. 
    '''
    global sum_of;
    sum_of = 30 # local variable.( it is defined inside a function. so it should only be used inside )

    print("We are insite the body.")
    
def main(b):
    c = sum_of + b
    print(c)
'''
response = add(1,1)    
print(response)
'''


a = 2 

def define():
    b = 4
    return b


def  add():
    c = a + define()
    print(c)

add()

