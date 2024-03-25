n,m =map(int,input().split())

#정답배열 만들기 
answer= [ [0]*m for _ in range(n)]

#범위내 확인 함수 
def inRange(i,j):
    return (0<=i<n) and (0<=j<m) 

#방향 :오른,아래,왼,위
dys,dxs = [0,1,0,-1],[1,0,-1,0]
dire=0

answer[0][0] = 1
x,y = 0,0

for i in range(2,n*m+1):#
    ny,nx = y+dys[dire] , x+dxs[dire] 
    if inRange(ny,nx) and answer[ny][nx] ==0:
        y,x = ny,nx 
        answer[y][x]= i    
    else:
        dire = (dire+1)%4
        y,x = y+dys[dire], x+dxs[dire]
        answer[y][x] =i


#출력 
for a in answer:
    print(*a,sep=" ")