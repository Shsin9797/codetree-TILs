ax1,ay1,ax2,ay2 = map(int,input().split())
bx1,by1,bx2,by2 = map(int,input().split())
OFFSET=1000
MINRAN = 2001
arr = [[0]*(MINRAN+1) for _ in range(MINRAN+1)]

ax1 += OFFSET
ax2 += OFFSET
ay1 += OFFSET
ay2 += OFFSET

bx1 += OFFSET
bx2 += OFFSET
by1 += OFFSET
by2 += OFFSET

#첫번째 사각형 채우기 
for i in range(ax1,ax2):
    for j in range(ay1,ay2):
        arr[i][j] =1

#두번째 사각형 채우기
for i in range(bx1,bx2):
    for j in range(by1,by2):
        arr[i][j] =0 



#가로길이 구하기 
sx,sy,ex,ey = ax1,ay1,ax2,ay2
for i in range(ax1,ax2):
    for j in range(ay1,ay2):
        if arr[i][j] == 1 :
            if sx > i : 
                sx = i 
            if sy >j :
                sy = j
            if ex < i :
                ex = i
            if ey <j:
                ey =j

#넓이 구하기 
print((ex-sx)*(ey-sy) )