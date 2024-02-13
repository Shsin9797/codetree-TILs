n= int(input())
arr = list(map(int,input().split()))

def f(idx):# 0 ~ (idx-1)까지 최댓값 반환
    # 종료조건 :  
    if idx == 0:
        return arr[0]
    
    #재귀호출 0~ (n-1) 까지 최댓값 반환
    cand1 = f(idx-1)
    cand2 = arr[idx-1]
    if cand1 > cand2 :
        return cand1 
    else:
        return cand2
    
print(f(n))