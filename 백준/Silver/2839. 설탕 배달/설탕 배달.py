N = int(input())
li = [-1] * 5001
li[3] = 1
li[5] = 1

for i in range(6, N + 1):
    if li[i - 3] != -1 and li[i - 5] != -1:
        li[i] = min(li[i - 3], li[i - 5]) + 1
    elif li[i - 3] != -1:
        li[i] = li[i - 3] + 1
    elif li[i - 5] != -1:
        li[i] = li[i - 5] + 1

print(li[N])