def feed(l):
    for i in l:
        yield i

l=["file1",'file2','file3','file4']

load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))


def simple_generator():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))



def count_up_to(n):
    count = 1
    while count<=n:
        yield count
        count +=1
counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


#function vs generator
#function approach
def square(n):
    result=[]
    for i in range(n):
        result.append(i*i)
    return result
print(square(5))


#generator approach
def square(n):
    for i in range(n):
        yield i*i
sq = square(5)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))


def countdown(n):
    while n>0:
        yield n
        n-=1
cd = countdown(3)
print(next(cd))
print(next(cd))
print(next(cd))


