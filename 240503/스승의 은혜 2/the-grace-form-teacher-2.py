n,b =map(int,input().split())
p=[0]*n

#선물가격 세팅
for i in range(n):
    p[i] =int(input())
    
p=sorted(p)
max_cnt = 0 

#반값할인할 애 정하기 
for i in range(n):
    #초기화 
    pp= p[:]
    bb=b
    cnt = 0

    #반값할인
    pp[i] /=2 #p 가 아니라 pp 를 절반띄기 

    #오름차순 정렬
    pp.sort() #sort(pp)
    
    #명수 세기    
    for k in range(n):
        bb -= pp[k]
        if bb >= 0:
            cnt =k+1
            continue 
        else:
            #cnt= k
            break
    
    #if max_cnt == cnt : #이런거 하지말기.. 
    #    break 

    max_cnt =max(max_cnt,cnt)

'''
원본을 오름차순 정렬했을때 
14, 22, 32, 34, 70, 98, 128, 128, 130, 140, 140, 156, 156 이순서로 나오고, 
첫 10개인14, 22, 32, 34, 70, 98, 128, 128, 130, 140 를 합하면 
796으로, 예산인 863과67 만큼 차이가 납니다. 

이때 140 을 반값 하면 70이 되고, 
14, 22, 32, 34, 70,70, 98, 128, 128, 130, 140 까지 해서 
'''
print(max_cnt)