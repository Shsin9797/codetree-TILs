A,B,C =map(int,input().split())
max_num = 0 

for a in range(C):
    for b in range(C):
        num = A*a +B*b
        if num <= C:
            max_num=max(num,max_num)

print(max_num)