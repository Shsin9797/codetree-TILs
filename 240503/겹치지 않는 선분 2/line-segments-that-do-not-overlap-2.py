n= int(input())

arr=[]
for _ in range(n):
    x1,x2 = map(int,input().split())
    arr.append((x1,x2))
#print(arr)
#끝점이 .. . x1은 다른 직선에 비해 작은데 x2는 크던지.. 
cnt = 0 

for i in range(n):#직선 1개 고르기 
    
    parall= True
    
    #for 문 
    for j in range(n): #다른 직선 1개 고르기 
        if i == j : #등호... 
            continue
        #print(i,':',arr[i])
        x1,x2 = arr[i]
        #print(j,':',arr[j])
        x3,x4 = arr[j] # j여야했다... 
        #print('--------')
        
        if ((x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4 )):
            parall = False
            break

    if parall:
        cnt +=1 

print(cnt)