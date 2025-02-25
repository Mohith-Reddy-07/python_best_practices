class Account:
    def __init__(self, balance=0):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")


acc = Account(100)
acc.deposit(50)
acc.withdraw(30)
