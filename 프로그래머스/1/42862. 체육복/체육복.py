def solution(n, lost, reserve):
    li = [1 for _ in range(n)]
    
    for i in reserve: 
        li[i-1] +=1
    
    for i in lost:
        li[i-1] -=1
    
    for k in range(n):
        if li[k] ==0 :
            if  0<= k-1 <n and li[k-1] >1:
                li[k-1] -=1
                li[k] +=1
            elif  0<= k+1 <n and li[k+1] >1:
                li[k+1] -=1
                li[k] +=1
    cnt= 0 
    for i in range(n):
        if li[i] != 0:
            cnt +=1
    answer = cnt
    return answer