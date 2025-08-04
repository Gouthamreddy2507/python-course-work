
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



#12. Currency denomination counter
money = int(input())

countof2k = 0
while money>=2000:
    money-=2000
    countof2k +=1

print(f"{countof2k}*2000")

countof500 = 0
while money>=500:
    money-=500
    countof500 +=1

print(f"{countof500}*500")

countof100 = 0
while money>=100:
    money-=100
    countof100 +=1

print(f"{countof100}*100")

countof50 = 0
while money>=50:
    money-=50
    countof50 +=1

print(f"{countof50}*50")

countof10 = 0
while money>=10:
    money-=10
    countof10 +=1

print(f"{countof10}*10")

countof1 = 0
while money>=1:
    money-=1
    countof1 +=1

print(f"{countof1}*1")



#13.Movie ticket price based on day and age
day = input("Day: ").lower()
age = int(input("age: "))

if age<12:
    if day == "sunday" or day == "saturday":
        print(200-200*0.5)
    else:
        print(150-150*0.5)
else:
    if day == "sunday" or day == "saturday":
        print(200)
    else:
        print(150)




#14. Classify angle as Acute, Right, Obtuse, Straight
angle = int(input("angle: "))
if angle<90:
    print("Acute")
elif angle==90:
    print("Right")
elif 91<=angle<=179:
    print("Obtuse")
elif angle==180:
    print("Straight")

    


#15. Grade college admission based on marks in 3 subjects
s1,s2,s3 = tuple(map(int,input().split(",")))
avg = (s1+s2+s3)/3
if avg>90 and s1>70 and s2>70 and s3>70:
    print("Admit")
elif avg>80:
    print("Waitlist")
else:
    print("Reject")



#16. Check if a number is perfect
n = int(input())
sum = 0
for i in range(1,n):
    if n%i==0:
        sum+=i
if n==sum:
    print("Perfect number")
else:
    print("Not Perfect number")



#17. Identify type of triangle by angles
a,b,c = tuple(map(int,input().split()))
if a+b+c == 180:
    if a<90 and b<90 and c<90:
        print("acute")
    elif a==90 or b ==90 or c==90:
        print("Right")
    elif a>90 or b>90 or c>90:
        print("obtuse")


#18. Convert marks (0–100) to 10-point GPA scale
marks = int(input())
if 91<=marks<=100:
    print("10")
elif 81<=marks<=90:
    print("9")
elif 71<=marks<=80:
    print("8")
elif 61<=marks<=70:
    print("7")
elif 51<=marks<=60:
    print("6")
elif 41<=marks<=50:
    print("5")
elif 31<=marks<=40:
    print("4")
elif 21<=marks<=30:
    print("3")
else:
    print("2")



#19. Check if four digits form a lucky number (sum of first two == last two)
number=input()

if int(number[0])+int(number[1])==int(number[2])+int(number[3]):
  print("Lucky number")
else:
  print("Unlucky number")


#20. Car insurance premium based on age and experience
age = int(input())
exp = int(input())
if age<25 and exp<3:
    print("High risk")
elif age>25 and exp>5:
    print("Low risk")



#22. Classify number as Single, Double, or Triple digit
n = input()
l = len(n)
if l==1:
    print("Single Digit")
elif l==2:
    print("Double Digit")
elif l==3:
    print("Triple Digit")



#23. Validate time input (HH:MM format)
HH,MM = input().split(":")
if 0 <= int(HH) <= 23 and 0 <= int(MM) <= 59:
    print("valid")
else:
    print("invalid")



#24. Weather categorization by temperature
t = int(input())
if t<10:
    print("Very cold")
elif 10<=t<=20:
    print("cold")
elif 21<=t<=30:
    print("warm")
else:
    print("hot")



#25. Assign mobile plan based on usage
data_in = input()
data = float(data_in.upper().replace("GB",""))
if data<1:
    print("Plan A")
elif data<5:
    print("Plan B")
else:
    print("Plan C")



#26. Identify duplicate digits in a 3-digit number
n = input()
if len(set(n))<len(n):
    print("duplicate present")
else:
    print("unique digits")



#28. Student attendance eligibility (> 75% to write exam)
attended = int(input())
total = int(input())
if (attended/total)*100>75:
    print("eligible")
else:
    print("not eligible")



#29. Print grade trend based on increasing or decreasing scores
s1,s2,s3 = tuple(map(int,input().split()))
if s1<s2<s3:
    print("improving")
elif s1>s2>s3:
    print("declining")
else:
    print("fluctuating")



#30. Validate mobile number (10 digits, starts with 6–9)
number = input()
if len(number)==10 and (number[0]==6 or number[0]==7 or number[0]==8 or number[0]==9) and number.isdigit():
    print("valid")
else:
    print("invalid")