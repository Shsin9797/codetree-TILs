a,b = map(int,input().split())

for i in range(1,a+1):#행
    for j in range(1,b+1):#열 
        print(i*j,end=" ")
    print()