n,M,d,s = map(int,input().split())
 
ptm=[[] for _ in range(n+1)] #치즈 먹은 초와 먹은 치즈 저장 ****
#print(ptm)
pti= [0]*(n+1) #아픈시간 

#사람- 시간 - 먹은치즈 저장 : 치즈 여러개 먹음... 
for _ in range(d):
    p,m,t = map(int,input().split())
    ptm[p].append((t,m))    

#print(ptm)

for _ in range(s):
    p,t = map(int,input().split())
    pti[p]=t

print(ptm)
print(pti)

#상한 치즈 고르기 
rot =[0]*(M+1) #문자 안바뀌게 주의

for i in range(1,n+1): # 사람 선택하기 
    li = ptm[i] # 모든사람 값이 존재하는건가..? 
    
    for t,m in li:    
        if t+1 == pti[i]:
            rot[m] =1 

#print(rot)
print(ptm)
print(rot)
cnt= 0
#치즈 먹은사람 찾기 -> 빼도 될듯 xx 빼면안됨.. 제대로 기록안된게 있어서 
for i in range(1,n+1):
    li = ptm[i]
    #print(ptm)
    
    #print(i,':',li)
    for t,m in li:
        if rot[m] == 1 :
            cnt +=1 

print(cnt)