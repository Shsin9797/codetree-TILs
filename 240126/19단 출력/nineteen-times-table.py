n= 19 

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{i} * {j} = {i*j}",end="")
        if j%2 ==0 or j == n :  #j == n  인거, and 가 아니라 or 써야하는거 주의
            print()
        else:
            print(" / ",end="")
    #print() #한타임 끝나면 띄워줘야함..