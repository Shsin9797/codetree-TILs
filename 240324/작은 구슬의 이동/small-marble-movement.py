n,t = map(int,input().split())
r,c,d = input().split()
r,c =int(r)-1,int(c)-1
dy, dx = [1,0,0,-1],[0,1,-1,0]

direct = {
    'U': 0,
    'R': 1,
    'D': 3,
    'L': 2
}

def inRange(i,j):
    return (0<= i < n) and (0<= j <n) 

#시작방향 
di_num= direct[d]


#움직이기 시작 
time =0 
while True :
    if time >= t : #부족 
        break 
    #범위내인지 체크 
    ny, nx = r +dy[di_num], c+dx[di_num]
    if not inRange(ny,nx):
        di_num = 3-di_num
    else:
        r,c= ny,nx
    time +=1 


print(r+1,c+1)