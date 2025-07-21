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