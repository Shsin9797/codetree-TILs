n,m= map(int,input().split())
A =list(map(int,input().split()))

def f(a,b):
    a,b = a-1,b-1
    sumA =0 
    for i in range(a,b+1):
        sumA +=A[i]
    return sumA


for i in range(m):
    a1,a2 = map(int,input().split())
    print(f(a1,a2))