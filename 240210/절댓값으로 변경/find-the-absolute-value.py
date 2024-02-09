def f(k):
    #k = list(map(abs,k))
    for i in range(len(k)):
        k[i] = abs(k[i])

n=int(input())
li= list(map(int,input().split())) # 여기에도 list 붙여줘야할듯.. 
f(li)
print(*li)