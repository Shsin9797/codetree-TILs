A=input()#입력양식 잘보기 .. 
B= input()

numA=""
numB=""
for i in A:
    if i.isdigit():
        numA+=i

for j in B:
    if j.isdigit():
        numB+=j

print(int(numA)+int(numB))