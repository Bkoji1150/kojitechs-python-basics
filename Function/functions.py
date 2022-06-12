
# Docstring 

"""
def sending_notification(name):
    '''This function is to send message to default users
    Parameter1(int): user name 
    Arguments: expects one argument
    Return:
    None
    '''
    print(f"Hello {name} your payment is due!")


sending_notification("Baca") 
"""
   
"""

def ListAllInstances(*args):
    print(f"Here are all the instances {args}")

ListAllInstances("instance1", "instance1", "instance1", "jshshgdhd", "hshsuye", "hsuueie")
"""

"""
"""
def population(name, *args):
    print(f"This is the house of {name}\nWe have {args}")



def address(address, city):
    print(f"the address is {address}\nThis city is {city}")


def user_info(**kwargs):
    print(type(kwargs))
    print(kwargs)


user_info(name="koji bello", age=24, subject="python")