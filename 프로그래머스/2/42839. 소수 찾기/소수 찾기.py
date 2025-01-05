from itertools import permutations

def solution(numbers):
    
    #소수 : 1과 자기자신만을 약수로 갖는 수 
    num_set = set() 
    l= len(numbers)
    
    ## 제시된 값으로 가능한 숫자만들기 
    for i in range(l):
        nums = permutations(numbers,i+1)
        #print(list(nums))
        num_set |= set(map(int,map("".join, nums)))
    
    print(num_set)
    
    ## 소수찾기 (에라토스 테네스의 체 활용)
    num_set -= set(range(0,2)) # 0과 1을 빼준다
    lim = int(max(num_set)**0.5) +1
    print(lim)
    
    for k in range(2,lim):
        num_set -= set(range(k*2, max(num_set)+1,k)) # i 로 안적게 주의..

    answer = len(num_set)
    return answer