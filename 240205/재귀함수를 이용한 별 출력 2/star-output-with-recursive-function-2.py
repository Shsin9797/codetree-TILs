def f(x):
    #종료조건 
    if x ==0:
        return
    #재귀호출 
    print("* "*x)
    f(x-1)
    print("* "*x)



n= int(input())
f(n)