n= int(input())
OFFSET = 100
MAXRAN = 201
arr = [[0]*(MAXRAN+1) for _ in range(MAXRAN+1)]

for i in range(n):
    x1,y1,x2,y2 =map(int,input().split())
    if i %2 ==0: #빨강 
        num = 0
    else: #파랑
        num = 1

    for j in range(x1,x2):
        for k in range(y1,y2):
            arr[j][k] = num

sumBlue =0
#합
for a in arr:
    sumBlue += sum(a)

print(sumBlue)