date = input()
print(date[6:],'/',date[3:5],'/',date[:2])



n=input().lower()
v='aeiou'
for i in v:
    if i in n:
        n=n.replace(i,'*')
print(n)


n=list(map(float,input().split()))
print(sum(n))
print(max(n))


credentials=("admin", "python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("login successful")
else:
    print("access denied")

n=set(input().split(','))
print(sorted(n))      


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


n=input().split()
for i in range(len(n)):
    n[i]=n[i][::-1]
print(' '.join(n))


s=input()
s=s.replace('0','')
print(s.split())

n=input()
res={}
for i in n:
    if i not in res and i!='':
        res[i]=n.count(i)
print(res)

    
