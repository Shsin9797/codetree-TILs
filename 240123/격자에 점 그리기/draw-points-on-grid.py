n,m= map(int,input().split())#split() 빼먹지말기 .. 
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1,m+1):
    r,c = map(int,input().split())
    arr[r-1][c-1] =1 

for a in arr:
    print(*a)