N= int(input())
x=0
y=0

dy,dx = [0,-1,1,0],[-1,0,0,1]

for _ in range(N):
    B,d = input().split()
    d= int(d)

    if B=='W':
        dire=0
    elif B=='S':
        dire=1
    elif B=='N':
        dire=2
    elif B=='E':
        dire=3
    
    x,y = x+dx[dire]*d,y+dy[dire]*d

print(x,y )