
print("welcome to the ATM")
acc_no = int(input("Enter your account number: "))
pin = int(input("Enter your PIN: "))
if acc_no==123456 and pin==7890:
    print("Login Successful")

    ATM_MENU= (
    "1. Check Balance",
    "2. Deposit", 
    "3. Withdraw",
    "4. View Transactions",
    "5. exit"
)
    for i in ATM_MENU:
        print(i)
    op=int(input("select the option: "))
    if op==1:
        print(f"Current balance: ₹ {data[acc]['current_balance']}")
    elif op==2:
        amount=int(input("enter amount to deposit: "))
        
    elif op==3:
    elif op==4:
    elif op==5:
        break
    else:
        print("invalid option ")

else:
    print("Invalid account number or pin")






