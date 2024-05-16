n= int(input())
li = list(map(int,input().split()))

max_cnt = 0
 
for k in range(1,102):
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if (li[j]-k) == (k-li[i]):
                cnt +=1  
    max_cnt=max(cnt,max_cnt)


print(max_cnt)