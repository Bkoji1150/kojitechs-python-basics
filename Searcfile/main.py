import os 
import sys

def search_file(filename):
    """This search is use to search any file provided by user and display entire file path
    Paramater: int
    Return:
    None
    """
    file = os.walk("/")
    for r,d,f in file:
        for each_file in f:
            if each_file == filename: 
                print(os.path.join(r,each_file))
                print(sys.exit())

filename = input("what is the name of the file you searching for?: ")
search_file(filename)    
