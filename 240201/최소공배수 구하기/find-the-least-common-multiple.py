def find_be(n,m):

    if n>m :
        n,m= m,n 
    be =m 
    while True:
        if be%n ==0 and be%m ==0 :
            break
        be +=1 
    print(be)




n,m = map(int,input().split())
find_be(n,m)