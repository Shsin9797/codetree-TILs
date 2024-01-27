n= int(input())
if n>1:
    for i in range(2,n+1):
        isSosu = True
        #소수확인
        if i ==2:
            print(i,end=" ")
            continue
        for j in range(2,n):
            if i%j ==0:
                isSosu=False
        if isSosu:
            print(i,end=" ")