
import json, os
from pprint import pprint

from sqlalchemy import true


file_name = {'Name': {"First_Name": "Bello", "LastName": "koji", "Middle_name": '', "is_male": True},
            "Skills": ['Python', "Terraform", "cdk", "java script", "html" 'Ansible', ]          
}
 

# pprint(dir(json))


'''
if os.path.exists(file_name):
    print(f"{file_name} exists")
'''

# opening json file in a read mode...
'''
with open(file_name, "r") as file:
    data = file.read() 
    print(data)

'''
# json.dump() method(without "s" in dump) used to write python object (serialized)
# write
# json with Encond python dict in a file 

with open("loaduserinfor.json", "w") as file:
    json.dump(file_name, file, indent=4)


'''
with open("loaduserinfor.json", "r") as file:
    data = file.read()
    print(data)
'''


  







 

