n= int(input())

Sum =0 

for _ in range(n):
    Sum += int(input())

Sum = str(Sum)

print(Sum[1:]+Sum[0])