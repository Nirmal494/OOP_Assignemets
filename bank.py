class BankAccount:
    def __init__(self, bankName, accountNumber, accountName, accountBalance):
        self.BankName = bankName
        self.AccountNumber = accountNumber
        self.AccountName = accountName
        self.AccountBalance = accountBalance

    def acc_details(self):
        print(f"Bank Name: {self.BankName}")
        print(f"Account Number: {self.AccountNumber}")
        print(f"Account Name: {self.AccountName}")
        print(f"Account Balance: {self.AccountBalance}")












