def solution(sizes):
    # 앞에께 무조건 더크도록 정렬 
    l= len(sizes)
    max0,max1=0,0
    for i in range(l):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        # 앞의꺼 최댓값, 뒤의꺼 최댓값 찾기
        if sizes[i][0] > max0:
            max0 = sizes[i][0]
        if sizes[i][1] > max1:
            max1 = sizes[i][1]
             
    answer = max0*max1
    return answer