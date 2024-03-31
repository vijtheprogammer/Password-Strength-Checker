import string
import time

time.sleep(1)
print("\nWelcome to the Password Strength Checker!")
print("-----------------------------------------")
time.sleep(1)

while (quit != "No"):
    password = input ("\nEnter a password: ")
    time.sleep(1)
    #adds 1 if it exists and 0 if it doesn't
    upper = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    password_length = len(password)

    chars = [upper, lower, special, digits]

    score = sum(chars)

    with open ("10k-most-common.txt", "r") as f:
        common = f.read().splitlines()

    if password in common:
        print ("\nPassword was found in a common list.")
        print ("Score: 0 / 7")
        exit()
    
    else:
        if password_length < 4:
            score += 0
        elif password_length > 4 and password_length < 8:
            score += 1
        elif password_length >=8 and password_length <= 12:
            score += 2
        elif password_length > 12:
            score += 3

        if score > 7:
            score = 7
        
        print(f"Score: {score:d} / 7")

        if score < 5:
            print("  Strength Level: Weak\n")
        elif score >= 5 and score < 6:
            print("  Strength Level: Okay\n")
        elif score >= 6:
            print("  Strength Level: Strong\n")
        
        time.sleep(1)
    
    quit = input("\nWould you like to continue? \nEnter: Yes / No\n ")
    
    while(quit != "Yes" and quit != "No"):
        quit = input("That was an invalid option please select Yes or No: ")
    
