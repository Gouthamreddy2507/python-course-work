'''
#1. Check if three lengths form an Equilateral, Isosceles, or Scalene triangle
a,b,c=tuple(map(int,input().split()))
if a==b==c:
    print("equivalent")

elif a!=b and b!=c and a!=c:
    print("scalene")
else:
    print("isosceles")



#2. Classify a character as: vowel, consonant, digit, special character
a=input()
vol = 'aeiouAEIOU'
if a.isalpha():
    if a in vol:
        print("vowel")
    else:
        print("consonant")
elif a.isdigit():
    print("digit")
else:
    print("special character")



#3. BMI Calculator and Category
#BMI = weight (kg) / (height (m))^2
h=float(input())
w=float(input())
bmi = w/h**2
if bmi<24.5:
    print("underweight")
elif bmi==24.5:
    print("normal")
else:
    print("overweight")



#4. Electricity bill calculator based on units used
units = int(input())
bill = 0
if units>0:
    if units<=100:
        bill=units*1
    elif units>=101 and units<=200:
        bill=100+(units-100)*2
    elif units>200:
        bill=300+(units-200)*3
print(bill)


#5. Check if a number is Armstrong (3-digit)
n=input()
arm = 0
for i in n:
    arm += int(i)**3
if int(n)==arm:
    print("amstrong")
else:
    print("not amstrong")


#6. Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 special char)
pwd = input()
if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("u")
        elif i.islower():
            s.add("l")
        elif i.isdigit():
            s.add("d")
        else:
            s.add("s")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")

#7. ATM Withdrawal Simulation
balance = int(input())
withdraw = int(input())
if withdraw<=balance and withdraw%100==0:
    print("success")
else:
    print("insufficient balance")



#8. Ticket fare calculator with age-based discounts
age = int(input())
fare = 100
if age>0:
    if age<=5:
        fare = 0
    elif age < 18:
        fare -= fare*0.5
    elif age > 60:
        fare -= fare*0.3
print(fare)



#9. 24-hour to 12-hour time converter
hrs,min = tuple(map(int,input().split(":")))
if 0<=hrs<=24 and 0<=min<=60:
    if 1<=hrs<=12:
        print(f"{hrs}:{min}AM")
    elif 13<=hrs<=24:
        print(f"{hrs-12}:{min}PM")
else:
    print("invalid")

#11. Grading system with nested bands (including + and - grades)
mark = int(input())
if 90<=mark<=100:
    print("A")
elif 85<=mark<=89:
    print("B+")
elif 80<=mark<=84:
    print("B")
elif 70<=mark<=79:
    print("C")
elif mark<70:
    print("F")

'''

#12. Currency denomination counter
m = int(input())
c2000=0
c500=0
c100=0
while m >0:
    if m%2000==0:
        c2000=m//2000
        updated = m%2000
    elif updated%500 == 0:
        c500 = updated//500
        updated_1 = m%500
    elif updated_1%100 == 0:
        s100=updated_1//100
        updated_1 -= s100*updated_1
        c100 = s100
print(c2000,c500,c100)





