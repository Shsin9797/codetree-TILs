import sys 

n= int(input())
li= [int(input()) for _ in range(n)]
min_len = sys.maxsize #-sys.maxsize()

for s in range(n): #start

    sum_len=0
    

    for e in range(n):#end 계속 바꿔야함 end를 바꿔가며,, 사람거리 구하기 
        idx=s
        go= (e-s+n)%n #두거리의 차이 
        
        if go ==0 : #이동거리가 없는경우 구하지 않는다.
            continue # break 하면 해당 s 자리에서 시작하는거 구하는거 끝남..   e 가 안돌아서..
        
        
        for walk in range(go):
            idx = (idx+1)%n
            sum_len += (walk+1)*li[idx]
        #print('(s,e): ',s,e,'go',go)
        #print(idx+1,'번 방에 있는 사람수',li[idx])

    print('(s,e): ',s+1,e+1,'go',go) 
    print('sumLen',sum_len) 
    if sum_len:
        min_len= min(min_len,sum_len)
    
print(min_len) #min 값 구하는거임