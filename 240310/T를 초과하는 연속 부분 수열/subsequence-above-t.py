n,t = map(int,input().split())
arr = list(map(int,input().split()))

ans,cnt =0,0
# 개수 세기 
for i in range(n):
    if arr[i]> t:
        cnt +=1
    else:
        cnt =0 # T 보다 작거나 같은경우는 안셈.. 1아님 


    ans= max(ans,cnt)

print(ans)