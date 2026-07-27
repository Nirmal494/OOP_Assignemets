from bank import BankAccount
class SavingAccount(BankAccount):
    def __init__(self, bankName, accountNumber, accountName, accountBalance, minimumBalance):
        super().__init__(bankName, accountNumber, accountName, accountBalance)
        self.MinimumBalance = minimumBalance

    def deposit(self, amount):
        self.AccountBalance = self.AccountBalance + amount
        print("Deposit Successful.")
        print(f"Account Balance: {self.AccountBalance}")
        print()

    def withdraw(self, amount):

        if amount > (self.AccountBalance - self.MinimumBalance):
            print("Invalid balance")
            print("Minimum balance must remain Rs.500 in the account")
            print()

        else:
            self.AccountBalance = self.AccountBalance - amount
            print("Withdrawal success full")
            print(f"New Account Balance is {self.AccountBalance}")
            print()

    def check_balance(self):
        print(f"Account Balance: {self.AccountBalance}")
        print()
