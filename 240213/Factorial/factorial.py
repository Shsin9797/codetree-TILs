def f(idx): #1~idx 까지 곱한 값
    #종료조건 
    if idx== 0 :
        return 1
    elif idx == 1:
        return 1 
    elif idx == 2:
        return 2
    elif idx ==3:
        return 6
    
    #재귀호출 : 점화식 f(idx) =idx*f(idx-1)
    return idx* f(idx-1)

n= int(input())
print(f(n))