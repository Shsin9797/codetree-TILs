import sys

n,k = map(int,input().split())
arr = [0]*(10000+1)

# 수직선 채우기
for _ in range(n):
    num,al= input().split()
    num = int(num)
    
    if al =='G': #1점
        arr[num] = 1
    else: #2점
        arr[num] = 2
    
max_sum = -sys.maxsize

# 합 완전탐색 
for i in range(1,10001-k+1): # 체킹 시작점 # +1 해주기 # 끝점은 n-k 아님.. arr 길이가 ..10001 임에 주의 ..
    sum_num = sum(arr[i:i+k+1]) # +1 해주기- 이게 첫점이랑 끝점 둘다 포괄하는거라
    max_sum = max(max_sum,sum_num)

print(max_sum)