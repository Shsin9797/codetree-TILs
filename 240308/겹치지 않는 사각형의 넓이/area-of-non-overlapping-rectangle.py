ax1,ay1,ax2,ay2= map(int,input().split())
bx1,by1,bx2,by2= map(int,input().split())
mx1,my1,mx2,my2= map(int,input().split())
OFFSET = 1000
arr= [[0 for _ in range(OFFSET*2+2)] for _ in range(OFFSET*2+2)] 

#A 칠하기 
for i in range(ax1,ax2):
    for j in range(ay1,ay2):
        arr[i][j] = 1 

#B 칠하기 
for i in range(bx1, bx2):
    for j in range(by1,by2):
        arr[i][j] =1

#M으로 덮기 
for i in range(mx1,mx2):
    for j in range(my1,my2):
        arr[i][j] =0
    
#합하기 
sumArr =0 
for a in arr:
    sumArr += sum(a)

#출력 
print(sumArr)