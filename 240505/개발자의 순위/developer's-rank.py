'''답지풀이
# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(k)
]

ans = 0

# 모든 쌍에 대해서 불변의 순위인 쌍을 찾습니다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # i번 개발자가 j번 개발자보다 항상 높은 순위인지 여부를 확인합니다.

        # i와 j가 같을 경우 넘어갑니다.
        if i == j:
            continue
            
        # correct : i번 개발자가 j번 개발자보다 항상 높은 순위일때 true
        correct = True

        # k번의 모든 경기에 대해서 두 개발자의 위치를 찾고,
        # 하나라도 i번 개발자가 더 뒤에 있으면 correct를 false로 바꿉니다.
        for lists in arr:
            index_i = lists.index(i)
            index_j = lists.index(j)

            if index_i > index_j:
                correct = False

        if correct:
            ans += 1
    
print(ans)

'''
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