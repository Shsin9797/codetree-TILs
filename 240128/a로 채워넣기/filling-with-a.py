s = input()
arr= list(s)
arr[1],arr[-2]='a','a'

result= "".join(arr)
print(result)