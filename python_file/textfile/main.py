
import os
import time


# make sure file exist ------->
'''
read()  "r". (write)

# if file doesn't exist 
write() "w", ("r", "w")

# main 
mode
append() "a"

# close 
close()
'''

'''

path = input("Enter name of file: ")
file = open(path, "r")
data = file.read()
print(data) 
file.close()



'''

'''
response = os.path.exists(path)
print(response)
'''

#    how to read a text file

path = "textfile_example.txt"
with open(path, "r") as file:
    # data = file.read()
    # data = file.readlines()
    object = file.readlines()
    
# Write to a file with python
with open('writing_data.txt', 'w') as file:
    file.write("This is line one")
    file.write("This is line two\n")
    file.write("This is line 3")
    print(dir(file))
    file.writelines(object)


# appendding data in a file
with open('writing_data.txt', 'a') as file:
    file.write("this is the fouth line\n")
    file.write("this is the fith line\n")
    file.write("this is the fith line\n")









