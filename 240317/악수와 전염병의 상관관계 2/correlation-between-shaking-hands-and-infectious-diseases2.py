N,K,P,T = map(int,input().split())
MaxTime = 250
hand = [(0,0) for _ in range(MaxTime +1)]
infected = [0 for _ in range(N+1)]

infectionCnt =[0 for _ in range(N+1)]
infectionCnt[P] =K
#악수 정황 저장
for _ in range(T):
    t,x,y =map(int,input().split())
    hand[t] = (x,y)

#감염자가 언제 처음 악수하는지 찾기 
for i in range(MaxTime+1):
    if hand[i][0] ==P :
        startTime = i 
        break
    elif hand[i][1]==P:
        startTime = i 
        break
infected[P] =1
time = startTime
#감염 루틴 
while True :
    if time > MaxTime:
        break
    d1,d2 = hand[time][0], hand[time][1]
    if infected[d1] ==1 and infectionCnt[d1] >0 :
        if infected[d2] == 0:
            infected[d2] =1
            infectionCnt[d2] =K
            if infected[d2] ==1 and infectionCnt[d2] >0:#감염된 사람끼리 악수하는경우 고려 
                infectionCnt[d2] -=1
        infectionCnt[d1] -=1
    elif infected[d2] ==1 and infectionCnt[d2] >0: 
        if infected[d1] ==0:
            infected[d1] =1
            infectionCnt[d1] =K
            if infected[d1] ==1 and infectionCnt[d1] >0:
                infectionCnt[d1] -=1
        infectionCnt[d2] -=1
    time +=1

infected.pop(0)# 첫번째 0초일때 빼줘야함 
print(*infected,sep="")