n,b =map(int,input().split())
p=[0]*n

#선물가격 세팅
for i in range(n):
    p[i] =int(input())

max_cnt = 0 
#반값할인할 애 정하기 
for i in range(n):
    #초기화 
    pp= p[:]
    bb=b
    #반값할인
    p[i] /=2
    #오름차순 정렬
    pp.sort() #sort(pp)
    #print(pp)
    
    #명수 세기 
    cnt = 0 
    for k in range(n):
        bb -= pp[k]
        if bb >= 0:
            #cnt +=1
            continue 
        else:
            cnt= k+1
            break
    
    max_cnt =max(max_cnt,cnt)

print(max_cnt)