n= int(input())
li = []
while True:
    if n <2: 
        li.append(n)
        break

    li.append(n%2)
    n //= 2 

print(*li[::-1],sep="")