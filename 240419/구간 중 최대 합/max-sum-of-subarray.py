import sys

n,k=map(int,input().split())
arr = list(map(int,input().split()))

max_sum = - sys.maxsize

for i in range(n-k+1):# 시작점
    sum_val=0
    for j in range(k):
        sum_val += arr[i+j] #  k 가 아니라 j 쓰는거 주의
    
    max_sum = max(sum_val,max_sum)

print(max_sum)