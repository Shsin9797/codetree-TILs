T,a,b =map(int,input().split())
li=[0]*1001

def inRange(t):
    return 1<=t<=1001

def isSpecial(k):
    for i in range(500):
        if not inRange(k+i) or not inRange(k-i):
            return False
        if li[k+i]=='S' or li[k-i]=='S':
            return True
        if li[k+i]=='N' or li[k-i]=='N':
            return False


for _ in range(T):
    c,x =input().split()
    x=int(x)
    li[x] = c

cnt =0 

for k in range(a,b+1):
    #특별한 위치인지 판별 
    if isSpecial(k):
        cnt +=1

print(cnt)