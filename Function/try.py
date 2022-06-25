
def Fizz_Buzz(num):
    """This function is use for the FizzBuzz theory.
    Parameter: 1(int): 
    Return:
    None
    """
    if num%15==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num) 
    return None


"""Return function
"""
def return_fizzbuzz(num):
    """This function is use for the FizzBuzz theory.
    Parameter: 1(int): 
    Return:
    num
    """
    if num%15==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        return num
 

response = return_fizzbuzz(12)
