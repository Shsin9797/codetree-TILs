class Person:
    def __init__(self,name,code,area):
        self.name = name
        self.code = code 
        self.area = area

n= int(input())
dial = []
for _ in range(n):
    info = input().split()
    p = Person(info[0],info[1],info[2])
    dial.append(p)

#순서 정하는 거
lateP= dial[0].name
idx = 0
for i in range(n):
    if dial[i].name > lateP:
        lateP = dial[i].name
        idx = i

print(f"name {dial[idx].name}" )
print(f"addr {dial[idx].code}")
print(f"city {dial[idx].area}")