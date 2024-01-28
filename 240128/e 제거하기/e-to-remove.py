arr = input()

arr= list(arr)

idx = arr.index('e')
arr.pop(idx)

print(''.join(arr))