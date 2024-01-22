n,m= map(int,input().split())
arr=[[0 for _ in range(n)] for _ in range(n)] # n+1 로적으면 안되는거 주의.. 출력형식 잘보기

for _ in range(m):
    r,c = map(int,input().split())
    arr[r-1][c-1] =1 #출력형식 때문에 여기에 -1 해줘야함 

for a in arr:
    print(*a)