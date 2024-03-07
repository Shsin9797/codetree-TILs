n=int(input())
arr=[[0 for _ in range(202)] for _ in range(202)]
OFFSET =100
for _ in range(n):
    x1,y1,x2,y2 =map(int,input().split())
    x1,y1,x2,y2 = x1+OFFSET,y1+OFFSET,x2+OFFSET,y2+OFFSET
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] =1

sumArr= 0 
for a in arr:
    sumArr +=sum(a)
print(sumArr)