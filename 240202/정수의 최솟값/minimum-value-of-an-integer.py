def findMin(*args):
    m = min(args)
    print(m)

a,b,c = tuple(map(int,input().split()))
findMin(a,b,c)#이거왜 바로 안에 넣으면 안되는건지..