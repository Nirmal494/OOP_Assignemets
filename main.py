from savingaccount import SavingAccount
from fixeddepositaccount import FixedDepositAccount

saving = SavingAccount("BOC", 300580, "Nirmal", 0, 500)
fix_depo = FixedDepositAccount("BOC", 300580, "Nirmal", 15000, 5, 10)

def savings_menu():
    while True:
        print("---Savings---")
        print("1.Account Balance:")
        print("2.Deposit")
        print("3.Withdrawal")
        print("4.Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            saving.check_balance()
        elif choice == 2:
            dp_amount = float(input("Enter deposit amount:"))
            saving.deposit(dp_amount)
        elif choice == 3:
            wd_amount = float(input("Enter Withdrawal amount:"))
            saving.withdraw(wd_amount)
        elif choice == 4:
            print("Exit...")
            print()
            break
        else:
            print("Enter number between 1-3")

def fixed_menu():
    while True:
        print("---Fix Deposit Accounts---")
        print("1.Account Balance:")
        print("2.Deposit")
        print("3.Calculate Interest")
        print("4.Withdrawal")
        print("5.Check balance")
        print("6.Exit")
        choice = int(input("Enter your choice:"))
        print()

        if choice == 1:
            fix_depo.check_fix_balance()
            print()
        elif choice == 2:
            amount = float(input("Enter amount:"))
            fix_depo.fixed_deposit(amount)
            print()
        elif choice == 3:
            fix_depo.cal_interest()
            print()
        elif choice == 4:
            fix_depo.fixed_withdrawal()
        elif choice == 5:
            fix_depo.check_fix_balance()
            print()
        elif choice == 6:
            print("Exit...")
            print()
        else:
            print("Enter number between 1-3")

def main():
    while True:
        print("---Bank System----")
        print("1.Savings Account")
        print("2.Fixed Deposit Account")
        print("3.Exit")
        choice = int(input("Enter your choice:"))
        print()

        if choice == 1:
            sacc_num = int(input("Enter you account number:"))
            if sacc_num == saving.AccountNumber:
                savings_menu()
            else:
                print("Invalid account number!")
                print("Please enter again")
        elif choice == 2:
            fix_acc_num = int(input("Enter you account number:"))
            if fix_acc_num == saving.AccountNumber:
                fixed_menu()
            else:
                print("Invalid account number!")
                print("Please enter again")

        elif choice == 3:
            print("Exit...")
            print()
            break
        else:
            print("Invalid number!")
            print("Please enter number between 1-3")

main()