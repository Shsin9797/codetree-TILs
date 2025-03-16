N, L = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

for hh in h:
    if L >= hh:
        L += 1  
    else:
        break 

print(L)
