n= int(input())


cnt = ord("A")


for i in range(n):
    for j in range(n):
        print(chr(cnt),end="")
        cnt+=1
    print()