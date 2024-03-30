#886, 2862
n= int(input())
arr=[]
        #위,오,아래,왼
dys,dxs = [-1,0,1,0],[0,1,0,-1]

def changeDirect(m,direc): # 위>왼, 오>아래, 아래>오 ,왼>위 
    if m=='\\': # 0>3, 1>2, 2>1, 3>0
        direc = 3-direc
    elif m=='/': #아래>왼, 오>위 , 위>오, 왼>아래
        direc= (1-direc+4)%4 #2>3, 1>0, 0>1, 3>2
    return direc

for _ in range(n):
    mirror = input()
    temp =[]
    for i in mirror:
        temp.append(i)
    arr.append(temp)


k= int(input())

#시작점 정하기
# 방향
# 1~n: 아래 (2) / n+1~2n: 왼 (3) / 2n+1~3n: 위 (0) / 3n~ 4n-1 : 오른 (1)
# 넘버 (dy,dx) 
# (0,0~n-1) :증가  / (0~n-1, n-1) :증가  / (n-1, n-1~0) : x감소   / (n-1~0, 0) : y 감소
if 1<=k <=n:
    b= 2
    y,x = 0, k-1
elif n+1<=k<=2*n:
    b=3
    y,x = k-n-1, n-1
elif 2*n+1 <=k <= 3*n:
    b=0
    y,x = n-1, 3*n -k
elif 3*n+1 <=k <=4*n:
    b=1
    y,x =  4*n-k , 0

#범위 벗어나는 거 찾기
def inRange(dy,dx):
    return (0<=dy<n) and (0<=dx<n)

#진행하기 
cnt =0  

while True:#범위내인지 확인 
    #print('x',x,'y',y,'b',b)
    #거울 찾기 
    m = arr[y][x]
    #print(m) :거울 확인용
    cnt+=1 # 거울 한번 마주침 
    b= changeDirect(m,b) #방향 먼저 바꾸고 
    x,y = x+dxs[b], y+dys[b]#위치변경 
    if not inRange(x,y):
        #print('x',x,'y',y)
        break
    

print(cnt)