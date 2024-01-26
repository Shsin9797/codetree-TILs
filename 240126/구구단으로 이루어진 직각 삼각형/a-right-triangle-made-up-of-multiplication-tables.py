n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{i} * {j} = {i*j}",end="")
        if j < n-i+1 :
            print(" / ",end="")
        else:
            print()
            break