n=5
print("G")
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i ==n-1 or (i>=n//2 and j==n-1) or (i==n//2 and j>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
print("O")
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print("U")
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()                

print("T")
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


print("H")
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


print("A")
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print("M")
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=n//2) or (i+j==n-1 and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
