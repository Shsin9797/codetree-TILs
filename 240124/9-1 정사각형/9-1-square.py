n= int(input())
cnt =9

for i in range(n):
    for j in range(n):
        if cnt<1:
            cnt=9
        print(cnt,end="")
        cnt -=1
    print()