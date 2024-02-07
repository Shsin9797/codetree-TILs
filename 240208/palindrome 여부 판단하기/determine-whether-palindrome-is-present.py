def palindrome(arr):

    arr = arr[::-1]
    return arr



A=input()
if A == palindrome(A):
    print('Yes')
else:
    print('No')