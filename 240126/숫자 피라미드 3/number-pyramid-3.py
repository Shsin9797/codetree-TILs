n= int(input())

for i in range(1,n+1):
    for j in range(1,i+1): # 그냥 i쓰면 0부터 시작함
        print(i*j,end=" ")
    print()