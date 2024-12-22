class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance if balance >= 0 else 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: ${self.__balance}")

    def __display_balance(self):
        print(f"Current Balance: ${self.__balance}")
       
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance
   
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

account = BankAccount("123456789", 100.0)
account.deposit(50)
account.withdraw(30)
account.set_balance(-10)
account.display_account_info()
