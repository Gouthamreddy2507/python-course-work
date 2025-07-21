
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)


def sumofnum(n):
    if n==0:
        return 0
    return n+sumofnum(n-1)
n=6
print(sumofnum(n))


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=6
print(factorial(n))


def shoot(n):
    if n==1:
        return 1
    print("before ",n)
    shoot(n-1)
    print("after",n)
n=5
shoot(n)



#fibonnacci series
n=int(input())
a=0
b=1
if n==1:
    print(a)
elif n>=2:
    
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c




