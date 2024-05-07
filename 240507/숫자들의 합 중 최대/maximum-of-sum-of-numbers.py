#a=list('1234') string 을 list 처리해주면 각각 떼어내준다...
x,y = map(int,input().split()) # int 로 바꿔주긴해야함.. 그래야  for 문 사용가능

max_a=0

for i in range(x,y+1):
    a= list(str(i))
    suma=0
    for k in a:
        suma += int(k)
    max_a=max(max_a,suma)

print(max_a)