A,B = input().split()

numA=""
numB=""
for i in A:
    if not i.isdigit():
        break
    numA +=i

for j in B:
    if not j.isdigit():
        break
    numB += j

print(int(numA)+int(numB))