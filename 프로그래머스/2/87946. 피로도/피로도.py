from itertools import permutations

def solution(k, dungeons):
    li = list(permutations(dungeons, len(dungeons)))
    max_cnt =0 
    for duns in li: 
        kk= k
        cnt = 0
        
        for elem in duns: 
            if kk < elem[0]:
                break
            kk -= elem[1]
            cnt +=1
        max_cnt = max(max_cnt,cnt)
    
    
    return max_cnt