# 배열 세팅 
n =int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))


# dp 테이블 세팅 
dp = [[0 for _ in range(n)] for _ in range(n)]

# 테이블 정의 
# dp = (0,0)에서 시작하여 오른쪽 ,밑으로만 이동하여 (n-1,n-1)까지 갈때 최대합

#초깃값 
dp[0][0] = arr[0][0]


for i in range(1,n):
    #가로
    dp[0][i] = dp[0][i-1]+ arr[0][i]
    #세로
    dp[i][0] = dp[i-1][0] + arr[i][0]

#1넣기 귀찮아서 만듦... xxxx
# dp[1][1] = max(dp[0][1], dp[1][0]) + arr[1][1]

#점화식
for j in range(1,n): # 1부터 봐야할듯.. 
    for i in range(1,n):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+arr[i][j]



print(dp[n-1][n-1]) #범위 안벗어나게 주의