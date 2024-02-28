yoil = ["Mon", 'Tue', 'Wed', "Thu", "Fri", 'Sat', 'Sun']
dayNum = [0,31,29,31,30,31,30,31,31,30,31,30,31]

m1,d1,m2,d2 =map(int,input().split())
A = input()

kIdx = 0 
aIdx = yoil.index(A)
aCnt = 0 

while True :
    #A 값 세기 
    if kIdx == aIdx:
        aCnt +=1
    #종료조건 
    if m1 ==m2 and d1 ==d2 : 
        break
    
    # 값변경
    #일 값 변경
    d1 +=1 
    if d1 > dayNum[m1]: 
        m1 +=1
        d1 =1
    #요일 값 변경 
    kIdx +=1  #aIdx 가 아니라 kIdx 를 변경해야한다
    if kIdx >= len(yoil):
        kIdx =0 
    


#출력 
print(aCnt)