import getpass

password = "kojitechs123"
user_guess = ""
user_atempt = 3 

# first condition "if user_atempt not == 0", user_guess!=password

while user_guess != password and user_atempt !=0:
    user_guess = getpass.getpass("Enter password: ")
    user_atempt -=1
    if user_atempt==0: 
        print("Sorry you have exhausted the limit of 3")  
        
    if user_guess == password:
        print("Login succesful!")
        
    else:
        print(f"You have {user_atempt} attempt left")