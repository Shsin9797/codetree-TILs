n,m=map(int,input().split())
A=list(map(int,input().split()))

sumA=0

def f(m):
    sumA=0
    m -= 1
    sumA+=A[m]
    while(m>0):
        if m%2==0:
            m -=1 
        else:
            m //= 2
        sumA += A[m]
    
    
    return sumA
        

print(f(m))