m1,d1,m2,d2 =map(int,input().split())
y2011 = [0,31,28,31,30,31,30,31,31,30,31,30,31]

day = 1
while True:
    if m1 ==m2 and d1 ==d2:
        break
    
    d1 +=1
    day +=1

    if d1 > y2011[m1]:
        m1 +=1
        d1=1

print(day)