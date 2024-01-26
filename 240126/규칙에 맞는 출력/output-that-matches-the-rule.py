n = int(input())

for i in range(n):#행
    w = n-i
    for j in range(i+1):
        print(w+j,end=" ")     
    print()