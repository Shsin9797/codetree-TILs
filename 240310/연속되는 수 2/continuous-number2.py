n= int(input())
li=[]
for _ in range(n):
    num = int(input())
    li.append(num)

cnt =0 
cntList= [] 
for i in range(n):
    if i ==0 or li[i-1]!= li[i]:
        cntList.append(cnt)
        cnt =1
    else:
        cnt +=1

print(max(cntList))