n,t= map(int,input().split())

Orders= input()
mat=[]
#행만들기 
for _ in range(n):
    mat.append(list(map(int,input().split())))

dys,dxs = [-1,0,1,0],[0,1,0,-1]
di=0
sumNum=0

y,x= n//2,n//2

sumNum += mat[y][x]

def inRange(y,x):
    return 0<=y<n and 0<=x<n


    


#탐색 
for order in Orders:
    if order =='L':
        di = (di-1+4)%4
    elif order =='R':
        di = (di+1)%4
    else:
        dy, dx = y+dys[di],x+dxs[di]
        if inRange(dy,dx):
            y,x= dy,dx
            sumNum += mat[y][x]

print(sumNum)