from calendar import c
import csv
import time
from pprint import pprint

'''
Working with csv, (comma sep, value)

First_name, last_name. data_of_birth
'''

'''
req_file = input("Enter file name: ")

with open(req_file, 'r') as file:
    data = csv.reader(file)
    for each_file in data:
        print(each_file)
'''

# How to create and write to a csv file using python.

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', '28748', 'AL', 'ALB'],
    ['Algeria', '2381741', 'DZ', 'DZA'],
    ['American Samoa', '199', 'AS', 'ASM']
]

with open("address.csv", "w") as file:
    csv_writer = csv.writer(file)
    # we have to write those data in a csv file
    #print(dir(csv_writer))
    # writerow  is just to write one list 
    csv_writer.writerow(header)

    # write multiple rows we use writerows

    csv_writer.writerows(data)
 

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    {"town": "Alabama",
     "area": 25678, 
     "country_code2": "alb", 
     "country_code3": "ABSHD"
     },
    {'town': 'Algeria', 
    'area': 2381741, 
    'country_code2': 'DZ',
    'country_code3': 'DZA'
    },
    {'town': 'American Samoa', 
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'
    }
]

with open("address2.csv", "w") as file:
    # pprint(dir(csv))
    # 
    writer_csv = csv.DictWriter(file, fieldnames=header)
    # pprint(dir(writer_csv))
    writer_csv.writeheader()

    writer_csv.writerows(data)

#      