n = int(input())

cnt = 1
for i in range(4):
    for j in range(4):
        
        if cnt >9:
            cnt=1
        print(cnt,end="")
        cnt +=1 
    print()