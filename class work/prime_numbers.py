
fact = 0
n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f"{n} is prime number\nFactors count={fact}")
else:
    print(f"{n} is not a prime number\nfactors count={fact}")



#prime or not
def primeornot(n):
    if n<=1:
        print("no")
    if n>=2:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("no")
        else:            
            print("yes")
n=int(input())
primeornot(n)


#each character of the name on a new line in the form of a right-aligned triangle
def ra(name):
    n=len(name)
    for i in range(n):
        s=n-1-i
        print(" "*s + name[i])
name = input()
ra(name)


#Check if a password has at least 8 characters and contains '@'.
pwd = input()
if len(pwd)>=8 and "@" in pwd:
    print("True")
else:
    print("False")