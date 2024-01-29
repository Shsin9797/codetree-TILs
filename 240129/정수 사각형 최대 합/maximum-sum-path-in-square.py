#강의내용 복습 
arr=[[4],[6,2],[3,7,9],[3,4,9,9]]
n=4
dp=[[0 for _ in range(n)]for _ in range(n)]

#1. dp 배열 정의 = 최상단arr[0][0]에서 시작하여 db[i][j] 까지 왔을때 얻을수있는 최대합  

#2. 초깃값 
dp[0][0] = arr[0][0]
for i in range(n):
    #첫번째줄 
    dp[i][0] = dp[i-1][0] +arr[i][0]
    #대각선줄 
    dp[i][i] = dp[i-1][i-1] + arr[i][i]


#3. 점화식 
for i in range(2,n):
    for j in range(1,i):
        con1=dp[i-1][j-1] +arr[i][j] 
        con2=dp[i-1][j] +arr[i][j]

        dp[i][j] = max(con1,con2)


#출력 
for i in dp:
    print(*i)