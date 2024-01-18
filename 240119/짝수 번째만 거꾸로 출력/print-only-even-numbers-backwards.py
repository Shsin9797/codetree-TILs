A = input()
if len(A)%2==0:
    print(A[::-2])
else:
    print(A[-2::-2])