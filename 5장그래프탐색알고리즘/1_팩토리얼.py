"""
[팩토리얼 구현 예제]
"""

import time 

# 반복적으로 구현한 n! 
def factorial_iterative(n):
    result = 1 
    # 1부터 n 까지의 수를 차례대로 곱하기 
    for i in range(1, n+1):
        result *= i 
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1 : # n이 1이하인 경우 1을 반환 
        return 1 
    # n! = n * (n-1)! 를 그대로 코드로 작성하기 
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n=5)
start_time = time.time()
print('반복적으로 구현:', factorial_iterative(5))
end_time = time.time()
print("time1:", end_time - start_time)

start_time = time.time()
print('재귀적으로 구현:', factorial_recursive(5))
end_time = time.time()
print("time2:", end_time - start_time)