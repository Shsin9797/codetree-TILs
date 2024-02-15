# 정점 방문처리위차 주의!!!! 

n,m= map(int,input().split())

#정점리스트 생성 
vertex = [[] for _ in range(n+1)]
#방문 리스트 생성
visited = [0 for _ in range(n+1)]


#DFS 함수 생성 
def DFS(v):#방문 정점 지정하면 연관된거 다 찾아줌 
    #### 여기에서.. 방문표시 하는게 좋다..
    
    for i in vertex[v]:

        if not visited[i]:
            visited[i] =1  # 쌤은.. 재귀함수가 호출이 되는 순간에 방문표시하심... #해설은 방문하기전에 방문 처리 해주고 .. 방문... 
            DFS(i)



#간선 체크 
for i in range(m):
    x,y = map(int,input().split())
    vertex[x].append(y)
    vertex[y].append(x)

#dfs 탐색 
DFS(1)
visited[1] = 0 #첫방문 정점은 0으로 바꾸기 ... 
print(sum(visited))