def f1(idx): # 1부터 idx 까지 숫자를 출력
    #종료조건
    if idx==0:
        return
    #재귀
    f1(idx-1)
    print(idx,end=" ")

def f2(idx): #idx 부터 1까지 출력 
    #종료조건 
    if idx == 0:
        return
    #재귀 
    print(idx,end=" ")
    f2(idx-1)


n =int(input())

f1(n)
print()
f2(n)