n= int(input())

for i in range(n): #행
    for j in range(n): #열
        if i==0 or (i <= j  and j%2==1):
            print("*",end=" ")
        else: #else 빼먹지말기
            print(" ",end=" ")
    print()