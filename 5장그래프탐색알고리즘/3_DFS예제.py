"""
[DFS(Depth-First Search) - 깊이 우선 탐색]
  - DFS 는 '깊이 우선 탐색'이라고도 부르며 그래프에서 '깊은 부분을 우선적으로 탐색하는 알고리즘'입니다.
  - DFS 는 '스택 자료구조(혹은 재귀 함수)를 이용'하며, 구체적인 동작 과정은 다음과 같습니다. 
    1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 합니다. 
    2. 스택의 최상단 노드에 방문한지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 
       방문 처리합니다. 방문하지 않는 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다. 
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다. 

    
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

"""

1  // 1번 노드(초기입력)
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, False, False, False, False, False, False, False]
 i = 2
2  // 1번 노드의 인접한 2 번 부터  
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, False, False, False, False, False, False]
 i = 1
 i = 7
7  // 1번은 방문했기에 7번 노드 
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, False, False, False, False, True, False]
 i = 2
 i = 6
6   // 2번 노드 방문했기에 6번 노드 
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, False, False, False, True, True, False]
 i = 7      // 이미 방문함 
 i = 8      // 7 번할때 남은 8번 노드 
8  
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, False, False, False, True, True, True]
 i = 1    // 방문함
 i = 7    // 방문함
 i = 3    // 맨처음 1번 노드에서 3, 8 남음 
3  
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, False, False, True, True, True]
 i = 1    // 이미 방문함  , 5번 노드 남음 
 i = 4    
4  
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, False, True, True, True]
 i = 3    // 이미방문함
 i = 5
5  
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, True, True, True, True]
 i = 3
 i = 4
 i = 5     // 위에 3번에서 5번노드 남은거
 i = 8     // 8 출력시 3번 노드 돌릴때 8 남은거 

"""


