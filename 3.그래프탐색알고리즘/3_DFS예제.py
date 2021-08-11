"""
[DFS(Depth-First Search) - 깊이 우선 탐색]

# 출력 예시 
1 2 7 6 8 3 4 5
"""

# DFS 메서드 정의
def dfs( graph , v, visited ):
    # 현재 노드를 방문처리 
    visited[v] = True
    #print(v, end = ' ')
    #확인용 print
    print(v , end= ' ')
    print(f" graph >> {graph}")
    print(f" visited >> {visited}")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[v]:
        print(f" i = {i}")
        if not visited[i]:
            dfs(graph , i , visited )


# ※ 1번 인덱스가 1번 노드에 인접한(연결된) 노드 나타냄
#    2차원 리스트의 0번 노드는 비워 두는게 좋음 
# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정로르 표현 ( 1차원 리스트 )
visited = [False] * 9 

# 정의된 DFS 함수 호출 
dfs(graph , 1, visited)