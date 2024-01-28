arr = input()

arr= list(arr)

'''idx = arr.index('e')
arr.pop(idx)'''
arr.pop(arr.index('e'))

print(''.join(arr))