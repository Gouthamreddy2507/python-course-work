
#sum of digits

def sumof(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumof(n//10)
n=int(input())
print(sumof(n))

#palindrome
def palindrome(name):
    if name[::-1]==name:
        return True
    else:
        return False
name=input()
print(palindrome(name))


#gcd
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input())
b=int(input())
print(gcd(a,b))


#fibonacci series
def fibonacci(n):
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
n=int(input())
fibonacci(n)



#sum of n natural numbers
def sumofnatural(n):
    sum=0
    for i in range(1,n+1):
        sum +=i
        
    return sum
        
n=int(input())
print(sumofnatural(n))


# maximum of three numbers
def maximum(a,b,c):
    return max(a,b,c)
num = input().split()
a=int(num[0])
b=int(num[1])
c=int(num[2])
print(maximum(a,b,c))


def fib(n):
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
    
n = int(input())
fib(n)