n= int(input())

for cnt in range(n,0,-1):
    for i in range(n,0,-1):
        if i <= cnt:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()