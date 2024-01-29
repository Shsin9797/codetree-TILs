n=int(input())

# 1. dp 테이블 정의
dp = [0 for _ in range(1001)] 
# 2. 초깃값 정의
dp[2]=1
dp[3]=1
dp[4]=1
dp[5]=2

# 3. 점화식
if n>=5:    
    for i in range(5,n):
        dp[i]  = dp[i-2]+dp[i-3]


# 4. 출력 
if dp[n] :
    print(dp[n]%10007)
else:
    print(0)