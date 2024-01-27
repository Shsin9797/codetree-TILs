n= int(input())

cnt = ord("A")

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(cnt),end=" ")
        cnt+=1
        #알파벳만 돌리는건 Z에서 A로 돌아가는거 까먹지말기
        if (cnt> ord("Z")):
            cnt = ord("A")
    
    print()