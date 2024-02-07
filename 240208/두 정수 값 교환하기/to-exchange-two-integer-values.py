def swap(a,b):
    a,b= b,a
    return a,b



n,m = map(int,input().split())
print(*swap(n,m))