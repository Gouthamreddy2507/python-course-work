'''
#1.automated salary tax calculator
salary=float(input())
if salary <=250000:
    print("No Tax")
elif salary>=250001 and salary<=500000:
    print((salary*5)/100)
elif salary>=500001 and salary<=1000000:
    print(salary*0.2)
elif salary>1000000:
    print(salary*0.3)


#2.Movie Ticket Pricing system
n=int(input())
total=0
for i in range(n):
    age=int(input())
    if age<5:
        total+=0
    elif age>=5 and age<=18:
        total+=100
    elif age>=19 and age<=60:
        total+=150
    elif age>60:
        total+=120
print(total)


#3.Electricity Bill Generator
units = int(input())
bill=0
if units<=100:
    bill+=units*1.5
elif units>100 and units<=200:
    bill+=150+(units-100)*2.5
elif units>200 and units<=500:
    bill+=400+(units-200)*4
elif units>500:
    bill+=1600+(units-200)*6
print(bill)


#4.Car Parking Fee calculator
hours=int(input())
fee=0
if hours<=2:
    fee=30
    
elif hours>2 and hours<24:
    fee=30+(hours-2)*10
    
elif hours>=24:
    fee=hours*24
print(fee)
'''

#5.Product Inventory Checker(Nested Conditionals)
name=input()
qua=int(input())
if qua==0:
    print("Out of stock")
if qua>=1 and qua<=10:
    print("Low Stock")
if qua>=11 and qua<=50:
    print("In Stock")
if qua>=50:
    print("OverStocked")



#6.Pattern row wise alterbating 0 and 1
n = int(input())
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
   

#Gym subscription billing(menu driven program)

print(
    "1. Monthly-₹500",
    "2. quarterly-₹1300",
    "3. yearly-₹5000"
    )
ch=int(input())
n=int(input())
if ch==1:
    print(n*500)
elif ch==2:
    print(n*1300)
elif ch==3:
    print(n*5000)

    
#8.Billing bot
total=float(input())
if total<1000:
    print(total)
elif total>999 and total<5000:
    print(total-total*0.05)
elif total>4999 and total<10000:
    print(total-total*0.1)
elif total>=10000:
    print(total-total*0.15)

     

#9.ATM pin verification with blocking logic
pin=1234
for i in range(3):
    epin=int(input())
    if epin==pin:
        print("Access Granted")
        break
else:
    print("Atm Blocked. try again later")
    


#10.Bus Booking System
total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f"total Seats:{total_seats}")
print(f"booked: {len(booked_seats)}")
print(f"Available seats:{total_seats-len(booked_seats)}")

