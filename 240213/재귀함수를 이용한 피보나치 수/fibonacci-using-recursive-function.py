def f(idx): # 1~idx 까지 구한값 
    #종료조건 
    if idx ==1:
        return 1
    if idx == 2:
        return 1
    #점화식 f(idx)= f(idx-1)+f(idx-2)
    return f(idx-1)+f(idx-2)

n=int(input())
print(f(n))