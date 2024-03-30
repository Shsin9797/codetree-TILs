n,m= map(int,input().split())
arr=[[0]*n for _ in range(n)] 
dys,dxs =[-1,0,1,0],[0,1,0,-1]

def inRange(r,c):
    return 0<=r<n and 0<=c<n

def isComfort(r,c):
    cnt =0 
    global dys
    global dxs 

    for i in range(4):
        nr,nc = r+dys[i], c+dxs[i]
        if inRange(nr,nc) and arr[nr][nc] ==1:
            cnt +=1

            

    if cnt ==3:
        return True
    else:
        return False

for _ in range(m):
    r,c= map(int,input().split())
    r,c = r-1,c-1
    arr[r][c]=1

    #편안한상태 체크
    if isComfort(r,c):
        print(1)
    else:
        print(0)