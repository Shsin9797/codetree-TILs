class Student:
    def __init__(self,n,h,w):
        self.n=n
        self.h=h
        self.w=w

n=int(input())
stList= []
for _ in range(n):
    n,h,m = input().split()
    h,m =int(h),int(m)
    stList.append(Student(n,h,m))

stList.sort(key= lambda x: (x.h,-x.w))

#출력
for st in stList:
    print(st.n,st.h, st.w)