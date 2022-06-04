import csv
from pprint import pprint

'''
Working with csv, (comma sep, value)

First_name, last_name. data_of_birth
'''
req_file = input("PLEASE ENTER FILE PATH: ")

# Opening csv in a write mode. 

with open(req_file, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["INSTANCE_ID", "STATUS", "ARN"])
    csv_writer.writerow(["TuesDay-10-05-2022", "Introduction/Installation of Terraform", "https://drive.google.com/file/d/1i9piQ_9AhRZO38Dayy5LX606PHSzusv7/view?usp=sharing"])
    csv_writer.writerow(["ThursDay-12-05-2022", "First Terraform Init, terraform plan, and terraform apply", "https://drive.google.com/file/d/1f97bfuoZQsLZmnNntdnG0mdEPdKIjOCI/view"])
