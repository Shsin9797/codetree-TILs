n,m= map(int,input().split())
A = list(map(int,input().split()))
B= list(map(int,input().split()))

cnt =0 

for i in range(n-m+1):#A의 시작점 
    #돌면서 B값 삭제
    BB = B[:] 
    for k in range(i,i+m):
        for t in range(m):
            if A[k] == BB[t]:
                BB[t]=0
                break # 한번 없앴으면 끝내야됌 
    
    #BB 값 다삭제되면 cnt 값 증가 
    if sum(BB)==0:
        cnt+=1

print(cnt)