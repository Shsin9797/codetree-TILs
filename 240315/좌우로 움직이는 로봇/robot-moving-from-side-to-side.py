n,m = map(int,input().split())

ap = 0
bp = 0
Alist = [ap]
Blist = [bp]

#A
for _ in range(n):
    t1,d = input().split()
    t1= int(t1)
    for i in range(t1):
        if d =='L':
            ap -= 1 
        else:
            ap += 1
        Alist.append(ap)


#B
for _ in range(m):
    t2,d = input().split()
    t2 =int(t2)
    for i in range(t2):
        if d =='L':
            bp -= 1 
        else:
            bp += 1
        Blist.append(bp)


la = len(Alist) 
lb = len(Blist) 

# t1, t2 중 긴시간 판별 
if la >= lb:
    t=la
    addNum= Blist[-1]
    for _ in range(lb,la):
        Blist.append(addNum)
else:
    t= lb
    addNum = Alist[-1]
    for _ in range(la,lb):
        Alist.append(addNum)



cnt =0 
#체크 
for i in range(2,t):
    if (Alist[i-1] != Blist[i-1]) and (Alist[i] == Blist[i]) :
        cnt +=1

print(cnt)