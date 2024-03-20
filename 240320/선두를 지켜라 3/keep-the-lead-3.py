N,M =map(int,input().split())
Ali=[]
Bli=[]
Win=[]
aP,bP=0,0
Ali.append(aP)
Bli.append(bP)
#A
for _ in range(N):
    v,t =map(int,input().split())
    for _ in range(t):
        aP += v 
        Ali.append(aP)
    
    
#B
for _ in range(M):
    v,t =map(int,input().split())
    for _ in range(t):
        bP += v 
        Bli.append(bP)

#선두 확인 
for i in range(len(Ali)):
    if Ali[i] > Bli[i]:
        Win.append('a')
    elif Ali[i] < Bli[i]:
        Win.append('b')
    else:
        Win.append('a,b')



# 선두 변경횟수 세기 
cnt=0
for i in range(1,len(Win)):
    if Win[i-1] != Win[i]:
        cnt +=1

print(cnt)