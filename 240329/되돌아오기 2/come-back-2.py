order= input()
n= len(order)
arr=[[0]*n]
dire =0
x,y= 0,0

dys,dxs =[-1,0,1,0],[0,1,0,-1]
time =0 
Arrived = False

for o in order:
    time +=1
    if o=='L':
        dire = (dire-1+4)%4
    elif o=='R':
        dire = (dire+1)%4
    elif o=='F':
        y += dys[dire]
        x += dxs[dire]
    if x==0 and y==0:
        Arrived =True
        break

if Arrived:
    print(time)
else:
    print(-1)