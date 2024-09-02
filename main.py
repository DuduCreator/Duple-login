import csv
import re

def main():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if not re.search(r"^\w*$", username) and not re.search(r"^\w*$", password):
            print("Invalid format. Only letters, numbers and underscores allowed!")
        else:
            break
        
    with open("login.csv", "r") as file:
        reader = csv.DictReader(file)
            
        for row in reader:
            if row["user"] == username and row["pass"] == password:
                login(username)
            else:
                exit("Incorrect password")

def login(user):
    while True:
        response = input(f"Good day, {user}! What would you like to do? Log out (/) or add a new password (+)\n")
        if response == "/":
            exit("\nLogged out successfully. Thanks for using Duple-login for logging in. I hope you have a great day!")

    

if __name__ == "__main__":
    main()