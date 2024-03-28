n =int(input())
MaxLen= n*10 
arr= [[0]*MaxLen for _ in range(MaxLen)]

time =0 
Arrived = False 
x,y = 0,0
dys,dxs=[-1,0,1,0],[0,1,0,-1]

def inRange(ny,nx):
    return 0<=ny<MaxLen and 0<=nx<MaxLen

for _ in range(n):
    b,l = input().split()
    l=int(l)


    if b =='N':
        dire= 0
    elif b=='E':
        dire=1
    elif b=='S':
        dire=2
    elif b=='W':
        dire=3

    for i in range(l):
        
        ny,nx = y+dys[dire] , x+dxs[dire]

        y,x=ny,nx

        time +=1 

        if y ==0 and x==0:
            Arrived =True
            break


    if Arrived :
        break


if Arrived:
    print(time)
else:
    print(-1)