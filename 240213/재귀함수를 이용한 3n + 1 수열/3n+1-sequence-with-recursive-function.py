n= int(input())

def f(idx):#1~ n 까지 계산횟수를 반환
    #종료조건 
    if idx ==1:
        return 0
    
    #재귀호출
    if idx%2==0:
        return f(idx/2)+1
    else:
        return f(idx *3 +1)+1

print(f(n))