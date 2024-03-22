x,y =0,0
dire=0
dx,dy = [0,1,0,-1],[1,0,-1,0]
N=input()
for m in N:
    
    if m =='L':
        dire = (dire-1+4)%4
    elif m=='R':
        dire = (dire+1) %4
    elif m=='F':
        x,y = x+dx[dire], y+dy[dire]

print(x,y)