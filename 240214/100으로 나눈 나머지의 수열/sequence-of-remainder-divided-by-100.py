def f(idx): # idx-1 와 idx-2를 100으로 나눈 나머지
    #종료조건 
    if idx ==1 : 
        return 2
    elif idx ==2:
        return 4
    #점화식 
    else:
        return (f(idx-1)* f(idx-2))%100 

n=int(input())
print(f(n))