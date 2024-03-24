n= int(input())
matrix = []
for _ in range(n):
    arr =list(map(int,input().split()))
    matrix.append(arr)

dys,dxs = [1,0,-1,0],[0,1,0,-1]

def inRange(i,j):
    return (0 <= i <n) and (0 <= j < n)

cntThree=0

for x in range(n):
    for y in range(n): # 매트릭스 탐험하기 
        cntOne=0
        for dy,dx in zip(dys,dxs):
            i,j = y+dy,x+dx
            if inRange(i,j) and matrix[i][j] ==1:
                cntOne +=1 
            if cntOne >=3:
                cntThree +=1 
                break

print(cntThree)