def isTwo(x):
    a= x[0]
    for i in range(len(x)):

        if x[i] != a:
            return True    

#A= list(input().split()) <-split 이 안먹음..
A =input()

if isTwo(A):
    print("Yes")
else:
    print("No")