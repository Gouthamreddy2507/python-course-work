#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n=int(input())
for i in range(1,n+1):
    print(f"{i}!={factorial(i)}")

#(sum of numbers)
def SumofNumber(n):
    s=0
    
    for i in range(n):
        s+=i
    return s
n=int(input())
print(f"{n}={SumofNumber(n)}")


#addition
def addition(a,b):
    return a+b
a=int(input())
b=int(input())
print(addition(a,b))

#square
def square(a,b):
    return a**b
a=int(input())
b=int(input())
print(square(a,b))



#area of circle
def areaofcircle(r):
    return 3.14*(r**2)
r=int(input())
print(areaofcircle(r))


#Greet the user
def greet(name):
    return name
name=input()
print(f"Hello, {name}")


#celsius to fahrenheit
def CtoF(c):
    return (c*(9/5))+32
c = int(input("enter temp in celsius: "))
print(f"temp in fahrenheit: {CtoF(c)}")


