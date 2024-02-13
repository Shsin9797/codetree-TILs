def f(idx): #  ⌊ n/3⌋ 번째 수와 (N-1)번째 수의 합
    #종료조건
    if idx==1:
        return 1
    elif idx==2:
        return 2
    return f(idx//3)+f(idx-1)

n= int(input())
print(f(n))