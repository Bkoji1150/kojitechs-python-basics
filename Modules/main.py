
## libary or it's a module
from pprint import pprint 
'''
import builtins
import secret_program

passwd = secret_program.password
print(passwd)
'''
import builtins
# pprint(dir(builtins))
import os 

# pprint(dir(os.path))

path = '/Users/kojibello/Downloads/src/kojitechs/kojitechs-python-basics/Modules/main.py'


# path= input("Enter a directory path: ")
'''
print(os.path.basename(path))
print(os.path.getsize(path))
print(os.path.getctime(path))# date, year, seconds
os.path.exists(path)
os.path.isfile(path)
os.path.join(path, path2)
os.path.realpath('main.py') # absolute path of a file

'''

'''
print(os.path.realpath('main.py'))
import platform
print(dir(platform))
'''

# print(os.path.exists(path))

'''
if  os.path.exists(path):
    print(f"path exist\nCongrats")
else:
    print(f" path doesn't exists")
'''
# write simple prog, that would only accept a file( not dir)

pprint(dir(os))

'''
Creating directory with python
'''
# print(os.mkdir("kojibello"))


# pat = ["folder1", "folder2", "folder3"]
# for i in pat:
#     os.mkdir(i)
'''
pat = ["kojibello"]
for i in pat:
    os.removedirs(i)
'''

print(os.listdir())