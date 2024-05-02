import sys

n= int(input())
spot = []
for _ in range(n):
    x,y = map(int,input().split())
    spot.append((x,y))

#print(spot)

arr= [] 
#점빼기 
for i in range(n):
    #초기화 해줘야함 위치주의 
    x_min,x_max,y_min,y_max = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize 
    
    for j in range(n): 
        if i==j:
            continue 
        
        
        #점 값 찾기  -> 점 값들의 차이가 가장 작아야함.. 
        #print(x_max,x_min)
        x,y = spot[j]
        #print(x,y)
        if x < x_min:
            x_min = x 
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y 
        if y > y_max:
            y_max = y
        
        #print(x_max,x_min)
        #넓이 구하기 
        y_len = y_max - y_min
        x_len = x_max - x_min
        arr.append(y_len*x_len)

print(arr)
print(min(arr))