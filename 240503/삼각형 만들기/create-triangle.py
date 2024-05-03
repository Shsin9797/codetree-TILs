n= int(input())
spots= [] 
for _ in range(n):
    spots.append(tuple(map(int,input().split())))

#삼각형 함수 
#우리가 원하는 삼각형인지 확인하는 함수 
def isSam(i1,i2,i3):
    x1,y1 = i1 
    x2,y2 = i2
    x3,y3 = i3
    
    if x1 != x2 and x2 != x3:
        return 0
    
    if y1 != y2 and y2 != y3 : 
        return 0 

    area = abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))
    return area

    

#점 세개 구하기
li=[]
for i in range(n):
    for j in range(n):
        for k in range(n): #이거 j+1 아니라 0 ~ n-1 까ㅣ인지.. 
            if i==j or j==k or k==i:
                continue
            #print(spots[i],spots[j],spots[k])
            li.append(isSam(spots[i],spots[j],spots[k]))
#print(li)

#최대넓이에 2 곱한값 출력 
print(max(li))