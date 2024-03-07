n =int(input())
OFFSET = 100
MAXRAN = 200
arr = [ [0]*(MAXRAN+1) for _ in range(MAXRAN+1) ]

for _ in range(n):
    x,y= map(int,input().split())
    x +=OFFSET #오프셋 더해주기 꼭!
    y +=OFFSET

    for i in range(x,x+8): #x 보다 8 큰값임.. 
        for j in range(y,y+8):
            arr[i][j] =1

#합구하기 
sumArr=0
for a in arr:
    sumArr +=sum(a)

print(sumArr)