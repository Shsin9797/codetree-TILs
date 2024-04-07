n= int(input())

arr= [[0]*n for _ in range(n)]

cnt =  n*n

#왼,위,오,아래
dys,dxs = [0,-1,0,1],[-1,0,1,0]
p= 0
x,y = n-1,n-1
arr[y][x] =cnt
cnt -= 1

def inRange(y,x):
    return 0<=x<n and 0<=y<n

while True:
    if cnt < 1:
        break
    ny,nx= y+dys[p], x+dxs[p] 
    
    if inRange(ny,nx) and arr[ny][nx] ==0:
        y,x= ny,nx
        arr[y][x] = cnt 
        cnt -=1 
    else:
        p = (p+1)%4

for a in arr:
    print(*a)