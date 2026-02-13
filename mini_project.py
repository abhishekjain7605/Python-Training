import json

class Bank:
    file = "Bank_Database.json"
    
    # Load data from JSON file
    try:
        with open(file, "r") as f:
            __bank_database = json.load(f)
    except:
        __bank_database = {}
        
    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.__bank_database, f, indent=4)
    
    def deposit(self, name, amount):
        if amount > 0:
            self.__bank_database[name][1] += amount
            self.__bank_database[name][2].append(f"Deposited amount: {amount}, Balance: {self.__bank_database[name][1]}")
        else:
            print("Amount must be positive")
        self.save_data()
        print("=================================================")
        print(f"Current Balance:{self.__bank_database[name][1]}")
        print("=================================================")
        
        
    def withdrawal(self, name, amount):
        if amount <= self.__bank_database[name][1]:
            self.__bank_database[name][1] -= amount
            self.__bank_database[name][2].append(f"Withdrawn amount: {amount}, Balance: {self.__bank_database[name][1]}")
        else:
            print("Insufficient balance")
        self.save_data()
        print("=================================================")
        print(f"Current Balance:{self.__bank_database[name][1]}")
        print("=================================================")
        
        
    def view_balance(self, name):
        print("=================================================")
        print(f"Name: {name}, Balance: {self.__bank_database[name][1]}")
        print("=================================================")

    def transaction_history(self, name):
        print("=================================================")
        print("Transaction History:") 
        for t in self.__bank_database[name][2]:
            print(t)
        print("=================================================")
    
    def operations(self, name):
        self.name = name
        while True:
            print("Choose an operation:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. Transaction History")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(name,amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                self.withdrawal(name,amount)
            elif choice == '3':
                self.view_balance(name)
            elif choice == '4':
                self.transaction_history(name)
            elif choice == '5':
                print("Thanku for visiting our bank, have a nice day!")
                break
            else:
                print("Invalid choice, please try again.")
     
    def register_new_user(self, name, password):
        if name in self.__bank_database:
            print("Account with this name already exists, Please choose a different username")
        else:
            self.__bank_database[name] = [password, 1000, ["Initial balance: 1000"]]
            self.save_data()
            print(f"Account created successfully\nWelcome to your new account {name}!")
            self.operations(name)
     
    def login(self, name, password):
        if name in self.__bank_database and self.__bank_database[name][0] == password:
            print(f"Login successful\nWelcome back, {name}!")
            self.operations(name)
        else:
            print("Invalid username or password")
    
    def __init__(self):
        

        print("===================================")
        print("Welcome to the Bank")

        a = int(input("Press 0 if you are a new user and 1 if already registered: "))
        if a == 0:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            self.register_new_user(name, password)
        elif a == 1:
            name = input("Enter your name: ")
            passwd = input("Enter your password: ")
            self.login(name, passwd)
        else:
            print("Enter valid input")


abhi = Bank()