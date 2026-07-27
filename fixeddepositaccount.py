from bank import BankAccount
class FixedDepositAccount(BankAccount):
    def __init__(self, bankName, accountNumber, accountName, accountBalance, depositPeriod, interestRate,):
        super().__init__(bankName, accountNumber, accountName, accountBalance)
        self.DepositPeriod = depositPeriod
        self.InterestRate = interestRate

    def fixed_deposit(self, amount):
        self.AccountBalance += amount
        print(f"Fixed account balance: {self.AccountBalance}")

    def fixed_withdrawal(self):
        print(f"Error: {self.AccountNumber} is a fixed deposit account")
        print("Withdrawals are not allowed in fixed deposit accounts")

    def cal_interest(self):
        interest = (self.AccountBalance * self.InterestRate * self.DepositPeriod) / 100
        print(f"Interest Amount: {interest}")
        print(f"Total Amount: {self.AccountBalance + interest}")

    def check_fix_balance(self):
        print(f"Account Balance: {self.AccountBalance}")