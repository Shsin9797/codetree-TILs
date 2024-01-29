n=int(input())

# 1. dp 테이블 정의
dp = [0 for _ in range(1001)] 

#문제정의 ***
# F[i] : = i 층 높이의 계단을 올라갈 수 있는 방법의 수 %10007

# 2. 초깃값 정의
dp[0]=1 ##
dp[1]=0 ## 
dp[2]=1
dp[3]=1
dp[4]=1
dp[5]=2

# 3. 점화식을 활용해서 문제 해결하기 => 마지막 행동을 기준으로 .. 나누기 
if n>=5:    
    for i in range(5,n+1):# 플러스1 해줘야 n 번째 됨 
        dp[i]  = dp[i-2]+dp[i-3]
        dp[i] %= 10007


# 4. 출력 
if dp[n] :
    print(dp[n]%10007)
else:
    print(0)