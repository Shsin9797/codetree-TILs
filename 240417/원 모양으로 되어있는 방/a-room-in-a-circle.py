import sys 

n= int(input())
li= [int(input()) for _ in range(n)]
max_len = 0 #-sys.maxsize()
for s in range(n): #start
    sum_len=0
    for e in range(n):#end
        if e < s:
            print('시작점이 더 크다',n-abs(s-e))
            sum_len += (n-abs(s-e))*li[e]
        elif s < e:
            print(abs(s-e))
            sum_len += abs(s-e)*li[e]

    print('sumLen',sum_len) 
    max_len =max(max_len,sum_len)
    

print(max_len)