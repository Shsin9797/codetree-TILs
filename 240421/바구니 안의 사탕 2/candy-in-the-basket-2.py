n,k= map(int,input().split())
#세팅 
arr= [0]*101
for _ in range(n):
    candy_num,idx=map(int,input().split()) 
    arr[idx] += candy_num

#구하기 
#길이 : K*2 +1 
max_candy=0

for i in range(101): # 시작점
    sum_candy=0
    for j in range(i,i+2*k+1):
        if j >100:
            break
        sum_candy += arr[j]
    
    max_candy= max(max_candy,sum_candy)

print(max_candy)