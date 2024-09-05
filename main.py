import csv
import re

class Login():
    def correct(self):
        with open("login.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["user"] == self.username and row["pass"] == self.password:
                    return "Correct"
                else:
                    return "Incorrect password"


def main():
    login = Login()
    
    while True:
        username = input("Username: ")
        password = input("Password: ")
        
        login.username = username
        login.password = password
        
        print(login)
        if login.correct() == "Correct":
            break
        else:
            print(login.correct())

    while True:
        response = input(f"Good day, {login.username}! What would you like to do? Log out (/) or add a new password (+)\n")
        if response == "/":
            exit("\nLogged out successfully. Thanks for using Duple-login for logging in. I hope you have a great day!")
        elif response == "+":
            create()


def create():
    with open("login.csv", "a") as new:
        writer = csv.DictWriter(new, fieldnames=["user", "pass"])
        user = input("Username: ")
        password = input("Password: ")

        writer.writerow({"user": user, "pass": password})


    print("Login information added sucessfully. Restarting...\n\n")


if __name__ == "__main__":
    main()
