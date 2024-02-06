def f(x):
    #종료조건 
    if x<10:
        return x**2
    return f(x//10) + (x%10)**2

n= int(input())
print(f(n))