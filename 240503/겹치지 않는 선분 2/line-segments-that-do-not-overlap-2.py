n= int(input())

arr=[]
for _ in range(n):
    x1,x2 = map(int,input().split())
    arr.append(((x1,0),(x2,1)))
#print(arr)
#끝점이 .. . x1은 다른 직선에 비해 작은데 x2는 크던지.. 
cnt = 0 

for i in range(n):#직선 1개 고르기 
    parall= True
    for j in range(i+1, n): #다른 직선 1개 고르기 
        if i != j : 
            continue
        print(arr[i])
        x1,x2 = arr[i][0][0],arr[i][1][0]
        print('x1',x1,'x2',x2)
        x3,x4= arr[j][0][0],arr[j][1][0]
        print('x3',x3,'x4',x4)

        if x1 < x3 and x2>x4:
            parall =False
            break
        elif x1 > x3 and x2 < x4: 
            parall =False
            break
            
    if parall:
        print(i,j ,'parall')
        cnt +=1 

print(cnt)