def f(x):#x가 1이될때까지 2로 나누는 함수 
    #종료조건 
    if x== 1 :
        return 0
    """elif x ==0:
        return 0
        없어도 되는 부분... """
    # 재귀 : f(x//2) 부르고 cnt +=1 
    if x %2 ==0:
        n= f(x//2)+1
    else:
        n=f(x//3)+1
    return n



n= int(input())
print(f(n))