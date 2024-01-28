A=input()

order = input()
for o in order:
    if o =='L':
        A=A[1:]+A[0]
    elif o =='R':
        A=A[-1]+A[:-1]
    
print(A)