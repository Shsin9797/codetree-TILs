X,Y = map(int,input().split())


cnt =0 
#값저장
for i in range(X,Y+1):
    numlist =[] 
    numdict={}
    for n in list(str(i)):
        if n not in numlist:
            numlist.append(n)
        if n in numdict.keys():
            numdict[n] += 1 
        else:
            numdict[n] =1
    #값 카운팅

    if len(numlist)==2 :
        li=[]
        for k in numdict.keys():
            li.append(numdict[k])
        if ((li[0]==1 and li[1] !=1 ) or (li[1]==1 and li[0] !=0)):
            cnt +=1

print(cnt)