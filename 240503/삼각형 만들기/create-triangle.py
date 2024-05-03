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
    
    ga=0
    se=0

    if x1==x2 :
        se= abs(y3-y2)
    elif x2==x3 :
        se = abs(y2-y1)
    elif x1==x3:
        se = abs(y1-y2)

    if y1==y2 :
        ga= abs(x3-x2)
    elif y2==y3 :
        ga = abs(x2-x1)
    elif y1==y3:
        ga = abs(x1-x2)
    
    
    if ga and se :
        return ga*se 
    else:
        return ga*se

#점 세개 구하기
li=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            print(spots[i],spots[j],spots[k])
            li.append(isSam(spots[i],spots[j],spots[k]))
print(li)

#최대넓이에 2 곱한값 출력 
print(max(li))