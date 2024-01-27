start, end= map(int,input().split())
cnt3 =0

#시작 ~끝 까지 약수의 개수 세기
for i in range(start,end+1):
    
    cnt =0 
    for j in range(1,i+1): #자기자신 빼먹으면 안됨... 
        if i%j ==0:
            cnt +=1
     
    if cnt == 3: # 체크 위치 주의 
        cnt3 +=1 

print(cnt3)