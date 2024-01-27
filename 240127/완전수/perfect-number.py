start,end= map(int,input().split())

cnt =0
for i in range(start,end+1):
    
    ls= []
    for j in range(1,i):
        if i%j==0:
            ls.append(j)
    
    if sum(ls) == i:
        cnt+=1
print(cnt)