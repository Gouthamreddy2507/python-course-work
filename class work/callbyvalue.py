def update(n):
    print("before- inside the function",n)
    n=n+10
    print("after- inside the function",n)
n=10
update(n)
print("outside of the function",n)


def update(n):
    print("before- inside the function",n)
    n=n+10
    print("after- inside the function",n)
n=10.8
update(n)
print("outside of the function",n)

def update(n):
    print("before- inside the function",n)
    n=n+"programming"
    print("after- inside the function",n)
n="python"
update(n)
print("outside of the function",n)

def update(n):
    print("before- inside the function",n)
    n=False
    print("after- inside the function",n)
n=True
update(n)
print("outside of the function",n)


def update(n):
    print("before- inside the function",n)
    n[6]=36
    print("after- inside the function",n)
n={1:1,2:4,3:9,4:16,5:25}
update(n)
print("outside of the function",n)


def update(n):
    print("before- inside the function",n)
    n=n.copy()
    n=n.append(20)
    print("after- inside the function",n)
n=[1,2,3]
update(n)
print("outside of the function",n)




