
atm_user_details={
    1:{"acc_no":123456,"pin":1234,"bal":300,"view_tran":[]},
    2:{"acc_no":678901,"pin":5678,"bal":250,"view_tran":[]},
    3:{"acc_no":876543,"pin":8901,"bal":350,"view_tran":[]},
    4:{"acc_no":543217,"pin":7654,"bal":400,"view_tran":[]},
}
for i in atm_user_details:
    print("welcome to the ATM")
    acc_no = int(input("Enter your account number: "))
    pin = int(input("Enter your PIN: "))


    if atm_user_details[i]["acc_no"]==acc_no and atm_user_details[i]["pin"]==pin: 
        print("Login Successful")
        
        while True:

            ATM_MENU= (
            "1. Check Balance",
            "2. Deposit", 
            "3. Withdraw",
            "4. View Transactions",
            "5. exit"
            )
            for j in ATM_MENU:
                print(j)
            op=int(input("select the option: "))
            if op==1:
                print(f"Current balance: {atm_user_details[i]["bal"]}")
            elif op==2:
                dep=int(input("enter amount to deposit: "))
                atm_user_details[i]["view_tran"].append(f"deposit: {dep}")
                atm_user_details[i]["bal"]+=dep
                print(f"you deposited amount: {dep}")
        
            elif op==3:
                withdraw=int(input("enter amount you want to withdraw:"))
                if withdraw>atm_user_details[i]["bal"]:
                    print("Insufficient balance")
                else:
                    atm_user_details[i]["view_tran"].append(f"withdrawl: {withdraw}")
                    atm_user_details[i]["bal"]-=withdraw
                    print(f"you withdraw: {withdraw}")
            elif op==4:
                print(f"your transactions: {atm_user_details[i]["view_tran"]}")
            elif op==5:
                print("thank you")
                break
            else:
                print("invalid option ")
        break

    else:
        print("Invalid account number or pin")






