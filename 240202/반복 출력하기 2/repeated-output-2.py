def f(idx):
    #종료조건
    if idx ==0:
        return

    #재귀조건
    f(idx-1)

    #구문실행
    print("HelloWorld")


n=int(input())
f(n)