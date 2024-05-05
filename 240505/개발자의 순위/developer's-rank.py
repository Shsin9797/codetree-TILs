k,n = map(int,input().split())
arr=[]
for _ in range(k):
    li=list(map(int,input().split()))
    li2=[0]*(n+1) #개발자 번호 #개발자수는 k 가 아니라 n 임 
    for t in range(len(li)): 
        t=t+1 # 등수 
        li2[li[t-1]] = t  #개발자 번호에 등수 넣기  
    arr.append(li2)

#print(arr)

# 완전탐색으로 개발자 각각의 등수 비교 
cnt = 0  # 항상 순위 불변인 경우 

#개발자 선택 
for i in range(1,n+1):# 첫번째 개발자 :a  # 0 부터 세면 안됨  1부터 세어야 됌
    for j in range(1,n+1):# 두번째 개발자 : b  
        
        if i ==j :
            continue 

        #개발자의 순위 탐색 
        isUnchanged=True 
        #순위 바뀌었는지 확인하는 구문 
        for game in arr: #게임선택 
            if game[i] > game[j] :
                isUnchanged= False 
                break # 얘둘은 가망없다 게임 더 확인할 필요없음 
        if isUnchanged:
            cnt +=1 #a 가 항상 b 보다 높은 순위였다.(낮은값 )

print(cnt) # 왜 두배값이 나오지.. .