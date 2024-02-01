def findMin(*args):
    m = min(args)
    print(m)

a,b,c = tuple(map(int,input().split()))
findMin(a,b,c)