#simple interest
def simple_interest(P,R,T):
    return (P*R*T)/100
P = int(input())
R = int(input())
T = int(input())
print(F"Simple Interest is: {simple_interest(P,R,T)}")

#append to a list
def app(my_list,num):
    my_list.append(num)
    return my_list
my_list= list(map(int,input().split()))
num=int(input())
print(app(my_list,num))

#double each element in a list
def double(l):
    d_l=[]
    for i in l:
        d_l.append(i*2)
    return list(d_l)
l=list(map(int,input().split()))
print(double(l))



#sort a list
def sortlist(l):
    s_l=sorted(l)
    return s_l
l=list(map(int,input().split()))
print(sortlist(l))

#clear a list
def clearlist(l):
    l.clear()
    return l
l=list(map(int,input().split()))
print(clearlist(l))



#updating a dictionary
def dec(d):
    d["a"]=2
    return d
d={"a":1,"b":2}
print(dec(d))

#Increment All Values in Dictionary
def dic(d):
    for key in d:
        d[key]+=1
    return d
n=int(input())
d={}
for i in range(n):
    key=input()
    value = int(input())
    d[key]=value
print(dic(d))


