n= int(input())
li = [ list(map(int,input().split())) for _ in range(n)]
lenth = [] 



#건너뛸애 정하기 
for i in range(1,n-1):
    sumlen=0
    bx,by = li[0][0], li[0][1]
    #하나씩 순회하면서 건너뛸애 빼고 길이 sumlen 구하기 
    #print('제외번지:',i)
    for j in range(1,n):
        
        if i == j : 
            continue
        ax,ay= li[j][0],li[j][1] #j로 써야함!!
        #print('b:(',bx,by,'a:(',ax,ay)
        #길이구하고 
        sumlen += abs(ax-bx) + abs(ay-by)
        # 전 값 변경 
        bx,by = ax,ay 
    lenth.append(sumlen)
#print(lenth)
print(min(lenth))