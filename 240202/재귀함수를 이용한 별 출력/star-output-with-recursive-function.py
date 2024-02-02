def f(idx): # 1부터 idx 번째 줄 까지 별을 출력하는 
    #종료조건: 1부터 0번째 줄 까지 별을 출력 
    if idx ==0:
        return
    #재귀함수 
    f(idx-1)
    print('*'*idx,end="")
    print()

n= int(input())
f(n)