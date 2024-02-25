class Student:
    def __init__(self,n,h,w):
        self.n=n
        self.h=h
        self.w=w


stList=[]
#학생 정보받기
for _ in range(5):
    n,h,w=input().split()
    h,w= int(h),float(w)
    stList.append(Student(n,h,w))

#이름 오름차순 출력
stList.sort(key = lambda x : x.n)
print("name")
for st in stList:
    print(f"{st.n} {st.h} {st.w:.1f}") # 부족.. 

print() 

#키 내림차순 정렬
stList.sort(key= lambda x : -x.h)
print("height")
for st in stList:
    print(f"{st.n} {st.h} {st.w:.1f}")