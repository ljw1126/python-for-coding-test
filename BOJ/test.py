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
