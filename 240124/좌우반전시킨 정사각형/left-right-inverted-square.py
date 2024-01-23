n= int(input())

for i in range(1,n+1):#여기는(n,0,-1): 아님!!! 
    for j in range(n,0,-1):
        print(i*j,end=" ")
    print()