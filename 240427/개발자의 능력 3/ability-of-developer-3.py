import sys

arr = list(map(int,input().split()))
sum_arr= sum(arr)

min_cha= sys.maxsize

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            #sum_abil1=0  없어도 될듯 
            if i != j and j !=k and i != k : 
                sum_abil1 = arr[i] + arr[j] +arr[k]
                sum_abil2 = sum_arr - sum_abil1
                cha_abil = abs(sum_abil2 - sum_abil1)
                min_cha= min(min_cha,cha_abil)

print(min_cha)