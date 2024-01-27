n=   int(input() )

for i in range(n):
    a,b= map(int,input().split())
    sumV=1
    for k in range(a,b+1):
        sumV *=k
    
    print(sumV)