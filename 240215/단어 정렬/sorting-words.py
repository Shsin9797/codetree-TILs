n = int(input())
arr =[]
for i in range(n):
    arr.append( input())


print(*sorted(arr),sep="\n") # sep 으로 구분자 적어주기.. 안적으면 기본 스페이스바