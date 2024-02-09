def f(a,b):
    if a>b:
        #a,b = b,a  자리 바꾸는거아님..
        a += 25
        b *= 2
    else:
        a*=2
        b +=25
    return a,b




a,b = map(int,input().split())
a,b=f(a,b)
print(a,b)