n= int(input())


cnt1 =0
start = 11
while cnt1 <n:

    cnt1 +=1 
    cnt2=0
    num = start
    while cnt2 <n:
        
        print(num,end=" ")
        num+=2
        cnt2 +=1

    start +=2

    print()