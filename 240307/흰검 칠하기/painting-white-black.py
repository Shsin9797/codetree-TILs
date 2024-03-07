n = int(input())

OFFSET = 100000

orderList = [] 
pointer = 0

g =0 
w =0
b =0

for _ in range(n):
    x,d = input().split()
    x = int(x)

    #왼쪽으로 가는경우 범위
    if d =="L":
        left = pointer-x+1
        right = pointer 
        pointer=left
    #오른쪽으로 가는경우 범위
    elif d=="R":
        left= pointer
        right= pointer +x -1
        pointer =right
    orderList.append([left,right,d])

white = [0 for _ in range(200002)]
black = [0 for _ in range(200002)]
color= ['N' for _ in range(200002)]
#이동시키기 
for l,r,d in orderList:
    l += OFFSET
    r += OFFSET

    if d =="L" : # 흰색에 추가 
        for i in range(l,r+1):
            white[i]+=1   
            color[i] = 'W'
    elif d=="R": # 검정색에 추가   
        for i in range(l,r+1):
            black[i]+=1
            color[i] ='B'

#색깔 판별
for t in range(200002):
    i,j = white[t], black[t]
    if i >=2 and j >=2:
        g +=1
        continue
    else:
        if color[t] == 'W':
            w += 1
        elif color[t] == 'B':
            b +=1

print(w,b,g)