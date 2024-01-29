A =input()
B=input()

n= 0 


"""while A!=B: #### 불가능한 경우 체크하려면 이거 하면 안됨.. 
    A = A[-1]+A[:-1]
    n+=1
    """
isSame= False 
for i in range(len(A)-1):
    A=A[-1]+A[:-1]
    n +=1 
    if A==B:
        isSame = True
        break


if isSame:
    print(n)
else:
    print(-1)