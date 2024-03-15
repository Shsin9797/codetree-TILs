N,K,P,T = map(int,input().split())
MaxTime = 250
hand = [(0,0) for _ in range(MaxTime+1)]
infected = [0 for _ in range(N+1)]

#악수 정황 저장
for _ in range(T):
    t,x,y =map(int,input().split())
    hand[t] = (x,y)

cnt =0 
infected[P] =1 
#감염자 찾기 
for i in range(MaxTime+1):
    if cnt >= K : 
        break

    if hand[i][0] == P :
        cnt += 1
        a= hand[i][1]
        infected[a] = 1
    elif hand[i][1]==P :
        cnt += 1
        a= hand[i][0]
        infected[a] = 1
infected.pop(0)
print(*infected,sep="")