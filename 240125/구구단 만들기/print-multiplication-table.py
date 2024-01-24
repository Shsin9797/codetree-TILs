a,b = map(int,input().split())

for i in range(1,10):
    for j in range(b,a-1,-2):
        print(f"{j} * {i} = {j*i}",end=" ") #j 인지 b 인지 잘보기
        if j > a:
            print("/",end=" ")
        else:
            print()