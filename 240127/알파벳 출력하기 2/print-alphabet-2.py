n= int(input())

cnt = ord("A")

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(cnt),end=" ")
        cnt+=1
    
    
    print()