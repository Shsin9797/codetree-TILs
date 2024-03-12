N,M =map(int,input().split())

#기본세팅
w=0
AList =[]
BList=[]
ar,br =0,0 #누적 거리 

AList.append(ar)
BList.append(br)
cnt =0

#A 이동
for _ in range(N):
    v,t =map(int,input().split())
    for i in range(t):
        ar += v
        AList.append(ar)


#B 이동
for _ in range(M):
    v,t =map(int,input().split())
    for i in range(t):
        br += v
        BList.append(br)

if AList[1] > BList[1]:
    w='a'
else:
    w='b'

#
for t in range(len(BList)):
    if w == 'a':
        if AList[t] < BList[t]:
            w= 'b'
            cnt +=1
    elif w=='b':
        if AList[t] > BList[t]:
            w='a'
            cnt +=1

print(cnt)