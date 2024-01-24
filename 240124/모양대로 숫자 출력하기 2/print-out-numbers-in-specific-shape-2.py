n= int(input())
cnt = 2
for i in range(n):
    for j in range(n):
        if cnt >8 : 
            cnt =2
        print(cnt,end=" ")
        cnt +=2
    print()