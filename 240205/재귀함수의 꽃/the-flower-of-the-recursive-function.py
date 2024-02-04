def f(x): 
    #종료조건
    if x==0:
        return

    print(x,end=" ")
    f(x-1)
    print(x,end=" ")





n=int(input())
f(n)

"""n = int(input())
for i in range(n,0,-1):
    print(i,end=" ")
for j in range(1,n+1):
    print(i,end=" ")"""