n,m = map(int,input().split())
arr= [[0]*m for _ in range(n)]

def inRange(x,y):
    return 0<=x<m and 0<=y<n

dys,dxs =[1,0,-1,0],[0,1,0,-1]
d= 0

x,y =0,0
cnt=1
arr[y][x] = cnt 

while cnt<(n*m): #여기 왜 등호 있으면 안되지... 
    nx,ny = x+dxs[d], y+dys[d]  #위치바꿔보기  
    if inRange(nx,ny) and arr[ny][nx]==0: #범위 내면  
        y,x =ny,nx
        cnt +=1 #넣기전에 플러스1 해주는거라.. 
        arr[y][x]=cnt  #넣고   
    else: #범위 밖이면 
        d = (d+1)%4 #방향을 바꿔보기 

for a in arr:
    print(*a)