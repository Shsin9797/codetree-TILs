n,m= map(int,input().split())
arr = [[0]*m for _ in range(n)]

Anum = ord('A')
Znum = ord('Z')
num= Anum 

def in_range(y,x):
    return 0<=y<n and 0<=x<m

dys,dxs = [0,1,0,-1],[1,0,-1,0]
di=0

x,y =0,0
arr[y][x] = chr(num)

for _ in range(n*m):
    for _ in range(2):
        ny,nx = y+dys[di], x+dxs[di]
        if in_range(ny,nx) and arr[ny][nx]==0:
            y,x =ny,nx
            num+=1
            if num > Znum:
                num= Anum

            arr[y][x] = chr(num)
            
            break
        else:
            di = (di+1)%4

for a in arr:
    print(*a)