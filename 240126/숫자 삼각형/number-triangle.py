n= int(input())

for i in range(n):#행
    for j in range(i+1): #열
        print(j+1,end=" ")
    print()