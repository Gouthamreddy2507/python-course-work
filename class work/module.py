import ATMlogic
print("welcome to ATM")
acc=int(input("enter acc num: "))
pin = int(input("enter pin: "))

ATMlogic.login(acc,pin)
ATMlogic.check_balance()
ATMlogic.deposit()
ATMlogic.withdraw()
ATMlogic.transaction_history()
ATMlogic.exit()