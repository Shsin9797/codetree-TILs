n= int(input())
spots=[]
for _ in range(n):
    x,y =map(int,input().split())
    spots.append((x,y))

lens= []
#두점사이의 거리구하기
for i in range(n):
    for j in range(i+1,n):
        x1,y1 = spots[i]
        x2,y2 = spots[j]
        le= (x1-x2)**2 + (y1-y2)**2
        lens.append(le)

print(min(lens))