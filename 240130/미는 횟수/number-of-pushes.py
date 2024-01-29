A =input()
B=input()

n= 0 


"""while A!=B: #### 불가능한 경우 체크하려면 이거 하면 안됨.. 
    A = A[-1]+A[:-1]
    n+=1
    """

for i in range(len(A)-1):
    A=A[-1]+A[:-1]
    n +=1 
    if A==B:
        break

print(n)