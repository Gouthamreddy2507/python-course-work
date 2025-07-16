fact = 0
n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f"{n} is prime number\nFactors count={fact}")
else:
    print(f"{n} is not a prime number\nfactors count={fact}")