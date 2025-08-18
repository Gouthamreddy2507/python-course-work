#1. compute geometric values(math module)
import math
def circle_geometry(radius):
    area = math.pi*radius*radius
    circumference = 2*math.pi*radius
    print("(%.2f,%.2f)"%(area,circumference))

circle_geometry(7)
circle_geometry(2.5)

#2.Random Team Picker(Random module)
import random
def pick_random_team(members,team_size):
    print(random.choices(members,k=team_size))

pick_random_team(["soul","crazy","strange","knight"],2)


#3.Temperature Alert(Lambda +Filter)
t1 = list(filter(lambda i:i>40,[36,42,39,45,41]))
t2 = list(filter(lambda i:i>40,[]))
t3 = list(filter(lambda i:i>40,[39,52,79,450,412]))
print(t1,t2,t3,sep="\n")

#4.identify prime numbers(recursion)
def is_prime(n,i=2):
    if i == n//2+1:
        return
    if n%i==0:
        return False
    
    return is_prime(n,i+1)
n=13
if is_prime(n,2):
    print("prime number")
else:
    print("not prime number")


#5.reverse digits(recursion)
def reverse_number(n,rev=0):
    if n==0:
        return rev
    return reverse_number(n//10,rev*10+(n%10))
n = 1234
print(reverse_number(n))


#6.Filter by starting letter (lambda)
seq = ["cat","car","bat","apple"]
ch = "a"
startingletter = list(filter(lambda i:i.startswith(ch),seq))
print(startingletter)


#7.remove duplicates case-insensitive(set + lambda)
l = ["Apple","apple","Banana","BANANA","Cherry"]

s = {i.lower() for i in l}
us = set(map(lambda i:i.lower(),l))
print(s,us)


#9.countdown timer(generator)
def countdown(n):
    for i in range(n,0,-1):
        yield i

n = 10
cnt = countdown(n)
for i in range(n):
    print(next(cnt))



#10.nested sum(recursion)
def sumoflist(l):
    sum = 0
    for i in l:
        if type(i)==int:
            sum+=i
        else:
            sum+=sumoflist(i)
    return sum
    
print(sumoflist([1,[2,3],4]))