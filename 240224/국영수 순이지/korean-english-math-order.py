class Student:
    def __init__(self,n,k,e,m):
        self.n=n
        self.k=k
        self.e=e
        self.m=m

n=int(input())
sts=[]
for _ in range(n):
    n,k,e,m =input().split()
    k,e,m =int(k),int(e),int(m)
    sts.append(Student(n,k,e,m))

sts.sort(key= lambda x : (-x.k,-x.e,-x.m))
for s in sts:
    print(s.n,s.k,s.e,s.m)