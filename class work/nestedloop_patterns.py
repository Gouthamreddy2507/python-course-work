n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()

    
''' * * * * * 
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * * '''

n=int(input())
for i in range(n):
    for j in range(n):
        print(i,end=' ')
    print()

''' 0 0 0 0 0 
    1 1 1 1 1 
    2 2 2 2 2 
    3 3 3 3 3 
    4 4 4 4 4'''


n=int(input())
for i in range(n):
    for j in range(n):
        print(j,end=' ')
    print()

''' 0 1 2 3 4 
    0 1 2 3 4 
    0 1 2 3 4 
    0 1 2 3 4 
    0 1 2 3 4 '''
    

n=int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

''' * 
    * * 
    * * * 
    * * * * 
    * * * * *  '''


n=int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

''' * * * * * 
    * * * * 
    * * * 
    * * 
    * '''

n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()

'''         * 
          * * 
        * * * 
      * * * * 
    * * * * * ''' 


n=int(input())
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print()

''' * * * * * 
      * * * * 
        * * * 
          * * 
            *  '''

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

''' * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * *  '''

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

''' * * * * * 
    *       * 
    * * * * * 
    *       * 
    * * * * * '''

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

''' * * * * * 
          *   
        *     
      *       
    * * * * * '''

n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

''' *       * 
      *   *   
        *     
      *   *   
    *       * '''
n=int(input())
for i in range(n,0,-1):
    for j in range( n-i):
        print(" ",end=" ")
    
    for k in range(2*i-1):
        print("*",end=" ")
    print()
