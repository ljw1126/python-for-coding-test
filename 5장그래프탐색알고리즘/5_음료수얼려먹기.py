"""
[문제설명]
- N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
  구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다. 
  이때 '얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성'하세요.
  다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다. 
  // 0을 한 묶으로 해서 하나로 침 
  ```
  00110
  00011
  11111
  00000
  ```

(입력조건)
    - 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. ( 1<=N,M<=1,000)
    - 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다. 
    - 이때 구멍이 뚫려있는 부분은 0 , 그렇지 않은 부분은 1입니다. 

(출력조건)
    - 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다. 

# 입력예시 
    4 5 
    00110
    00011
    11111
    00000
# 출력예시 
    3

--------------------
- 이 문제는 DFS 혹은 BFS로 해결할 수 있습니다. 
  일단 앞에서 배운대로 얼음을 얼릴 수 있는 공간이 상,하,좌,우로 연결되어 있다고 표현할 수 있으므로 
  그래프 형태로 모델링 할 수 있습니다. 
- DFS를 활용하는 알고리즘은 다음과 같습니다. 
  1. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 
     않는 지점이 있다면 해당 지점을 방문합니다. 
  2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면,
     '연결된 모든 지점을 방문'할 수 있습니다. 
  3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않는 지점의 수를 카운트합니다.    

"""
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료 
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
        
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 
        graph[x][y] = 1 
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출 
        dfs(x-1 , y)
        dfs(x , y-1)
        dfs(x+1 , y)
        dfs(x , y+1)
        return True
    
    # graph[x][y] == 1이면 
    return False 



# N, M을 공백을 기준으로 구분하여 입력받기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기 
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)    // [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# 모든 노드(위치)에 대하여 음료수 채우기 
result = 0 
for i in range(n):
    for j in range(m):
        print(f" i , j >> {i},{j}")
        # 현재 위치에서 DFS 수행 
        if dfs(i,j) == True:
            result += 1


print(result)


"""
# 입력
4 5
00110
00011
11111
00000

# graph 
[[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
 
# 재귀 함수가 원점 기준으로 상,좌,하,우 돌면서 점검함 >> 상,좌,하,우 가 return False 받아서 돌아오면 마지막 return True가 넘어가네 

 i , j >> 0,0
 *x,y = 0,0
 x,y = -1,0
 x,y = 0,-1
    *x,y = 1,0
    x,y = 0,0
    x,y = 1,-1
    x,y = 2,0
        *x,y = 1,1
            *x,y = 0,1
                x,y = -1,1
                x,y = 0,0
                x,y = 1,1
                x,y = 0,2
            x,y = 1,0
            x,y = 2,1
        *x,y = 1,2
            x,y = 0,2
            x,y = 1,1
            x,y = 2,2
            x,y = 1,3
 x,y = 0,1    // 맨 처음 0,0 넣었을때 마지막 0,1 이네 
 
 i , j >> 0,1
 x,y = 0,1
 i , j >> 0,2
 x,y = 0,2
 i , j >> 0,3
 x,y = 0,3
 i , j >> 0,4
 x,y = 0,4
 x,y = -1,4      // return False 
 x,y = 0,3       // return False  
 x,y = 1,4       // return False  
 x,y = 0,5       // return False 
 i , j >> 1,0
 x,y = 1,0
 i , j >> 1,1
 x,y = 1,1
 i , j >> 1,2
 x,y = 1,2
 i , j >> 1,3
 x,y = 1,3
 i , j >> 1,4
 x,y = 1,4
 i , j >> 2,0
 x,y = 2,0
 i , j >> 2,1
 x,y = 2,1
 i , j >> 2,2
 x,y = 2,2
 i , j >> 2,3
 x,y = 2,3
 i , j >> 2,4
 x,y = 2,4
 i , j >> 3,0
 x,y = 3,0
 x,y = 2,0
 x,y = 3,-1
 x,y = 4,0
 x,y = 3,1
 x,y = 2,1
 x,y = 3,0
 x,y = 4,1
 x,y = 3,2
 x,y = 2,2
 x,y = 3,1
 x,y = 4,2
 x,y = 3,3
 x,y = 2,3
 x,y = 3,2
 x,y = 4,3
 x,y = 3,4
 x,y = 2,4
 x,y = 3,3
 x,y = 4,4
 x,y = 3,5
 i , j >> 3,1
 x,y = 3,1
 i , j >> 3,2
 x,y = 3,2
 i , j >> 3,3
 x,y = 3,3
 i , j >> 3,4
 x,y = 3,4

"""

# BFS 
from collections import deque 

# N x M 
n,m = map(int, input().split())

# 그래프 생성 
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 방문여부 선언 visited = [[False] * m for i in range(n)] 

# 상좌하우 탐색( 백터 값 )
dx = [-1,0,1,0]
dy = [0,-1,0,1]


def bfs(x,y):
    # 현재 위치를 큐에 집어 넣음 
    q = deque()
    q.append((x,y))

    # 만약 현재 위치가 1이라면 아이스크림을 만들 수 없는 공간이거나 이미 탐색한 경우
    if graph[x][y] == 1 :
        return False 

    # 현재 위치 기준으로 BFS 탐색 -
    while q : 
        print(f" while 문 q >> {q}")
        x,y = q.popleft()
        print(f" x,y >> {x},{y}")
        # 현재 위치 값을 0에서 1로 변경 
        graph[x][y] = 1
        # 상좌우하 탐색 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(f" nx,ny >> {nx},{ny}")
            # 얼음 틀 범위에서 벗어나지 않고, 그 위치값이 0인 경우에만 queue에 넣음 
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx,ny))
    # 하나의 아이스크림이 만들어지는 공간을 모두 탐색한 경우 True 
    return True 

result = 0 

for i in range(n):
    for j in range(m):
        if bfs(i,j) == True:
            result += 1 


print(result)


"""
# 입력 
4 5
00110
00011
11111
00000

# bfs 
 q >> deque([(0, 0)])
    while 문 q >> deque([(0, 0)])
    x,y >> 0,0
        nx,ny >> -1,0
        nx,ny >> 0,-1
        nx,ny >> 1,0
        nx,ny >> 0,1
    while 문 q >> deque([(1, 0), (0, 1)])
    x,y >> 1,0
        nx,ny >> 0,0
        nx,ny >> 1,-1
        nx,ny >> 2,0
        nx,ny >> 1,1
    while 문 q >> deque([(0, 1), (1, 1)])
    x,y >> 0,1
        nx,ny >> -1,1
        nx,ny >> 0,0
        nx,ny >> 1,1
        nx,ny >> 0,2
    while 문 q >> deque([(1, 1), (1, 1)])
    x,y >> 1,1
        nx,ny >> 0,1
        nx,ny >> 1,0
        nx,ny >> 2,1
        nx,ny >> 1,2
    while 문 q >> deque([(1, 1), (1, 2)])
    x,y >> 1,1
        nx,ny >> 0,1
        nx,ny >> 1,0
        nx,ny >> 2,1
        nx,ny >> 1,2
    while 문 q >> deque([(1, 2), (1, 2)])
    x,y >> 1,2
        nx,ny >> 0,2
        nx,ny >> 1,1
        nx,ny >> 2,2
        nx,ny >> 1,3
    while 문 q >> deque([(1, 2)])
    x,y >> 1,2
        nx,ny >> 0,2
        nx,ny >> 1,1
        nx,ny >> 2,2
        nx,ny >> 1,3
 q >> deque([(0, 1)])
 q >> deque([(0, 2)])
 q >> deque([(0, 3)])
 q >> deque([(0, 4)])
    while 문 q >> deque([(0, 4)])
    x,y >> 0,4
        nx,ny >> -1,4
        nx,ny >> 0,3
        nx,ny >> 1,4
        nx,ny >> 0,5
 q >> deque([(1, 0)])
 q >> deque([(1, 1)])
 q >> deque([(1, 2)])
 q >> deque([(1, 3)])
 q >> deque([(1, 4)])
 q >> deque([(2, 0)])
 q >> deque([(2, 1)])
 q >> deque([(2, 2)])
 q >> deque([(2, 3)])
 q >> deque([(2, 4)])
 q >> deque([(3, 0)])
 while 문 q >> deque([(3, 0)])
    x,y >> 3,0
    nx,ny >> 2,0
    nx,ny >> 3,-1
    nx,ny >> 4,0
    nx,ny >> 3,1
 while 문 q >> deque([(3, 1)])
    x,y >> 3,1
    nx,ny >> 2,1
    nx,ny >> 3,0
    nx,ny >> 4,1
    nx,ny >> 3,2
 while 문 q >> deque([(3, 2)])
    x,y >> 3,2
    nx,ny >> 2,2
    nx,ny >> 3,1
    nx,ny >> 4,2
    nx,ny >> 3,3
 while 문 q >> deque([(3, 3)])
    x,y >> 3,3
    nx,ny >> 2,3
    nx,ny >> 3,2
    nx,ny >> 4,3
    nx,ny >> 3,4
 while 문 q >> deque([(3, 4)])
    x,y >> 3,4
    nx,ny >> 2,4
    nx,ny >> 3,3
    nx,ny >> 4,4
    nx,ny >> 3,5
 q >> deque([(3, 1)])
 q >> deque([(3, 2)])
 q >> deque([(3, 3)])
 q >> deque([(3, 4)])
3


"""








