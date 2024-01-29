A = input()
sumA=0 

for i in A:
    if i.isdigit():
        i =int(i)
        sumA +=i

print(sumA)