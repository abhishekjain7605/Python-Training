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
            
        
    def register_new_user(self, name, password):
        if name in self.__bank_database:
            user_exist = True 
            return user_exist
        else:
            self.__bank_database[name] = [password, 1000, ["Initial balance: 1000"]]
            self.save_data()
            return False

    
    def login(self, name, password):
        if name in self.__bank_database and self.__bank_database[name][0] == password:
            return True
        
    