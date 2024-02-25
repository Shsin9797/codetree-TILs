class Student:
    def __init__(self,h,w,num):
        self.h=h
        self.w=w
        self.num=num
    

n=int(input())
stList=[]
cnt =0
# 학생값 저장
for _ in range(n):
    h,w= map(int,input().split())
    cnt += 1
    stList.append(Student(h,w,cnt))
    

# 정렬
stList.sort(key= lambda x: (-x.h,-x.w,x.num))

#출력 키 뭄무게 번호
for st in stList:
    print(st.h,st.w,st.num)