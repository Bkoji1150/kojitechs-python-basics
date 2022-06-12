from datetime import datetime
import sys, os
from pprint import pprint

def checkFileLessThanXdays(file_path):
    """This function check all files less than x days and delete 
    Parameter: 1(str) Description: 
    file_path: requires directory path.
    variables: [age]
    return None
    """
    age = 3
    try:
        if not os.path.exists(file_path):
            print("Please provide a valid path")
        if os.path.isfile(file_path):
            print("OOoops!, You just provided a file please provide directory path.!")
        for each_file in os.listdir(file_path):
            result = os.path.join(file_path, each_file)
            if os.path.isfile(result):
                time_stamp = datetime.fromtimestamp
                file_creation_date =  time_stamp(os.path.getctime(result))
                if file_creation_date.day > age:
                    print(f"{result}, created {file_creation_date.day} Days ago")         
    except Exception as e:
        print(e)  
    return None      


file_path = input("Enter directory path: ")
checkFileLessThanXdays(file_path)

# write a function a function.
# This function would require one argument("name of file")

# system wild search to check the file 
# print out the full path of the file. 