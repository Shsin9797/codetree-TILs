n= int(input())
arr=list(map(int,input().split()))


print(*sorted(arr))
print(*list(reversed(sorted(arr)))) #reversed 는 내림차순 정렬이 아니라.. 현재 상태를 뒤집어주는거임..