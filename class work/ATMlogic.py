data = {
    1234:{"balance": 45678,"pin":123,"history":[]},
    4321:{"balance": 8978,"pin":123,"history":[]},
    9874:{"balance": 876578,"pin":123,"history":[]},
    1454:{"balance": 45645678,"pin":123,"history":[]},
    1875:{"balance": 23478,"pin":123,"history":[]}
}
acc_num = None
login_status = False

def menu():
    print("1.check balance")
    print("2.deposit")
    print("3. withdraw")
    print("4.transaction history")
    print("0.exit")
    
def login(acc,pin):
    if acc in data:
        if data[acc]["pin"]==pin:
            global acc_num
            global login_status
            acc_num=acc
            login_status=True

            print("login successful")
        else:
            print("invalid pin")
    else:
        print("invalid acc num")

def check_balance():
    if login_status and acc_num:
        print(f"balance: {data[acc_num]["balance"]}")
    else:
        print("login again")

def deposit():
    if login_status and acc_num:
        dep = int(input("enter amout to deposit: "))
        data[acc_num]["history"].append(f"deposited: {dep}")
        data[acc_num]["balance"] += dep
        print(f"balance: {data[acc_num]["balance"]}")

def withdraw():
    if login_status and acc_num:
        amount = int(input("enter amount to withdraw: "))
        if amount>data[acc_num]["balance"]:
            print("amount not sufficient")
        else:
            data[acc_num]["history"].append(f"withdraw: {amount}")
            data[acc_num]["balance"] -= amount
            print(f"amount after withdraw: {data[acc_num]["balance"]}")
def transaction_history():
    if login_status and acc_num:
        print(f"transactions: {data[acc_num]["history"]}")
def exit():
    if login_status and acc_num:
        print("Thank you")





