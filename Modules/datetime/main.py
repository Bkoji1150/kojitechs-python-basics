
from dataclasses import dataclass
from datetime import datetime

import time

# print(dir(time))
# print(dir(datetime))


tim = datetime.now()
print(tim)
# print(tim.strftime("%Y/%m/%d %H:%m"))
# print(dir(tim))
# print(time.hour)
# print(dir(time))
# print(time.minute)
# print(time.month)


'''
print("----------------------------")
print(datetime.today())
print("----------------------------")

'''

# print(dir(datetime))
# print(datetime.year)

# 2022-05-29 15:04:45.124563


def Hello(name):
    print(f"Good morning and welome {name}")
    time.sleep(300)
    print(f"Good morning and welcome {name}")
   
