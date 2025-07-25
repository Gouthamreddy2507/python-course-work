n=5
squ=lambda n: n*n
print(squ(n))


n=5
eo = lambda n: "Even" if n % 2==0 else "odd"
print(eo)


#map
l=[1,2,3,4]
squ = list(map(lambda i: i**2,l))
print(squ)


l=["soul","strange","smart","venom"]
c=list(map(lambda i: i.title(),l))
print(c)

l=["soul","strange","smart","venom"]
c=list(map(lambda i: i.upper(),l))
print(c)

l="python"
c=list(map(lambda i: i.title(),l))
print(c)


l="python"
v="aeiou"
c=list(map(lambda i:"*" if i in v else i,l))
print(c)



#filter
#Filter Even Numbers Using filter() and Lambda
l=[1,2,3,4,5,6]
evennum=list(filter(lambda i:  i%2==0,l))
print(evennum)



