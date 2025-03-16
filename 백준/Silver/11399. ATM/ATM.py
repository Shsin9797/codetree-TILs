N = int(input()) 
P = list(map(int, input().split()))  

P.sort()

time = 0  
wait = 0  

for t in P:
    wait += t  
    time += wait 

print(time)