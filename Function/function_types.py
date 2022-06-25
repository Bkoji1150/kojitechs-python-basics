
"""

def notify(name):
    return f"hello {name} You payment is due"

# print(notify("Grand Baca"))
message = notify("Grand Baca")

with open("message.sh", "w") as file:
    file.write(message)

"""

# def a function to notify users about their payment
# A return function
def send_text(name):
    return f"hello {name} you payment is due!"
    

   


# Print function

def send_text(name):
    print(f"hello {name} you payment is due!")
    return None
    
send_text("baca")

def increment(number, by):
    return number + by

print(increment(1, by=4))  