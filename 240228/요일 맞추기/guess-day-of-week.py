m1, d1, m2, d2 = map(int,input().split())
y2011 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
yoil = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
idxY = 0

while True:
    if m1==m2 and d1==d2:
        break
    
    #두번째가 큰 경우 값을 증가시켜준다 
    if m1 < m2 : 
        d1 +=1 
        idxY +=1
    elif m1 == m2 and d1 <d2:
        d1 +=1 
        idxY +=1
    elif m1 ==m2 and d1> d2 :
        d1 -=1
        idxY -=1
    elif m1>m2 :
        d1 -=1
        idxY-=1

    #값의 범위 체크
    if d1 > y2011[m1]:
        m1 +=1
        
        #월도 체크해주기...
        if m1 >12: 
            m1 =1
        elif m1 < 1:
            m1 =12
            
        d1 = 1 

    elif d1 <1:
        m1 -=1
        
        #월도 체크해주기...
        if m1 >12: 
            m1 =1
        elif m1 < 1:
            m1 =12
        
        d1 = y2011[m1]
    
    #월도 체크해주기...
    if m1 >12: 
        m1 =1
    elif m1 < 1:
        m1 =12
    
    #요일 법위 체크
    if idxY >= len(yoil):
        idxY =0
    elif idxY <0:
        idxY =6


print(yoil[idxY])