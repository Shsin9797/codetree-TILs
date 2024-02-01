def bae(n):
    first = n//10
    sec = n%10 
    sum1 = first +sec
    return n%2==0 and sum1%5==0


n= int(input())
isgood= bae(n)

if isgood : 
    print("Yes")
else:
    print("No")