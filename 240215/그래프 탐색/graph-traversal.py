n,m= map(int,input().split())

#정점리스트 생성 
vertex = [[] for _ in range(n+1)]
#방문 리스트 생성
visited = [0 for _ in range(n+1)]


#DFS 함수 생성 
def DFS(v):#방문 정점 지정하면 연관된거 다 찾아줌 
    for i in vertex[v]:
        if not visited[i]:
            visited[i] =1 
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