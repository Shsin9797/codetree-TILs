n= int(input())

li=[0 for _ in range(101)]
personList =[]
for _ in range(n):
    idx, alpha = input().split()
    idx = int(idx)
    li[idx]=alpha
    personList.append(idx)

personList.sort()
max_len = 0 
#personList 값 어디부터 어디까지 를 사진의 크기로 결정할지 결정 
for start in range(len(personList)):
    for end in range(start+1,len(personList)):
        Gcnt=0
        Hcnt=0
        # PersonList 순회 
        for i in range(start,end+1):
            if i >= len(personList):
                break
            
            idx = personList[i]
            if li[idx]=='G':
                Gcnt +=1
            elif li[idx] =='H':
                Hcnt +=1
        
        if Gcnt == Hcnt or (Gcnt==0 and Hcnt > 1) or (Gcnt >1 and Hcnt==0):
            max_len= max(max_len, personList[end]-personList[start])
        

print(max_len)