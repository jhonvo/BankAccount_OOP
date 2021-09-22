from BankAccount import BankAccount

Account1 = BankAccount(10.0,0.15)
Account2 = BankAccount(100.0,0.15)

Account1.deposit(100.0).deposit(50.0).withdraw(30).yield_interest().display_account_info()
Account2.deposit(50.5).deposit(50.0).withdraw(20.0).withdraw(20.0).yield_interest().display_account_info()
print(".....")
BankAccount.instances()

