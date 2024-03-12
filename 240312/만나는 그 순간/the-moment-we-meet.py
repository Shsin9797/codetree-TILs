n,m =map(int,input().split())
A=[]
B=[]

#시작점 
aP=0
bP=0

A.append(aP)
B.append(bP)

#A 이동
for _ in range(n):
    d,t = input().split()
    t=int(t)
    for _ in range(t):
        if d =='L':
            aP -= 1
        else:
            aP += 1
        A.append(aP)


#B이동
for _ in range(m):
    d,t = input().split()
    t=int(t)
    for _ in range(t):
        if d=='L':
            bP -= 1
        else:
            bP += 1
        B.append(bP)

isNoSamePosition =True
#만나는 지점 찾기 
for k in range(1,len(A)):
    if A[k] == B[k]:
        print(k)
        isNoSamePosition =False
        break

if isNoSamePosition:
    print(-1)