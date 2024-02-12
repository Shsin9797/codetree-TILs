def f(idx): # idx 홀수 : 1~ idx 홀수합 / idx 짝수 : 2~idx 짝수합 
    #종료조건 
    if idx ==1:
        return 1
    if idx ==2:
        return 2

    return idx+f(idx-2)



n= int(input())
print(f(n))