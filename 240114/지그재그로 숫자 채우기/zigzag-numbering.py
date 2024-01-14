n,m = map(int,input().split())

arr = [[0 for _ in range(m)]
        for _ in range(n)]

num =0

#채우기
for j in range(m):
    if j%2==0:
        for i in range(n):
            arr[i][j] = num
            num +=1 
    else:
        for i in range(n-1,-1,-1):
            arr[i][j] =num
            num +=1 

#출력
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()