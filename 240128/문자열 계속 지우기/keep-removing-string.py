A = input()
B= input()

while B in A:
    idx= A.index(B)
    A= list(A)
    for i in range(len(B)):
        A.pop(idx)

    
    A = ''.join(A)

print(A)