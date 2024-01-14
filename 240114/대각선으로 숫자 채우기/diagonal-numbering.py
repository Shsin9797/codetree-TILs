n,m= map(int,input().split())

arr= [[0 for _ in range(m)] 
        for _ in range(n)]

num =1 

for sum in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i+j == sum:
                arr[i][j]= num
                num +=1




# 출력 
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()