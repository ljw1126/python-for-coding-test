"""
[BFS(Breadth-First Search) - 너비 우선 탐색]

# 출력 예시 
1 2 3 8 7 4 5 6
"""

from collections import deque 

# BFS 메서드 정의 
def bfs(graph, start, visited):
    # 큐 ( Queue ) 구현을 위해 deque 라이브러리 사용 , 큐에 값 삽입 
    queue = deque([start])
    # 현재 노드를 방문 처리 
    visited[start] = True 
    # 규가 빌 때까지 반복 
    while queue:
        print(f" queue >> {queue}")
        # 큐에서 하나의 원소를 뽑아 출력하기 
        v = queue.popleft()
        #print(v, end = ' ')
        #확인용
        print(v)
        print(f" graph >> {graph}")
        print(f" visited >> {visited}")
        # 아직 방문하지 않는 인접한 원소들을 큐에 삽입 
        for i in graph[v]:
            print(f" i >> {i} ")
            if not visited[i]:
                queue.append(i)
                visited[i] = True 

# 각 노드가 연결된 정보를 표현(2차원 리스트)
# 1번 노드가 인덱스 1번에 해당하도록 하기 위해 0번 인덱스 비움 
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

visited = [False] * 9

bfs(graph, 1, visited)


"""

queue >> deque([1])
1
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, False, False, False, False, False, False, False]
 i >> 2 
 i >> 3 
 i >> 8 

queue >> deque([2, 3, 8])
2
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, False, False, False, False, True]
 i >> 1 
 i >> 7 

queue >> deque([3, 8, 7])
3
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, False, False, False, True, True]
 i >> 1 
 i >> 4 
 i >> 5 

queue >> deque([8, 7, 4, 5])
8
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, True, False, True, True]
 i >> 1 
 i >> 7 

queue >> deque([7, 4, 5])
7
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, True, False, True, True]
 i >> 2 
 i >> 6 
 i >> 8 

queue >> deque([4, 5, 6])
4
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, True, True, True, True]
 i >> 3 
 i >> 5 

queue >> deque([5, 6])
5
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, True, True, True, True]
 i >> 3 
 i >> 4 

queue >> deque([6])
6
 graph >> [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
 visited >> [False, True, True, True, True, True, True, True, True]
 i >> 7 

"""