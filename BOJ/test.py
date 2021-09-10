"""
1929번 소수 구하기
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""
# 시간 초과
# import sys 
# a,b = map(int, sys.stdin.readline().split())

# for i in range(a, b+1, 2):
#     for j in range(a,i):
#         if i % j == 0 : 
#             break 
#     else:
#         print(i)

# 제곱근으로 해야 한다네.. 
# TypeError 출력됨..
# import sys
# a,b = map(int, sys.stdin.readline().split())

# prime = [None] * 1001 
# ptr = 0 

# prime[ptr] = 2
# ptr += 1 

# for n in range (a, b+1, 2):
#     i = 0 
#     while ( prime[i] * prime[i] <= n ): 
#         if n % prime[i] == 0 :
#             break 
#         i += 1 
#     else :
#         prime[ptr] = n 
#         ptr += 1
#         print(n)

"""
18258번 큐 2 

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
# from collections import deque
# import sys 

# N = int(sys.stdin.readline())
# queue = deque()
# # queue.reverse() 역순으로 바꾸기 가 있음 
# for _ in range(N):
#     cmd = sys.stdin.readline().split() 

#     if cmd[0] == "push":
#         queue.append(int(cmd[1]))
#     elif cmd[0] == "front":
#         if len(queue) > 0 : 
#             print(queue[0])
#         else:
#             print(-1)
#     elif cmd[0] == "back":
#         if len(queue) > 0 : 
#             print(queue[-1])
#         else:
#             print(-1)
#     elif cmd[0] == "size":
#         print(len(queue))
#     elif cmd[0] == "empty":
#         if len(queue) > 0 :
#             print(0)
#         else : 
#             print(1)
#     elif cmd[0] == "pop":
#         if len(queue) > 0 :
#             print(queue.popleft())   # pop 은 뒤에 원소부터  
#         else : 
#             print(-1)
#     # elif cmd[0] == "dump":
#     #     print(queue)
#     else : 
#         break 

"""
2164번 카드2    ------ 직접 품 
문제
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

출력
첫째 줄에 남게 되는 카드의 번호를 출력한다.
"""
from collections import deque
import sys 

N = int(sys.stdin.readline())
queue = deque() 

for i in range(1, N + 1):
   queue.append(i) 

while len(queue) > 1 : 
    queue.popleft()
    a = queue.popleft() 
    queue.append(a)

print(queue.popleft())
