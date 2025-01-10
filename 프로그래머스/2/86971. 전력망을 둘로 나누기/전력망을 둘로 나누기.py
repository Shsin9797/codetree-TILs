from collections import defaultdict, deque

def solution(n, wires):
    def count_connected(graph, start, excluded):
        visited = set()
        queue = deque([start])
        count = 0
        
        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                count += 1
                
                for neighbor in graph[current]:
                    # excluded로 지정된 노드로의 연결은 무시
                    if neighbor not in visited and (current, neighbor) != excluded and (neighbor, current) != excluded:
                        queue.append(neighbor)
        
        return count

    # 그래프 생성
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = n  # 최대 차이로 초기화
    
    # 각 전선을 끊어보며 최소 차이 계산
    for v1, v2 in wires:
        # v1을 시작점으로 하는 전력망의 송전탑 수 계산
        count1 = count_connected(graph, v1, (v1, v2))
        # v2를 시작점으로 하는 전력망의 송전탑 수 계산
        count2 = count_connected(graph, v2, (v1, v2))
        
        # 차이 계산 및 최소값 갱신
        diff = abs(count1 - count2)
        min_diff = min(min_diff, diff)
    
    return min_diff