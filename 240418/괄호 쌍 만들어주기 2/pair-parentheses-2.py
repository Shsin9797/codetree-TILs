A=input()
lA= len(A)
cnt=0

for i in range(lA-3): # 여기 2아니라 3빼줘야하는거 맞나..
    if A[i]=='('and A[i+1]=='(':
        for j in range(i+2,lA-1):
            if A[j]==')'and A[j+1] ==')':
                cnt+=1

print(cnt)