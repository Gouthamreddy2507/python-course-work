#1.birthday format
date = input()
print(date[6:],'/',date[3:5],'/',date[:2])


#2.even or odd
n=int(input())
if n%2==0:
    print("Even winner")
else:
    print("Odd winner")


#3.vowel replacer
n=input().lower()
v='aeiou'
for i in v:
    if i in n:
        n=n.replace(i,'*')
print(n)


#4.shopping cart
n=list(map(float,input().split()))
print(sum(n))
print(max(n))


#5.secure login system
credentials=("admin", "python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("login successful")
else:
    print("access denied")


#6.remove duplicates
n=set(input().split(','))
print(sorted(n))      


#7.students marks record(dict)
n=int(input())
data={}
max_value=0
res=''
for i in range(n):
    name,mark=input().split()
    mark=int(mark)
    if mark>max_value:
        res=name
    data[name]=mark

print(data)
print(res)


#8.reverse words
n=input().split()
for i in range(len(n)):
    n[i]=n[i][::-1]
print(' '.join(n))


#9.clean list(removing 0's)
s=input()
s=s.replace('0','')
print(s.split())


#10.frequency counter
n=input()
res={}
for i in n:
    if i not in res and i!='':
        res[i]=n.count(i)
print(res)

    
