class Student:
    def __init__(self,n,p1,p2,p3):
        self.n=n
        self.p1=p1
        self.p2=p2
        self.p3=p3


n=int(input())
sts=[]
for _ in range(n):
    n,p1,p2,p3 =input().split()
    p1,p2,p3 =map(int,[p1,p2,p3])
    sts.append(Student(n,p1,p2,p3))

sts.sort(key=lambda x: x.p1+x.p2+x.p3)
for i in sts:
    print(i.n,i.p1,i.p2,i.p3)